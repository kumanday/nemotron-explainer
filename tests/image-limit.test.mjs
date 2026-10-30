import test from "node:test";
import assert from "node:assert/strict";
import { limitImageInputs } from "../.pi/lib/image-limit.mjs";

const image = (id) => ({ type: "image_url", image_url: { url: `fixture:${id}`, detail: "high" } });
const imagesIn = (payload) => payload.messages.flatMap((message) => Array.isArray(message.content)
  ? message.content.filter((part) => part.type === "image_url").map((part) => part.image_url.url) : []);
function freeze(value) {
  if (value && typeof value === "object") {
    Object.values(value).forEach(freeze);
    Object.freeze(value);
  }
  return value;
}

test("requests at the limit retain object identity and every image", () => {
  const payload = freeze({ messages: [{ role: "user", content: Array.from({ length: 8 }, (_, i) => image(i)) }] });
  const result = limitImageInputs(payload, 8);
  assert.equal(result.payload, payload);
  assert.equal(result.before, 8);
  assert.equal(result.sent, 8);
  assert.equal(result.omitted, 0);
});

test("nine images keep the newest eight without mutating original history", () => {
  const payload = freeze({ model: "target", stream: true,
    messages: Array.from({ length: 9 }, (_, i) => ({ role: "user", content: [image(i)] })) });
  const originalBytes = JSON.stringify(payload);
  const result = limitImageInputs(payload, 8);
  assert.deepEqual(imagesIn(result.payload), Array.from({ length: 8 }, (_, i) => `fixture:${i + 1}`));
  assert.equal(result.before, 9);
  assert.equal(result.sent, 8);
  assert.equal(result.omitted, 1);
  assert.match(result.payload.messages[0].content[0].text, /Earlier image omitted.*8-image limit/);
  assert.equal(JSON.stringify(payload), originalBytes);
  assert.equal(result.payload.stream, true);
});

test("keeps text, tool-call identities and tool results when trimming across messages", () => {
  const system = { role: "system", content: "System instructions" };
  const call = { role: "assistant", content: null, tool_calls: [{ id: "read-1", type: "function", function: { name: "read", arguments: "{}" } }] };
  const tool = { role: "tool", tool_call_id: "read-1", content: "Source path and previous review" };
  const text = { type: "text", text: "Current review instructions" };
  const payload = freeze({ messages: [system, call, tool,
    { role: "user", content: [image("old-1"), text, image("old-2")] },
    { role: "user", content: Array.from({ length: 8 }, (_, i) => image(`new-${i}`)) }] });
  const result = limitImageInputs(payload, 8);
  assert.deepEqual(imagesIn(result.payload), Array.from({ length: 8 }, (_, i) => `fixture:new-${i}`));
  assert.equal(result.payload.messages[0], system);
  assert.equal(result.payload.messages[1], call);
  assert.equal(result.payload.messages[2], tool);
  assert.equal(result.payload.messages[3].content[1], text);
  assert.equal(result.omitted, 2);
  assert.deepEqual(limitImageInputs(result.payload, 8).payload, result.payload);
});

test("a current batch over the limit is marked explicitly rather than silently truncated", () => {
  const payload = { messages: [{ role: "user", content: Array.from({ length: 12 }, (_, i) => image(i)) }] };
  const result = limitImageInputs(payload, 8);
  assert.equal(result.omitted, 4);
  assert.equal(result.payload.messages[0].content.filter((part) => part.type === "text").length, 4);
  assert.deepEqual(imagesIn(result.payload), Array.from({ length: 8 }, (_, i) => `fixture:${i + 4}`));
});

test("text-only requests are unchanged; invalid limits fail explicitly", () => {
  const payload = { messages: [{ role: "user", content: "No images" }] };
  assert.equal(limitImageInputs(payload, 8).payload, payload);
  assert.equal(limitImageInputs({}, 8).sent, 0);
  for (const limit of [0, -1, 1.5, undefined]) assert.throws(() => limitImageInputs(payload, limit), /positive integer/);
});
