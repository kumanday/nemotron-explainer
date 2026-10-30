import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("delivery", Path(__file__).resolve().parents[1] / "scripts/check-delivery.py")
delivery = importlib.util.module_from_spec(spec)
spec.loader.exec_module(delivery)

class DeliveryChecks(unittest.TestCase):
    def test_root_head_is_required_even_if_a_browser_would_infer_it(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "index.html").write_text('<html><body><div data-composition-src="scene.html"></div></body></html>')
            self.assertFalse(delivery.render_head_present(root))
            (root / "index.html").write_text('<html><head><meta charset="utf-8"></head><body><div data-composition-src="scene.html"></div></body></html>')
            self.assertTrue(delivery.render_head_present(root))

    def test_head_inside_body_does_not_satisfy_the_root_contract(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "index.html").write_text('<html><body><template><head></head></template></body></html>')
            self.assertFalse(delivery.render_head_present(root))

    def test_single_hard_cut_does_not_count_as_sustained_motion(self):
        frames = [bytes([0]) * 4] * 20 + [bytes([255]) * 4] * 20
        intervals = delivery.motion_intervals(b"".join(frames), width=2, height=2, fps=2)
        self.assertTrue(any(interval["duration_s"] >= 9 for interval in intervals))

    def test_continuous_change_does_not_produce_static_hold(self):
        raw = b"".join(bytes([i]) * 4 for i in range(40))
        self.assertEqual(delivery.motion_intervals(raw, width=2, height=2, fps=2), [])

    def test_unmounted_video_is_not_accepted_as_composition_content(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "index.html").write_text('<div data-composition-src="scene.html"></div>')
            (root / "scene.html").write_text('<video src="assets/real.mp4"></video>')
            (root / "unused.html").write_text('<video src="assets/unused.mp4"></video>')
            self.assertEqual(delivery.mounted_sources(root), {(root / "assets/real.mp4").resolve()})

    def test_missing_artifact_and_evidence_cannot_pass(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            report = delivery.check(root / "missing.mp4", root, root / "missing.json")
            self.assertFalse(report["passed"])
            names = {item["name"] for item in report["checks"] if not item["passed"]}
            self.assertTrue({"artifact", "generated_footage_evidence", "video_layer", "explanatory_motion_review"}.issubset(names))

if __name__ == "__main__":
    unittest.main()
