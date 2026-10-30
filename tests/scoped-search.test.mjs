import test from "node:test";
import assert from "node:assert/strict";
import { isWholeFilesystemSearch } from "../.pi/lib/scoped-search.mjs";

test("blocks literal root searches including the observed command", () => {
  for (const command of [
    'find / -name "generated_media*" -type d 2>/dev/null | head',
    'find -L "/" -name x',
    "find '/' -type f",
    'grep -rl "Selection revision already exists" / 2>/dev/null | head',
    'grep --recursive error /',
    'rg -l "error" /',
  ]) assert.equal(isWholeFilesystemSearch(command), true, command);
});

test("allows repository searches and direct module introspection", () => {
  for (const command of [
    'rg -n "Selection revision already exists" /Users/magos/dev/media-tooling/src/media_tooling',
    'find . -maxdepth 2 -name "*.json"',
    'find /Users/magos/dev/nemotron-explainer/storyboards -type f',
    'python3 scripts/tool-locations.py',
    'grep -n "error" /Users/magos/dev/media-tooling/src/media_tooling/generated_media.py',
    'ls /',
  ]) assert.equal(isWholeFilesystemSearch(command), false, command);
});
