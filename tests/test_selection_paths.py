import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("selection_paths", Path(__file__).resolve().parents[1] / "scripts/select-take.py")
selection = importlib.util.module_from_spec(spec)
spec.loader.exec_module(selection)

class SelectionPaths(unittest.TestCase):
    def test_precreated_output_draft_is_rejected_before_cli(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            draft = root / "rough-cuts/manifests/selections/edit-1.json"
            draft.parent.mkdir(parents=True)
            draft.write_text('{"edit_revision_id":"edit-1"}')
            with self.assertRaisesRegex(ValueError, "CLI output"):
                selection.prepare(root, draft)

    def test_new_draft_chooses_native_output_path(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            draft = root / "rough-cuts/manifests/drafts/edit-1.source.json"
            draft.parent.mkdir(parents=True)
            draft.write_text('{"edit_revision_id":"edit-1"}')
            output, existing = selection.prepare(root, draft)
            self.assertEqual(output, (root / "rough-cuts/manifests/selections/edit-1.json").resolve())
            self.assertFalse(existing)
            self.assertFalse(output.exists())

    def test_matching_selection_reused_and_changes_require_new_id(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            draft = root / "rough-cuts/manifests/drafts/edit-1.source.json"
            output = root / "rough-cuts/manifests/selections/edit-1.json"
            draft.parent.mkdir(parents=True)
            output.parent.mkdir(parents=True)
            data = {"edit_revision_id": "edit-1", "scenes": []}
            draft.write_text(json.dumps(data))
            canonical = {**data, "document_sha256": "sha256:test", "created_at": "recorded"}
            output.write_text(json.dumps(canonical))
            original = output.read_bytes()
            self.assertTrue(selection.prepare(root, draft)[1])
            data["scenes"] = [{"new": "edit"}]
            draft.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, "choose a new"):
                selection.prepare(root, draft)
            self.assertEqual(output.read_bytes(), original)

if __name__ == "__main__":
    unittest.main()
