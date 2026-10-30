// Nebius limits images across the whole Chat Completions request, including
// replayed tool results. Adapt a copy of the request; keep native history intact.
export function limitImageInputs(payload, limit) {
  if (!Number.isSafeInteger(limit) || limit < 1) {
    throw new Error("Image limit must be a positive integer");
  }
  const messages = Array.isArray(payload?.messages) ? payload.messages : [];
  const isImage = (part) => part?.type === "image_url";
  const before = messages.reduce((count, message) => count + (Array.isArray(message?.content)
    ? message.content.filter(isImage).length : 0), 0);
  const omitted = Math.max(0, before - limit);
  if (omitted === 0) return { payload, before, sent: before, omitted: 0 };

  let remaining = omitted;
  const adapted = messages.map((message) => {
    if (!Array.isArray(message?.content)) return message;
    let changed = false;
    const content = message.content.map((part) => {
      if (!isImage(part) || remaining === 0) return part;
      remaining -= 1;
      changed = true;
      return {
        type: "text",
        text: `[Earlier image omitted from this request to respect Nebius's ${limit}-image limit. `
          + "The original remains in the Pi transcript and source files. Prior review text is retained. "
          + "Re-read the source image if it is needed again; do not infer unseen visual details.]",
      };
    });
    return changed ? { ...message, content } : message;
  });
  return { payload: { ...payload, messages: adapted }, before, sent: before - omitted, omitted };
}
