import { appendFileSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { limitImageInputs } from "../lib/image-limit.mjs";
import { isWholeFilesystemSearch } from "../lib/scoped-search.mjs";

// Static registration is project-local because Pi reads models.json only from
// the agent directory. The standard Pi Chat Completions implementation owns I/O.
export default function (pi: ExtensionAPI) {
  const root = resolve(dirname(fileURLToPath(import.meta.url)), "../..");
  const { provider, ...config } = JSON.parse(readFileSync(resolve(root, "configs/nebius.json"), "utf8"));
  pi.registerProvider(provider, config);
  const ledger = resolve(root, ".pi/evidence/runtime.jsonl");
  let sessionId: string | null = null;
  const record = (event: string, fields: Record<string, unknown> = {}) => {
    mkdirSync(dirname(ledger), { recursive: true, mode: 0o700 });
    appendFileSync(ledger, JSON.stringify({
      schema: "nemotron-demo/runtime-v1", at: new Date().toISOString(),
      run_id: process.env.NEMOTRON_RUN_ID ?? null, session_id: sessionId, event, ...fields,
    }) + "\n", { mode: 0o600 });
  };
  pi.on("session_start", (_event, ctx) => {
    sessionId = ctx.sessionManager.getSessionId();
    record("session_start", { provider: ctx.model?.provider, model: ctx.model?.id,
      base_url: ctx.model?.baseUrl, api: ctx.model?.api });
  });
  pi.on("model_select", (event) => record("model_select", {
    provider: event.model.provider, model: event.model.id, base_url: event.model.baseUrl,
  }));
  pi.on("tool_call", (event) => {
    if (event.toolName !== "bash" || !isWholeFilesystemSearch(event.input.command)) return;
    record("blocked_whole_filesystem_search", { tool: "bash" });
    return { block: true, reason: "Whole-filesystem search is outside this production workflow. Run python3 scripts/tool-locations.py, then use rg on /Users/magos/dev/media-tooling/src/media_tooling or /Users/magos/dev/kumanday/ttv-pipeline. Selection revisions are immutable: read docs/tool-locations.md for the recovered draft/selection paths." };
  });
  pi.on("before_provider_request", (event, ctx) => {
    const original = event.payload as Record<string, any>;
    const selected = config.models.find((model: any) => model.id === original.model);
    const limit = selected?.inputLimits?.images?.maxPerRequest;
    const adapted = ctx.model?.provider === provider && limit
      ? limitImageInputs(original, limit) : null;
    const payload = adapted?.payload ?? original;
    const messages = Array.isArray(payload.messages) ? payload.messages : [];
    const images = messages.reduce((n, message) => n + (Array.isArray(message.content)
      ? message.content.filter((part: any) => part.type === "image_url").length : 0), 0);
    record("provider_request", {
      provider: ctx.model?.provider, model: payload.model, base_url: ctx.model?.baseUrl,
      image_inputs: images, tool_definitions: Array.isArray(payload.tools) ? payload.tools.length : 0,
      max_tokens: payload.max_tokens ?? null, reasoning_effort: payload.reasoning_effort ?? null,
      image_inputs_before_limit: adapted?.before ?? images,
      omitted_image_inputs: adapted?.omitted ?? 0,
    });
    // Return only the wire adaptation. Pi's native transcript and image files
    // retain every image; neither request content nor reasoning enters our ledger.
    if (adapted?.omitted) return payload;
  });
  pi.on("after_provider_response", (event) => record("provider_response", { status: event.status }));
  pi.on("tool_execution_end", (event) => record("tool_end", {
    tool: event.toolName, error: event.isError, duration_ms: event.durationMs ?? null,
  }));
  pi.on("message_end", (event) => {
    const message = event.message;
    if (message.role !== "assistant") return;
    const usage = message.usage;
    record("assistant_end", {
      provider: message.provider, model: message.model, stop_reason: message.stopReason,
      usage: usage ? { input: usage.input, output: usage.output, cache_read: usage.cacheRead,
        cache_write: usage.cacheWrite, total_tokens: usage.totalTokens,
        estimated_cost_usd: usage.cost?.total ?? null } : null,
    });
  });
  pi.registerCommand("demo-route", {
    description: "Show the selected model and endpoint without credentials",
    handler: async (_args, ctx) => {
      const ok = ctx.model?.provider === provider && ctx.model?.id === config.models[0].id
        && ctx.model?.baseUrl === config.baseUrl;
      ctx.ui.notify(`${ok ? "EXPECTED ROUTE" : "ROUTE MISMATCH"}: ${ctx.model?.provider}/${ctx.model?.id}\n${ctx.model?.baseUrl}`, ok ? "info" : "warning");
    },
  });
}
