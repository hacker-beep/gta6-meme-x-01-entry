// gta6-meme-x-01 entrypoint (Node 22, standard library only, no network).
//
// The entry itself is the X post: a GTA 6 meme whose first picture is the ghost
// WANTED poster (meme.png) and whose text carries make.fun plus our play code.
// This program does exactly one thing: it hands POST.json — the file naming that
// post's URL — to the grader by writing it into the output directory. The house
// then reads the post from X itself; nothing this program writes is judged.
//
// Local check: mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const repoDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const FILE = "POST.json";

const source = join(repoDir, FILE);
const target = join(outDir, FILE);

mkdirSync(outDir, { recursive: true });

let payload: Buffer;
try {
  payload = readFileSync(source);
} catch (err) {
  console.error(`cannot read ${source}: ${(err as Error).message}`);
  process.exit(1);
}

// Fail loudly on a malformed post file instead of handing the grader bytes it
// cannot use: POST.json must be a JSON object naming the post's URL.
let parsed: unknown;
try {
  parsed = JSON.parse(payload.toString("utf8"));
} catch (err) {
  console.error(`POST.json is not valid JSON: ${(err as Error).message}`);
  process.exit(1);
}
if (typeof parsed !== "object" || parsed === null || Array.isArray(parsed)) {
  console.error("POST.json must be a JSON object like {\"url\": \"...\"}");
  process.exit(1);
}

try {
  writeFileSync(target, payload);
} catch (err) {
  console.error(`cannot write ${target}: ${(err as Error).message}`);
  process.exit(1);
}
