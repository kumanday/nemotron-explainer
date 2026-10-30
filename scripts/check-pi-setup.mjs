#!/usr/bin/env node
// Inspect the actual Pi resource loader without starting a model or session.
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { homedir } from "node:os";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const agentDir = join(homedir(), ".pi/agent");
const version = readFileSync(join(agentDir, "install/current-version"), "utf8").trim();
const entry = join(agentDir, "install/releases", version, "node_modules/@earendil-works/pi-coding-agent/dist/index.js");
const { DefaultResourceLoader, SettingsManager } = await import(pathToFileURL(entry).href);
const settingsManager = SettingsManager.create(root, agentDir, { projectTrusted: true });
const loader = new DefaultResourceLoader({ cwd: root, agentDir, settingsManager,
  noExtensions: true, additionalExtensionPaths: [join(root, ".pi/extensions/nebius.ts")],
  noPromptTemplates: true, noThemes: true });
await loader.reload({ resolveProjectTrust: async () => true });
const required = ["hybrid-explainer", "media-motion-graphics", "media-tts", "hyperframes",
  "hyperframes-core", "hyperframes-creative", "hyperframes-animation", "hyperframes-registry", "hyperframes-cli"];
const loaded = new Set(loader.getSkills().skills.map((skill) => skill.name));
const missing = required.filter((name) => !loaded.has(name));
const appendLoaded = loader.getAppendSystemPromptSources().some((source) => source.path === join(root, ".pi/APPEND_SYSTEM.md"));
const extensionErrors = loader.getExtensions().errors.map((error) => ({ path: error.path, error: error.error }));
const extensionLoaded = loader.getExtensions().extensions.some((extension) => extension.path === join(root, ".pi/extensions/nebius.ts"));
const report = { passed: missing.length === 0 && appendLoaded && extensionLoaded && extensionErrors.length === 0, pi_version: version,
  required_skills: required, missing_skills: missing, production_system_prompt_loaded: appendLoaded,
  project_extension_loaded: extensionLoaded, extension_errors: extensionErrors,
  limitation: "Discovery advertises skills; the production prompt explicitly requires their full reads." };
writeFileSync(join(root, "analysis/pi-setup-check.json"), JSON.stringify(report, null, 2) + "\n");
console.log(JSON.stringify(report, null, 2));
process.exitCode = report.passed ? 0 : 1;
