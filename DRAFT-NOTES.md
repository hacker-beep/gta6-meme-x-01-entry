# Draft notes — gta6-meme-x-01: "GTA VI — THE MOST WANTED WALLET"

Concept (Eva's verdict, synthesised with bontot): the #3 joke (grinding virtual GTA money
vs the ghost already cashing out real USDC) inside the #2 visual language (GTA 5-star
WANTED poster). Composition rule (bontot, agreed by all): in EVERY draft the ghost + the
5 wanted stars DOMINATE the frame; the grinding player is small/secondary only.
All three drafts use the REAL make.fun ghost mark from the press kit
(`assets/mark-1024.png`, taken from the official press-kit zip at
https://make.fun/press/make-fun-press-kit.zip) — never redrawn.

## The three drafts

### V1 — classic WANTED poster (RECOMMENDED)
`drafts/meme-v1.png` — gold double frame; WANTED + 5 gold stars; ghost mugshot (460px);
"LAST SEEN: VICE CITY" (gold); "REWARD: REAL USDC" (white); "make.fun" (pink).

> REVISED in round 2 (Eva's verdict) — see "Revision (Eva round 2)" at the end of this
> file. The "REWARD: REAL USDC" line no longer exists; it reads
> "THE GHOST ALREADY CASHED OUT" now. The rest of this section describes round 1.
- Punchline: wanted-poster absurdity + reward in real USDC. The grinding contrast lives
  in the post text (Eva's punchline), so the full joke lands when image + text are read
  together — which is exactly how the judge reads them.
- GTA identity: strongest of the three in-image — 5-star wanted level AND "LAST SEEN:
  VICE CITY" (Vice City is GTA VI-specific, criterion 3's own example list).
- Selling: "REWARD: REAL USDC" sells make.fun's real-money bounties inside the picture.
- Readability at 480px: PASS — every line readable, ghost unmistakable (sparkle eyes +
  star coin visible), nothing cut off.
- Cleanliness: balanced poster layout, nothing crowded. The frame makes it read as one
  poster, not pasted elements.

### V2 — contrast (CASHED OUT. vs still grinding)
`drafts/meme-v2.png` — WANTED + 5 stars; ghost (480px); "CASHED OUT." + "REAL USDC ·
make.fun"; small dim strip at the bottom: cash-stack icon + "everyone else: still
grinding GTA$".
- Punchline: STRONGEST in-image joke of the three — the full #3 contrast is visible in
  the frame alone, no post text needed. A GTA fan gets it in one second.
- GTA identity: weakest of the three in-image — WANTED + stars + "GTA$" say GTA, but
  nothing says GTA *VI* (no Vice City / Leonida / 13-year anchor). The post text must
  carry the GTA VI anchor for this draft.
- Selling: strongest in-image selling — "CASHED OUT." + "REAL USDC · make.fun".
- Readability at 480px: PASS after one fix — the first render had the cash icon
  overlapping the word "everyone"; fixed by centering the icon + text as one group.
  Main lines all readable; the strip is small but legible and correctly subordinate.
- Cleanliness: good — the strip is dim and small, ghost + stars dominate per the rule.
- Verdict: the punch-first alternative. Best second submission / iteration candidate if
  V1's dev board suggests the joke needs more punch in-image.

### V3 — minimal (ghost huge, one line)
`drafts/meme-v3.png` — 5 gold stars; ghost HUGE (660px); "WANTED IN LEONIDA"; "make.fun".
- Punchline: weakest in-image — no cash-out / reward line at all. The joke depends
  entirely on the post text. "WANTED IN LEONIDA" + ghost is amusing, but the #3 joke is
  absent from the picture.
- GTA identity: strong — "LEONIDA" is GTA VI-specific.
- Selling: weakest in-image — only the "make.fun" name; no USDC / earning line.
- Readability at 480px: PASS — least text, most readable, ghost most dominant.
- Cleanliness: cleanest of the three.
- Verdict: fallback minimalist. Best if the field turns out to reward pure branding over
  joke density — but on the stated criteria the picture should carry more of the joke.

## Punchline test (in the post text, not the image)
- Eva's candidate: "Everyone's grinding GTA money. The ghost already cashed out."
  Two beats, the contrast IS the joke, instantly gettable. WINS — used in caption option 1.
- My alternative: "13 years waiting for GTA VI. The ghost got paid in week one."
  Adds the 13-year-wait anchor (criterion 3), but "got paid in week one" is vaguer (paid
  by whom?) and slightly claim-like. Kept as caption option 2 with a clarifying rewrite
  ("already got paid — on make.fun") so the payer is unambiguous.

## 480px verification (judge view)
All three drafts downscaled to 480x480 and inspected: ghost recognisable in all three
(sparkle eyes + magenta star coin visible); every primary text line readable; nothing
important cut off. V2's strip text is small by design (secondary element) but legible.
Full-size files are 1024x1024; the judge shrinks to at most 512px a side, then to a
768x480 JPEG view — the 480px check covers the worst case.

## Satire guardrail check (Eva, binding)
No draft claims GTA 6 pays USDC. The USDC is the poster's "reward" for the wanted ghost
(V1) / the ghost's own cash-out (V2) — both read as meme/satire, and the post text states
the earning happens on make.fun. No fabricated wallet screenshot or withdrawal proof in
any draft. The ghost-as-fugitive premise is inherently absurd, not a factual claim.

## Recommendation
**Ship V1 first.** It is the only draft that scores on all seven criteria inside the
picture: ghost (C1), wanted-poster joke + reward (C2), Vice City (C3), REWARD: REAL USDC
(C4), readable (C5), original execution of a known format (C6), clean poster (C7). The
post text adds the grinding contrast (Eva's punchline), completing the #3 joke.
V2 is the designated second submission if the dev board / Feed shows the field rewarding
in-image punch over GTA-VI anchoring. V3 stays a fallback.

## For Eva's next evaluation
- Q1: V1 (completeness) vs V2 (punch) — is the in-image grinding contrast worth losing
  the Vice City anchor? My call is V1 first, V2 second.
- Q2: does "REWARD: REAL USDC" (V1) read as satire to you, or does it risk looking like a
  factual earnings claim? I judge it satire (a ghost fugitive with a USDC bounty), but
  flag it for your check.

## Revision (Eva round 2) — V1 revised, V2/V3 untouched

Eva's verdict on the round-1 drafts:
- Q1: V1 is the first submission candidate (V2 second, V3 fallback). V1 wins on
  criteria completeness: GTA VI anchor, in-image branding, connection to make.fun.
  Caption must stay short and COMPLEMENT the joke, not be its only source.
- Q2: "REWARD: REAL USDC" is ambiguous between satire and a financial reward promise
  and must be replaced. Eva's recommended replacement: "THE GHOST ALREADY CASHED OUT".

### What changed (this session)
- `build-memes.py` (`v1_poster` only): the "REWARD: REAL USDC" line (font 56) is now
  "THE GHOST ALREADY CASHED OUT" (font 50, tracking 1; measured 873.6px incl.
  tracking, fits the 944px inside the gold frame with margin). Everything else in V1
  is unchanged: gold double frame, WANTED + 5 gold stars, ghost mugshot (460px, real
  press-kit mark), "LAST SEEN: VICE CITY" (gold, font 40), "make.fun" (pink, font 38).
  No other element was shrunk; the ghost + stars still dominate the frame.
- `drafts/meme-v1.png` regenerated from the edited script (sha256
  0c720342550522c54122ed617d0cf5dff1deff17fd4ac105c0cd274eb96782a4); `meme.png`
  updated to the revised V1 (same hash). V2/V3 files were NOT rewritten.
- `drafts/contact-sheet.png` rebuilt from the three PNGs on disk (now shows revised V1).
- `POST-TEXT.md` option 1 rewritten so the caption COMPLEMENTS the in-image punchline
  instead of duplicating it: the image carries the payoff ("THE GHOST ALREADY CASHED
  OUT"), so the caption carries the grinding setup ("Everyone's grinding GTA money.")
  + the make.fun pitch + link + play code. The phrase "the ghost already cashed out"
  appears nowhere in the caption. Option 2 also revised: its "already got paid" beat
  paraphrased the image's payoff, so it now reads "13 years waiting for GTA VI.
  Everyone's still grinding GTA money." (keeps the 13-year C3 anchor, no duplication).

### Re-verification (Eva's pre-submission checklist)
1. 480px legibility (judge view): revised V1 downscaled to 480x480 and visually
   inspected — PASS. Ghost unmistakable (sparkle eyes + magenta star coin visible);
   EVERY line readable, including the new longer line on one line with margin inside
   the frame; nothing cut off; poster still clean and uncrowded.
2. Hard filter: PASS — the real make.fun ghost is large (460px mugshot) and
   unmistakable in the picture; "make.fun" also appears in pink at the bottom.
3. Caption check: PASS — option 1 is 4 short lines, complements (setup + pitch) the
   in-image payoff without duplicating it; the two-beat joke still lands when image +
   text are read together, as the judge reads them.
4. No fake claims: PASS — no reward promise remains anywhere in the image or the
   caption ("REWARD" appears nowhere in the revised V1 or POST-TEXT.md); no fabricated
   wallet or withdrawal proof. "THE GHOST ALREADY CASHED OUT" is the ghost's completed
   joke action on the poster, not an offer to the reader; the caption states the
   earning happens on make.fun.
5. main.ts double-run: PASS — two runs byte-identical (sha256
   09be0a598afaedecb3b98d30c0c3df66494c7244e7cc46407af919b0c018913c, same as round 1;
   main.ts itself unchanged).

### Status after revision
V1 (revised) is the submission candidate, pending bontot's independent verification
of the revised version (Eva's checklist item 5 — parent's step) and the human posting
it from @yaampungil. Do NOT submit the old V1 (superseded).

## V2 REBUILD — rich AI scene (this session, 19 Nov ~22:47–22:52 WIB)

### Why
V1 (PIL poster) was judged TOO PLAIN by the user against the live leaderboard
standard: every top entry is a rich AI-generated scene with a visual story and
joke text baked into the image. The user approved a rebuild after seeing the
rank-1 entry ("Lucia Wasn't the Only One Released Today", a rich AI prison-release
scene) and an example image from Eva. Same concept, new execution: V2 = rich AI
scene, grinding vs cashed out + WANTED framing, punchline baked into the image.

### How (this session, recorded)
Generated with `media.generate_image` in THIS session (3 calls), Eva's image as a
richness/composition reference + the real press-kit ghost (`assets/mark-1024.png`)
as the ghost reference. Prompts specified the scene, the exact text lines, and the
satire guardrail (no withdrawal receipt, no USDC amount). The model rendered the
baked-in text CORRECTLY on the first try for both variants, so the PIL text
fallback was NOT needed. No "Grand Theft Auto VI" logo in either variant (logo
fallback per brief — Vice City + stars + WANTED carry the GTA-VI-ness; no retry
burned on the logo). Generated files came out 1600x1600 and were resized to
1024x1024 per the brief (raw 1600px files kept under their `media-generation-*`
names). `meme.png` was NOT overwritten — the parent decides after verification.

### Variants
- **A** — `drafts/meme-v2-scene-a.png` (sha256
  ebb3e24d344021fc9d4d4aaf70309088123c170f004417c813ff6dff87f4330d):
  ghost center-frame with sunglasses + gold make.fun chain, holding a wallet with
  coins spilling + the magenta star coin; WANTED poster top-right ("DEAD OR CASHED
  OUT", 5 stars); grinder at left ("+125 Grinding..."); Vice City neon, skyline,
  helicopter, pink sports car; bottom text both lines spelled correctly.
  Weaknesses: (1) sunglasses HIDE the ghost's signature sparkle eyes — the ghost
  is still recognizable (white ghost + star coin + make.fun name), but the most
  distinctive mark feature is covered; (2) composition tracks Eva's reference
  layout closely (same element arrangement), so it reads as a variation of her
  image rather than a fully original composition; (3) a few tiny garbled glyph
  fragments on the poster's right edge ("E6", "IT" — barely visible at 480px).
  Backup, not the pick.
- **B** — `drafts/meme-v2-scene.png` (THE PICK; sha256
  e4bf8c35c34d28e5544f74ca518f5ae356925fecc34eab94318655e5c9544acc):
  ghost LOUNGING on the hood of a pink convertible at golden-hour sunset, sparkle
  eyes visible, holding the magenta star coin, wallet full of gold coins beside
  it; WANTED poster on the wall behind (5 stars); grinder small at left ("+125
  Grinding..."); Vice City neon, beach skyline, helicopter, palms; top text
  "Everyone's grinding GTA money.", bottom text "The ghost already cashed out.",
  "make.fun" bottom-right. Original composition — the lounging-on-the-car gag is
  its own visual joke (relaxed, already rich) and differs from both Eva's image
  and rank 1's prison scene.
  One fix applied: the first render garbled the poster line as "DEAD OR OR CASHED
  OUT" (duplicated "OR"). Fixed in-session via a resume edit on the snapshot —
  the poster now reads "DEAD OR / CASHED OUT" (two lines, correct). All other
  elements unchanged by the edit (verified visually).
  Remaining weaknesses (honest): (1) the poster's "CASHED OUT" line sits partly
  behind the ghost's coin hand at full size — still reads fine at 480px, but the
  overlap is visible up close; (2) no GTA VI logo and no 13-year anchor in-image
  (the "GTA money" text + Vice City carry C3; caption option 2 has the 13-year
  anchor if the parent wants it); (3) the grinder detail is very small at 480px
  (secondary by design); (4) the ghost is an AI stylization of the press-kit
  mark, not the exact mark — recognizably the same character (white ghost,
  sparkle eyes, magenta star coin) plus the "make.fun" name in-image.

### 480px verification (judge view) — B (the pick)
Downscaled to 480x480 (`drafts/check480/meme-v2-scene-480.png`) and visually
inspected: PASS. Both baked-in lines fully readable; ghost large and unmistakable
(sparkle eyes + magenta star coin); WANTED + 5 stars + "DEAD OR CASHED OUT"
readable; "make.fun" readable bottom-right; grinder detail present but small
(secondary, as designed); no garbled text visible. A also passes 480px
(`drafts/check480/meme-v2-scene-a-480.png`).

### Self-check vs the 7 criteria — B (the pick)
1. Hard filter (ghost/logo/name IN picture): PASS — ghost large + recognizable,
   plus "make.fun" name in-image.
2. Funny: the two-beat joke is fully in-image (grinding setup top, cash-out
   payoff bottom) AND visual (ghost lounging rich on a sports car while a gamer
   grinds in the background). A GTA fan gets it in one second.
3. GTA VI specifically: Vice City neon, 5-star wanted level, WANTED poster,
   palms/sunset/helicopter/sports car, "GTA money" in the text. No Lucia/Jason
   or 13-year anchor in-image — good, not perfect.
4. Sells make.fun: ghost-as-earner visual (wallet of coins, sports car) +
   "make.fun" name; the explicit pitch ("agents earn real money") lives in the
   caption, as in V1. Decent.
5. Caption short + readable: both baked-in lines are short and readable at 480px.
6. Original: own composition, distinct from Eva's reference and rank 1's image.
7. Clean: rich but organized — top/bottom text banners, ghost dominant,
   background details don't fight the foreground.
Satire guardrail: PASS — no withdrawal receipt, no USDC amount anywhere. The
wallet holds plain gold coins with no numbers; the only number on screen is
"+125" on the grinder's monitor (GTA money, the joke's setup — not a USDC claim).

### Status after rebuild
`drafts/meme-v2-scene.png` (B, fixed) is the V2 submission candidate, pending the
parent's verification round (bontot independent check + Eva if the parent wants
it) and the human posting it from @yaampungil. A stays as the backup variant.
`meme.png` still holds revised V1 — do NOT overwrite until the parent decides
V2 replaces it. POST.json / main.ts / README / LICENSE untouched by this session.

## V2 FIX — coin-hand occlusion (2026-11-19 ~22:55 WIB, fix session)

Bontot's independent verification of V2 found ONE defect: the ghost's
coin-holding hand occluded the "C" of "CASHED OUT" on the WANTED poster
(confirmed at full resolution). Verdict was NOT ready to submit until fixed.
Everything else passed.

Fix (one media.generate_image edit call, in this session, on
drafts/meme-v2-scene.png): the edit moved the ghost's coin hand from the
right side (next to the poster) to the ghost's left side, holding the pink
star coin clear of the poster. No other change was requested or made.

### Fixed file
- `drafts/meme-v2-scene-fixed.png` — 1024x1024 PNG, sha256
  f03c8ca18d15a47505792784d96bf1f39924a7b644ad1e3610a085cd29a3ceab
- Raw 1600px edit kept as
  `drafts/media-generation-meme-v2-scene-fixed-0-3607ff22-a9ed-46e5-b995-c437adeaf49f.png`
- 480px check: `drafts/check480/meme-v2-scene-fixed-480.png`

### Checks (inspected visually at full size AND 480px)
- "DEAD OR CASHED OUT" FULLY visible, no occlusion — FIXED.
- All other text still spelled correctly: "Everyone's grinding GTA money." /
  "The ghost already cashed out." / "WANTED" / 5 stars / "make.fun" /
  "+125 Grinding...".
- Ghost, pink convertible, Vice City background, wallet of coins, grinder —
  unchanged in composition. The ghost's pose shifted slightly as a side
  effect of moving the hand (it now holds the coin on its left); same
  character, same style, still dominant and clearly the make.fun ghost.
- No new defects, no fake amounts introduced. Satire guardrail still PASS.
- 480px: both headlines readable, ghost unmistakable, WANTED + 5 stars +
  "DEAD OR CASHED OUT" readable, "make.fun" readable. "+125 Grinding..."
  unreadable at 480px by design (accepted by the verifier).

### Originals untouched
- `drafts/meme-v2-scene.png` sha256 e4bf8c35... (unchanged).
- `meme.png` still revised V1, sha256 0c720342... (unchanged).
- POST.json / main.ts / README / LICENSE untouched by this session.

### Status after fix
`drafts/meme-v2-scene-fixed.png` is the V2 submission candidate, pending the
parent's next steps (Eva evaluation per bontot's verdict, then the human
posting it from @yaampungil). No retry was needed — the first edit passed
all checks.

---

## ENTRY 2 DRAFTS — wait+paid pivot (2026-11-19 ~23:18 WIB)

Context: entry 1 ("The Ghost Already Cashed Out", V2 grinding scene)
finished dev grading at 59.1271% (2W 3D 7L), rank ~166/368, vs paid
cutoff 72.7243%. Eva ruled a STRATEGIC PIVOT: do not polish grinding;
test wait+paid as the entry-2 candidate. Top-50 census: wait 22,
sick-day 11, download 7, paid 5, grinding 0. Eva's caution: the top-50
pattern is a strategic signal, NOT causal proof.

Three drafts were briefed (W1 main time-split, W2 birthday, S1
sick-day). **Only 2 of 3 could be built — see W1 below.**

### W1 — "13 YEARS LATER" time-split — NOT BUILT (generation failed)

- The media generation call for the W1 time-split scene
  (2013 vs 2026, young vs bearded gamer, ghost lounging on coins)
  returned an integrity failure and produced no image. Per the
  standing instruction on failed media calls it was NOT retried in
  any form — no reworded prompt, no alternate endpoint.
- There is therefore NO W1 draft file. The main wait concept
  (time-split) has no visual to evaluate. If the team still wants
  a time-split draft, it needs a fresh brief/decision from the
  parent — this session cannot produce it.

### W2 — "13TH BIRTHDAY" (wait variant)

- File: `drafts/meme-v3-wait-b.png` — 1024x1024 PNG, sha256
  bbb117544a587c3afab106ec65953590ff41ae37ff503df0e802beb5adc4b63c
- Raw 1600px generation kept as
  `drafts/media-generation-meme-v3-wait-b-0-ed94f65f-a766-4679-bffe-0b49ae3154e7.png`
- Concept: the ghost blows out 13 candles on a birthday cake at a
  party; a faded, dusty "GTA VI — COMING SOON" poster hangs behind
  it; plain gold coins sit beside the cake as the ghost's present.
  The birthday IS the 13-year wait, personified; the present is
  the paid punchline.
- Exact in-image text: "13TH BIRTHDAY" / "STILL NO GTA VI." /
  "THE GHOST GOT ITS PRESENT ANYWAY." (bottom, two lines) /
  poster "GTA VI — COMING SOON" / "make.fun" wordmark bottom-right.
  All spelled correctly.
- Ghost: white, thick black outline, two black four-pointed
  sparkle eyes clearly visible, round hand holding the magenta
  star coin. Dominant, center-right. (It has a small puckered
  blowing mouth for the candles — reads as the blowing action,
  not a third eye.)
- Guardrail check: PASS. Coins plain, no amounts, no receipts,
  no screens. Only joke number is 13. No claim GTA pays USDC.
- Originality: birthday device is not on the board's taken list
  (no prison/tally, no doctor's note, no queue, no download bar,
  no ghost-as-dead-waiter). Wording differs from "The Ghost Got
  Paid While We Waited".
- 480px check (`drafts/check480/meme-v3-wait-b-480.png`): PASS.
  All three text lines readable; ghost unmistakable; poster
  "GTA VI / COMING SOON" readable; "make.fun" readable; coins
  visible. No defects found.

### S1 — "CALLED IN SICK, NEVER WENT BACK" (sick-day alternative)

- File: `drafts/meme-v3-sick-a.png` — 1024x1024 PNG, sha256
  8367ffa77eb54305bf43cf09007828ff9229b188fc7f0bb2ab0ffce2173c63ff
- Raw 1600px generation kept as
  `drafts/media-generation-meme-v3-sick-a-0-d7821eac-fe1f-43d4-8867-a041558eec4c.png`
- Concept: the ghost in a bright modern office cheerfully hands
  a resignation letter reading "I QUIT" to a small, surprised
  boss; a GTA VI poster on the wall; plain gold coins on the
  desk. It called in sick for launch day and quit, because
  make.fun pays better. NOT a doctor's-note image: the letter is
  a resignation, and no medical imagery appears anywhere.
- Exact in-image text: "CALLED IN SICK FOR GTA VI LAUNCH."
  (top, two lines) / "NEVER WENT BACK." (bottom) / "I QUIT" on
  the letter / poster "grand theft auto VI / WELCOME TO LEONIDA"
  / "make.fun" wordmark bottom-right. All spelled correctly.
- Ghost: white, thick black outline, two black four-pointed
  sparkle eyes clearly visible (with small white glints), smiling
  mouth, holding the magenta star coin. Dominant, center frame;
  boss small and secondary.
- Guardrail check: PASS. Coins plain, no amounts, no receipts,
  no screens. No dollar/USDC figure anywhere.
- Originality: resignation twist is not on the board's taken
  list (no doctor's note, no queue/boss-in-line angle — the boss
  here is the resignation recipient, not a queue rival; no
  download bar, no prison).
- 480px check (`drafts/check480/meme-v3-sick-a-480.png`): PASS.
  Both headlines + "I QUIT" readable; ghost unmistakable;
  "make.fun" readable; coins visible. Poster text is small at
  480px (background detail only — acceptable).
- Minor defect (not fixed, not worth a fix call): the wall
  poster's title renders as "gRand theft auto VI" with odd
  mixed-case capitalization. Background detail, barely legible
  at 480px, does not touch the joke.

### Contact sheet

- `drafts/contact-sheet-v3.png` — W2 (left) + S1 (right) side by
  side, 1024x512, sha256
  7ff46b0ce76514e4378197614aee52c5f14a02fd013e79f7502dac29ae29b624
  (2 drafts only — W1 does not exist.)

### Drafter's ranking (my own judgment)

1. **S1 (sick-a) — strongest draft.** The joke lands in one beat:
   "called in sick, never went back" + the "I QUIT" letter is a
   visual punchline that needs no setup. The ghost is the biggest
   and most central of the two drafts, the bottom line is the
   shortest and punchiest, and the resignation twist is original
   within the proven sick-day lane (11/50). Cleanest composition
   at 480px.
2. **W2 (wait-b) — close second.** The birthday device is
   charming and original, and the wait anchor is the most direct
   of any draft ("13TH BIRTHDAY" IS the 13-year wait). Slightly
   weaker than S1 because the joke needs two inferential steps
   (birthday = 13 years waiting, then present = paid) and the
   bottom line is the longest text in either draft.
3. **W1 — not ranked (does not exist).**

STRATEGIC NOTE (tension to flag, not to resolve here): Eva
prioritized the 13-year wait as the MAIN anchor and sick-day as
the alternative. By draft strength I rank S1 first — but W2 is
the only wait draft that exists, so if the team wants to test
the wait hypothesis as Eva directed, W2 is the vehicle. Draft
strength and strategic priority point at different drafts; the
peli/bontot evaluation + Eva's verdict should decide.

### Untouched

- `meme.png`, `POST.json`, `main.ts`, `README.md`, `LICENSE`
  untouched. No commit, push, submit, X post, or recording.
  `drafts/meme-v2-scene*.png` and `drafts/meme-v1.png` untouched.

### Status after drafts

Two entry-2 drafts ready for independent peli/bontot evaluation
(W2 wait, S1 sick-day). W1 (main time-split) missing due to a
failed, unretryable generation — parent decision needed on
whether to re-brief it, proceed with W2 as the wait candidate,
or proceed with S1. No submission before Eva's approval.
