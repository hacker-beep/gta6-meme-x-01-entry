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

## Entry 2 — angle D: "13 YEARS OF 'COMING SOON'" time-split rebuild (SAMPLE ONLY, 2026-11-19 ~23:41 WIB)

Context: the user rejected the W2/S1 drafts ("jelek jokesnya" — too
clever, multi-step), then sent his own concept image (pixel-art
time-split: 2013 young broke gamer vs 2026 same man old, phone showing
a make.fun +500 USDC bounty reward) and asked for a REBUILD of that
concept as a sample to look at — no submission, no quota. Angle D is
that rebuild, executed originally (own style, composition, text).

### Draft D1 — meme-v3-time-a.png (time-split)

- File: `drafts/meme-v3-time-a.png`, 1024x1024 PNG (generated at
  1600x1600, downscaled to 1024), sha256
  b73bd75ed1bb78e914917f109cbb9b717cdfa7446e9e511f2fc9380fe052e963
- 480px check: `drafts/check480/meme-v3-time-a-480.png`, sha256
  f650eec55267f8bee5dd542c760bd59fae3e35a1227dfe422b1e0df08a039b62
- Concept: split-screen. LEFT (2013): the make.fun ghost YOUNG,
  holding an OPEN EMPTY wallet; behind it a fresh, bright "GTA VI —
  COMING SOON" poster. RIGHT (2026): the SAME ghost now OLD (gray
  hair, round glasses, small gray goatee), the same poster now
  FADED, torn, and cobwebbed — the sign never changed, the ghost
  aged. A pile of PLAIN gold coins beside the old ghost; it holds
  the magenta star coin. The ghost is the protagonist in BOTH
  panels, large and dominant, sparkle eyes visible.
- Exact in-image text: top `13 YEARS OF 'COMING SOON'.` (white),
  bottom `THE GHOST GOT PAID FOR WAITING.` (pink), small labels
  `2013` (left) and `2026` (right), make.fun wordmark
  bottom-right. Poster text in both panels: `GTA VI / COMING SOON`.
- Guardrail check: PASS. No phone, no receipt, no dollar/USDC
  amount anywhere; coins are plain gold with no numbers. The joke
  is the wait itself becoming paid work — no claim GTA pays USDC.
- Dropped from the user's concept (per brief): the +500 USDC phone
  (fake receipt, forbidden), thought bubbles + long Indonesian
  pitch text (480px-illegible), portrait format, tiny corner
  ghost, human protagonist. English only, 2 main lines only.
- Originality: distinct from the taken board concepts — the ghost
  does NOT die/become a ghost (vs "I BECAME A GHOST"); it IS the
  waiter, not a bystander (vs "The Ghost Got Paid While We
  Waited"); the unchanged COMING SOON sign gag is not on the board
  as far as the titles show.
- 480px verdict: PASS with one minor defect (below). Both main
  lines readable, year labels readable, both posters readable
  (fresh vs faded contrast clear), ghost recognisable in both
  panels, wordmark readable, no occlusion.
- Minor defect (left as-is, sample only): the top line's closing
  quote + period are clipped at the right edge — it renders as
  `13 YEARS OF 'COMING SOON` with no visible closing quote or
  period. The line still parses cleanly; only the punctuation is
  lost. (Fix would need a new generation call.)
- Note: the old ghost has a human-ish face (ears, nose, smile,
  goatee) vs the young ghost's blank face — the aging reads
  clearly and the sparkle eyes + sheet body keep it recognisably
  the make.fun ghost. Stylistic interpretation, not a defect.

### Untouched

- `meme.png` (still `f03c8ca1…`), `POST.json`, `main.ts`,
  `README.md`, `LICENSE` untouched. No commit, push, submit, X
  post, or recording. All existing draft files untouched.

### Status

One angle-D sample draft ready for the user to look at. No
evaluation or submission step taken — parent decides next.

## Entry 2, angle D — FIX (2026-11-19 ~23:46 WIB): right poster OUT NOW

User verdict on the D1 sample (`meme-v3-time-a.png`): left panel fine, but
the right panel was logically wrong — it is 2026 and GTA VI has RELEASED,
so its poster cannot still say COMING SOON. Fixed in a new file; the
original draft is untouched.

### D1-fix — `drafts/meme-v3-time-b.png`

- 1024x1024 PNG (generated at 1600x1600, downscaled), sha256
  `404d924918e586c92baa7aa1979d94c17d485473e40ef6556acea180b581da11`.
  480px check: `drafts/check480/meme-v3-time-b-480.png`, sha256
  `42c200604f8b8c6d831b10d6fce2c21292ceeea134948bc2b963a0700c63db80`.
- What changed (ONE change + one punctuation repair, per the fix brief):
  1. Right panel poster: COMING SOON → OUT NOW. The 2026 poster is now
     a fresh, bright `GTA VI / OUT NOW` poster pasted OVER the old faded
     COMING SOON poster, with one peeling corner revealing the old text
     underneath (reads `COMIN SOON`, partially covered). The joke is
     now: after 13 years of "coming soon", the sign FINALLY says OUT
     NOW — and the ghost is old and already paid.
  2. Top line punctuation: the closing quote is now FULLY VISIBLE
     inside the frame (`13 YEARS OF 'COMING SOON'`).
- Kept identical: left panel (young ghost, open empty wallet, fresh
  bright COMING SOON poster, label `2013`); old ghost (gray hair, round
  glasses, small gray goatee, sparkle eyes, magenta star coin); plain
  gold coin pile; bottom line `THE GHOST GOT PAID FOR WAITING.` (pink);
  year labels `2013` / `2026`; make.fun wordmark bottom-right.
- Guardrail check: PASS. No phone, no receipt, no dollar/USDC amount
  anywhere; coins are plain gold with no numbers.
- 480px verdict: PASS. Both main lines fully readable, both posters
  readable (COMING SOON left, OUT NOW right, peeling corner visible),
  year labels readable, ghost recognisable in both panels, wordmark
  readable, no text cut off or occluded.
- Minor defect (new, honest): the top line's trailing PERIOD after the
  closing quote is not discernible — it renders as
  `13 YEARS OF 'COMING SOON'` with no clear `.`. The quote fix landed;
  the period did not. The line still parses cleanly; punctuation-only.
- Minor note: the peeling corner reveals only partial old text
  (`COMIN SOON` — the G of COMING is hidden). At 480px it is small but
  the "old poster underneath" device still reads.
- Carried over from D1 (unchanged by design): the old ghost's human-ish
  face (ears, nose, smile, goatee) — the aging reads clearly, weakest
  visual element.

### Untouched

- `meme-v3-time-a.png` (still `b73bd75e…`), `meme.png` (still
  `f03c8ca1…`), `POST.json`, `main.ts`, `README.md`, `LICENSE`
  untouched. No commit, push, submit, X post, or recording. All other
  existing draft files untouched.

### Status

Fixed angle-D sample draft ready for the user to look at. No evaluation
or submission step taken — parent decides next.

---

## Entry 2 — user's concept: ghost finally playing GTA VI + earning (sample)

### meme-v3-ghost-a.png (sha256 `21733ebf…`)

- Concept: the user's own concept — a gamer waits 13 years for GTA VI,
  becomes a ghost (died waiting), and finally plays GTA VI as a ghost
  while earning on make.fun. Three-beat arc (wait → death → play + earn);
  death didn't stop him — he got the game AND the money. Single scene,
  NOT a split.
- Scene: classic make.fun ghost (white sheet, thick black outline, two
  black four-pointed sparkle eyes, BLANK face — no human features) sits
  on a couch holding a game controller, facing a big TV showing Vice City
  gameplay (palm trees, neon "Vice City" sign, sunset skyline, cars; no
  GTA VI logo). Pile of plain gold coins on the table beside the
  controller, magenta star coin visible among them. Dusty old COMING SOON
  poster on the wall behind, small and faded. Warm evening light, TV glow
  on the ghost.
- Text, all spelled correctly: top `WAITED 13 YEARS FOR GTA VI.` (white);
  bottom `FINALLY PLAYING. EARNING ON MAKE.FUN.` (pink); make.fun
  wordmark bottom-right. Both lines fully inside the frame.
- Death beat is VISUAL-ONLY: the ghost IS the dead gamer; the text never
  says "became a ghost", "died", "dead", or "came back" (those words are
  owned on the board by "I BECAME A GHOST" 76.90% and "DIED WAITING. CAME
  BACK FOR LAUNCH DAY" 78.99%). Our differentiator is the EARNING beat,
  which neither of them has.
- Guardrail check: PASS. No phone, no receipt, no wallet screenshot, no
  dollar/USDC amount; coins plain. "EARNING ON MAKE.FUN" = bounties, and
  the wordmark + coins carry it; no claim GTA pays.
- 480px verdict: PASS (`check480/meme-v3-ghost-a-480.png`, sha256
  `c52abdf8…`). Both main lines fully readable, ghost unmistakable, TV
  reads as Vice City, coins visible, wordmark readable, no text cut off
  or occluded.
- Minor defect (honest): the COMING SOON poster is clipped at the left
  frame edge — only a sliver is visible ("...NG / ...ON"), its text not
  readable. Background detail only; the joke does not depend on it.

### Untouched

- `meme.png` (still `f03c8ca1…`), `POST.json`, `main.ts`, `README.md`,
  `LICENSE` untouched. No existing draft file overwritten or edited. No
  commit, push, submit, X post, or recording.

### Status

User's-concept sample draft ready for the user to look at. No evaluation
or submission step taken — parent decides next.

## Entry 2 — "ga sia-sia" concept: the wait paid off twice (SAMPLE ONLY, 2026-11-20 ~00:04 WIB)

### meme-v3-worth-a.png (sha256 `2c24c245…`)

- Concept: the user rejected the ghost-a sample ("biasa bro skip" —
  ordinary) and proposed "ga sia-sia" — the 13-year wait WASN'T in vain,
  because besides enjoying the newly released GTA VI you can also earn
  money from make.fun. Frame is VINDICATION / triumph: a DOUBLE PAYOFF
  (the game + the money). Different engine from ghost-a (morbid — died
  waiting) and from the D time-split (aging). The ghost here is the
  make.fun mascot celebrating the double payoff — NOT a dead gamer.
  Single scene, triumphant.
- Scene: classic make.fun ghost (white sheet, thick black outline, two
  black four-pointed sparkle eyes, BLANK face — no ears, nose, mouth,
  eyebrows, goatee, or hair), DOMINANT and center-frame, arms raised in
  triumph. One hand holds a GTA VI GAME CASE (cover reads "GTA VI" in
  bold letters, plus a large "VI" with palm trees and skyline — the case
  is the payoff prop). The other hand holds a plain canvas MONEY BAG
  (carries a "$" symbol only, NEVER any number or amount). Background:
  Vice City at golden-hour sunset (palm trees, neon "Vice City" sign,
  city skyline, warm light). A few plain gold coins scattered at the
  ghost's feet (no amounts, no numbers on them). Subtle confetti in the
  air, clear of the text.
- Text, all spelled correctly: top `13 YEARS. NOT WASTED.` (white);
  bottom `GOT THE GAME. GOT THE BAG.` (pink); make.fun wordmark
  bottom-right. Both lines fully inside the frame — nothing clipped.
- Originality: "not wasted" / "worth it" framing does not appear in the
  board titles. "GOT THE BAG" is the money punchline instead of "got
  paid" ("The Ghost Got Paid While We Waited" 76.83% owns that phrase).
  No death beat at all — no "became a ghost", "died", "dead", or "came
  back" anywhere.
- Guardrail check: PASS. No phone, no receipt, no wallet screenshot, no
  dollar/USDC amount; money bag carries a "$" symbol only; coins plain.
  The only number in-image is "13" (the joke number). No claim GTA pays
  — the money is make.fun bounty earnings, carried by the wordmark.
- 480px verdict: PASS (`check480/meme-v3-worth-a-480.png`, sha256
  `8d0989de…`). Both main lines fully readable, game case readable as
  GTA VI, money bag readable, ghost unmistakable, wordmark readable,
  coins visible, no text cut off or occluded.
- Defects: none found. Both text lines, both payoff props, and the
  wordmark all read cleanly at full size and at 480px.

### Untouched

- `meme.png` (still `f03c8ca1…`), `POST.json`, `main.ts`, `README.md`,
  `LICENSE` untouched. No existing draft file overwritten or edited. No
  commit, push, submit, X post, or recording.

### Status

"Ga sia-sia" sample draft ready for the user to look at. No evaluation
or submission step taken — parent decides next.

## Worth-B — "ga sia-sia" REBUILD with explicit make.fun line (2026-11-20 ~00:11 WIB)

- File: `drafts/meme-v3-worth-b.png` (1024x1024 PNG, generated at
  1600x1600, downscaled), sha256
  `d59f91ac03e47ec251a28f1da9f010330ace7b018362d779c469fe3646dbfc82`.
- Context: the user APPROVED worth-a ("ini masuk") but said the make.fun
  promotion felt weak. He picked option 3 of the fixes offered: name
  make.fun explicitly in the bottom line. This rebuild changes ONLY the
  bottom line; the scene is reproduced from worth-a.
- Scene: identical to worth-a — classic make.fun ghost (white sheet, thick
  black outline, two black four-pointed sparkle eyes, BLANK face — no ears,
  nose, mouth, eyebrows, goatee, or hair), DOMINANT and center-frame, arms
  raised in triumph. One hand holds a GTA VI GAME CASE (cover reads "GTA
  VI" in bold, plus a large "VI" with palms/skyline); the other holds a
  plain canvas MONEY BAG ("$" symbol only, NEVER any number or amount).
  Background: Vice City at golden-hour sunset (palm trees, neon "Vice
  City" sign, skyline). Plain gold coins scattered at the ghost's feet.
  Subtle confetti, clear of the text.
- Text, all spelled correctly: top `13 YEARS. NOT WASTED.` (white,
  UNCHANGED); bottom `GOT THE GAME. GOT THE BAG FROM MAKE.FUN.` (pink,
  wrapped to two lines: `GOT THE GAME.` / `GOT THE BAG FROM MAKE.FUN.`);
  make.fun wordmark bottom-right. All lines fully inside the frame —
  nothing clipped, no punctuation cut off.
- Originality: "not wasted" / "worth it" framing does not appear in the
  board titles. No "got paid" anywhere ("The Ghost Got Paid While We
  Waited" 76.83% owns that phrase). No death beat at all — no "became a
  ghost", "died", "dead", or "came back" anywhere.
- Guardrail check: PASS. No phone, no receipt, no wallet screenshot, no
  dollar/USDC amount; money bag carries a "$" symbol only; coins plain.
  The only number in-image is "13" (the joke number). No claim GTA pays
  — the money is make.fun bounty earnings, carried by the wordmark and
  the "FROM MAKE.FUN" line.
- 480px verdict: PASS (`check480/meme-v3-worth-b-480.png`, sha256
  `337f8a178eb66784280f9469766381ee6230229417d5d914365914196c0ce937`).
  Both main lines fully readable, game case readable as GTA VI, money
  bag readable, ghost unmistakable, wordmark readable, coins visible,
  no text cut off or occluded.
- Defects: none that affect readability. Minor cosmetic note: the
  wordmark sits tight against the right end of the second bottom line
  (its top edge nearly touches the bottom of "FUN.") — visible at 480px
  as crowding, but no letter is occluded and the period after "FUN." is
  fully visible.

### Untouched

- `meme.png` (still `f03c8ca1…`), `POST.json`, `main.ts`, `README.md`,
  `LICENSE` untouched. No existing draft file overwritten or edited
  (worth-a still `2c24c245…`). No commit, push, submit, X post, or
  recording.

### Status

"Ga sia-sia" rebuild draft ready for the user to look at. No evaluation
or submission step taken — parent decides next.

## Worth-C — "ga sia-sia" REBUILD 2: branded bag + GOT THE USDC (2026-11-20 ~00:13 WIB)

- File: `drafts/meme-v3-worth-c.png` (1024x1024 PNG, generated at
  1600x1600, downscaled), sha256
  `74c15ab474456dad428561817bad5a24bf978fb162e79e856132a2155cad841c`.
- Context: the user approved the worth-b rebuild's direction and asked for
  TWO changes: (1) the money bag the ghost holds should carry the make.fun
  STAR LOGO (small magenta circle with a white star), (2) "GOT THE BAG"
  becomes "GOT THE USDC" so the payment is explicit. This rebuild makes
  ONLY those two changes; the scene is otherwise reproduced from worth-b.
- Scene: identical to worth-b — classic make.fun ghost (white sheet, thick
  black outline, two black four-pointed sparkle eyes, BLANK face — no ears,
  nose, mouth, eyebrows, goatee, or hair), DOMINANT and center-frame, arms
  raised in triumph. One hand holds a GTA VI GAME CASE (cover reads "GTA
  VI" in bold, plus a large "VI" with palms/skyline); the other holds a
  plain canvas MONEY BAG. THE BAG (CHANGED): it carries the make.fun STAR
  LOGO — a MAGENTA/PINK CIRCLE with a WHITE FIVE-POINTED STAR in the
  center, like the make.fun star coin — centered on the bag, clearly
  visible. It REPLACES the "$" symbol (no "$" on the bag). No numbers or
  amounts on the bag. Background: Vice City at golden-hour sunset (palm
  trees, neon "Vice City" sign, skyline). Plain gold coins scattered at
  the ghost's feet. Subtle confetti, clear of the text.
- Text, all spelled correctly: top `13 YEARS. NOT WASTED.` (white,
  UNCHANGED); bottom `GOT THE GAME. GOT THE USDC FROM MAKE.FUN.` (pink,
  wrapped to two lines: `GOT THE GAME.` / `GOT THE USDC FROM MAKE.FUN.`);
  make.fun wordmark bottom-right. All lines fully inside the frame —
  nothing clipped, no punctuation cut off.
- Originality: "not wasted" / "worth it" framing does not appear in the
  board titles. No "got paid" anywhere ("The Ghost Got Paid While We
  Waited" 76.83% owns that phrase) — "GOT THE USDC" is the payment
  punchline instead. No death beat at all — no "became a ghost", "died",
  "dead", or "came back" anywhere.
- Guardrail check: PASS. No phone, no receipt, no wallet screenshot, no
  dollar/USDC amount; "GOT THE USDC FROM MAKE.FUN" names the currency
  only, never an amount (true — make.fun bounties pay in USDC); coins
  plain. The only number in-image is "13" (the joke number). No claim
  GTA pays — the money is make.fun bounty earnings, carried by the
  wordmark, the star-logo bag, and the "FROM MAKE.FUN" line.
- 480px verdict: PASS (`check480/meme-v3-worth-c-480.png`, sha256
  `a0f342943aaee431fb70315020c4d6d2bc298828ac28f94676b0d401ebe116e8`).
  Both main lines fully readable, game case readable as GTA VI, money
  bag + star logo readable (magenta circle with white star clearly
  visible at 480px), ghost unmistakable, wordmark readable, coins
  visible, no text cut off or occluded.
- Defects: none that affect readability. Minor cosmetic note (inherited
  from worth-b, unchanged despite the brief's "if possible" request for
  more room): the wordmark sits tight against the right end of the second
  bottom line (its top edge nearly touches the bottom of "FUN.") —
  visible at 480px as crowding, but no letter is occluded and the period
  after "FUN." is fully visible.

### Untouched

- `meme.png` (still `f03c8ca1…`), `POST.json`, `main.ts`, `README.md`,
  `LICENSE` untouched. No existing draft file overwritten or edited
  (worth-a still `2c24c245…`, worth-b still `d59f91ac…`). No commit,
  push, submit, X post, or recording.

### Status

"Ga sia-sia" rebuild 2 draft ready for the user to look at. No evaluation
or submission step taken — parent decides next.

---

## Draft: meme-v3-peter-a.png — Peter Parker glasses meme, $79.9 → $0 receipt (2026-11-20 ~00:43 WIB)

### Concept
The user's refined Peter Parker glasses concept (PRICE angle). Panel 1:
sticker shock — GTA VI is out and costs $79.9. Panel 2: the realization —
with make.fun it costs $0, shown by the user's own receipt photo. Two-beat
minimal joke ($79.9 → $0), one feeling (relief). The make.fun sell is
direct: make.fun is the reason it's $0.

### Composition (NOT AI-generated scene — assembled from three sources)
- **Peter Parker template stills** — blank template fetched from
  https://cdn.magicmeme.com/templates/peter-parkers-glasses.jpg
  (1400×1399, via the MagicMeme template page; imgflip's top-100 API did
  not list this template). Spider-Man (2002), Tobey Maguire. Top still:
  Peter holding glasses away from his face (blurry/surface view). Bottom
  still: Peter putting glasses on (clear realization). Left column of the
  template, portrait-cropped to 420×512 per panel.
- **User's receipt photo** —
  `~/workspace/user/files/Screenshot_2026-11-20-00-36-40-044_com.brave.browser-edit_0_48e3.jpg`
  (1080×399, original untouched). Reassembled to remove the
  "-$1,000,079.99" line while keeping the ghost logo circle whole: top
  block (x 44–760, y 0–302) + circle bottom (x 87–252, y 302–371,
  original pixels — the dash text starts at x 281, clear of the circle
  which ends at x 252) + pure-cream patch strip for the background.
  Intermediate saved as `drafts/receipt-cropped-peter-a.png` (716×371).
  Keeps: "TOTAL DUE: $0.00" + ghost logo + "PAID IN FULL BY MY AGENT ON
  make.fun". The user wrote the text as "total cost:" but the photo says
  "TOTAL DUE:" — photo used as-is per the brief.
- **GTA VI game case** — cropped from our own generated draft
  `drafts/meme-v3-worth-c.png` (case region x 655–895, y 130–375),
  the ghost's hand holding it kept (reads naturally).

### Layout (1024×1024, two stacked 1024×512 panels, 420/604 column split)
- Panel 1 (top): Peter glasses-OFF left; GTA VI game case right on a dark
  violet cell, with a yellow "$79.9" price-tag sticker overlapping the
  case's top-right corner. Text across the top of the panel, bold white
  with thick black outline (DejaVu Sans Bold 72px):
  `GTA VI OUT NOW. $79.9` — the price EXACTLY as the user wrote it
  (not $79.99, not $100).
- Panel 2 (bottom): Peter glasses-ON left; cropped receipt right on a
  cream cell (receipt cream matched, thin border so it reads as a card).
  No extra text — the receipt carries the punchline. No make.fun wordmark
  added (hard filter already satisfied by the ghost logo + "make.fun" in
  the receipt text; adding it would crowd the panel).
- Thin black dividers between panels and columns.

### Exact in-image text
- `GTA VI OUT NOW. $79.9` (panel 1, overlaid)
- `$79.9` (yellow price tag on the game case)
- `GTA VI` (on the game case)
- `TOTAL DUE: $0.00` (receipt)
- `PAID IN FULL BY MY AGENT ON make.fun` (receipt)
- No "got paid", "became a ghost", "died", "dead", or "came back" anywhere.

### Guardrail check
- Hard filter PASS: make.fun ghost logo + "make.fun" name both in the
  picture (panel 2 receipt).
- The receipt is the JOKE (a $0.00 total due is transparently a gag, not
  a claim of earnings received). No other receipt, amount, wallet
  screenshot, or phone screen added. The -$1,000,079.99 line is ABSENT
  (cropped out, verified by pixel analysis + visual check).
- No amounts invented: $79.9 is the user's price; $0.00 is the receipt's
  own text.

### 480px check: PASS
- File: `drafts/check480/meme-v3-peter-a-480.png`
  (sha256 `3039398a1e64b0640fae2d56b930e4a9400162d2aade54459d0f5d993145475c`).
- Panel 1 text fully readable; "$79.9" readable (text + tag); game case
  readable as GTA VI; Peter recognizable in both panels, glasses-off vs
  glasses-on distinction visible; receipt readable ("$0.00" large and
  clear; "PAID IN FULL BY MY AGENT ON make.fun" legible, smallest text
  in the image but distinct); ghost logo visible; no text cut off or
  occluded; -$1,000,079.99 line absent.

### Defects
- Cosmetic: the panel-1 top text overlaps the top of Peter's hair /
  forehead (standard meme top-text style; his eyes, face, and the
  glasses are fully clear — no letter is occluded and no facial feature
  is covered).
- The receipt's "PAID IN FULL BY MY AGENT ON make.fun" is the smallest
  text in the image at 480px — legible, but the smallest element.
  Inherent to using the user's photo at this scale; the key numbers
  ($79.9, $0.00) are large and dominant.

### Untouched
- `meme.png` (still `f03c8ca1…`), `POST.json`, `main.ts`, `README.md`,
  `LICENSE` untouched. No existing draft file overwritten or edited
  (worth-a still `2c24c245…`, worth-b still `d59f91ac…`, worth-c
  untouched — only read for the case crop). The user's receipt photo
  untouched (crop went to a NEW file). No commit, push, submit, X post,
  or recording.

### Status
Peter Parker $79.9 → $0 receipt draft ready for the user to look at.
No evaluation or submission step taken — parent decides next.

## Draft: meme-v3-peter-b.png — Peter Parker sad→happy, $79.9 → $0 receipt (2026-11-20 ~01:01 WIB)

### Concept
The user's OWN mockup, tidied up ("rapihin"). He replaced the glasses
template with his own two-face Peter: crying Peter (sad at $79.9) →
smiling Peter (happy at $0.00). Same price joke as peter-a, new
protagonist format: the emotion flip IS the joke. Sample only — no
submission, no quota, no X post.

### Composition (NOT AI-generated — pure composition from the user's assets)
- Crying Peter + smiling Peter: cropped from the user's mockup
  `~/workspace/user/files/51937_4_uu00.jpg` (1080x1798). Column divider
  found by pixel analysis at x=552; row divider between the two photos
  at y≈876. First-pass crops cut the mouths at the bottom edge, so both
  were re-cropped lower after visual inspection:
  - Crying: (552, 210, 1080, 738) — eyes + tear + full downturned mouth
    visible.
  - Smiling: (552, 1100, 1080, 1628) — eyes + full grin with teeth
    visible.
  Each resized 528→512 with LANCZOS. The user's mockup file was NOT
  edited.
- GTA VI game case + $79.9 tag: `drafts/gta-vi-case-79.9.png` (604x422,
  the clean crop from peter-a). Fitted to the quadrant width (512),
  centered vertically on the sampled violet background (20,16,38).
  Pixel analysis showed the art spans the full frame, so no tighter
  crop was possible — the symmetric violet bands top/bottom are the
  aspect-ratio slack (1.43:1 art in a square quadrant), not a misfit.
- Ghost logo: cropped from the user's ORIGINAL receipt photo
  `~/workspace/user/files/Screenshot_2026-11-20-00-36-40-044_com.brave.browser-edit_0_48e3.jpg`
  at (80, 199, 259, 378) — the magenta circle (bbox x 88–251, y 207–370
  by pixel analysis) is whole there, while the reassembled
  `receipt-cropped-peter-a.png` clips the circle's bottom edge. The
  user's photo was NOT edited.
- Receipt font: DejaVu Sans Mono Bold
  (/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf) — monospace
  / typewriter style, as the user asked ("pake font receipt gitu").

### Layout (1024x1024, exact 2x2 grid, each quadrant 512x512)
- TOP-LEFT: game case + $79.9 tag, fitted to the quadrant width, tag
  FULLY visible (nothing clipped — fixes the mockup's clipped tag),
  no stray white bars.
- TOP-RIGHT: crying Peter, square-cropped on his face, fills the
  quadrant.
- BOTTOM-LEFT: receipt panel on cream (247,243,232 — sampled from the
  receipt photo), monospace receipt font, centered, vertically balanced:
  "TOTAL COST:" (48px) / "$0.00" (116px) / ghost logo (118px) beside
  "PAID IN FULL BY" / "MY AGENT ON make.fun" (27px — auto-fit to the
  space beside the logo). "TOTAL COST" per the user's wording (NOT
  "TOTAL DUE" — this supersedes the earlier receipt photo's wording).
  The "ONmake.fun" missing space in his mockup was fixed to "ON
  make.fun".
- BOTTOM-RIGHT: smiling Peter, square-cropped on his face, fills the
  quadrant.
- 4px black cross dividers on the quadrant boundaries. NO extra text
  anywhere — no title line, no added captions. The mockup is the spec;
  tidied, not redesigned.

### Exact in-image text
- "$79.9" (yellow tag on the game case)
- "TOTAL COST:"
- "$0.00"
- "PAID IN FULL BY"
- "MY AGENT ON make.fun"

### Guardrail check
- Hard filter PASS: make.fun ghost logo + "make.fun" name both in the
  picture (bottom-left receipt panel).
- No "got paid", "became a ghost", "died", "dead", or "came back"
  anywhere.
- No -$1,000,079.99 line, no other amount, receipt, wallet screenshot,
  or phone screen. The $0.00 receipt is the joke.
- No amounts invented: $79.9 is the user's price; $0.00 is the
  receipt's own figure.

### 480px check: PASS
- File: `drafts/check480/meme-v3-peter-b-480.png`
  (sha256 `9da37a495d11da9e5a67afacd5bdd64ae308f85eb7600f7549c65759ceb514aa`).
- Game case readable as GTA VI; "$79.9" tag fully visible and readable;
  crying vs smiling Peter clearly distinguishable (tear + downturned
  mouth vs big grin); "TOTAL COST: $0.00" large and readable; "PAID IN
  FULL BY MY AGENT ON make.fun" legible; ghost logo visible; no text
  cut off, clipped, or occluded; quadrants aligned, no stray bars.

### Defects
- Cosmetic, inherited: the white blob at the bottom-right of the game
  case (the ghost's hand from the worth-c crop) is still visible — it
  comes from the source crop, not from this composition.
- The "PAID IN FULL BY MY AGENT ON make.fun" lines are the smallest
  text at 480px (~13px) — legible, but the smallest element. The key
  numbers ($79.9, $0.00) are large and dominant.
- Both Peter crops cut the chin slightly at the bottom edge (a 528px
  square cannot hold the full face) — eyes, nose, and mouth are fully
  in frame in both, so the expressions read completely.

### Untouched
- `meme.png` (still `f03c8ca1…`), `POST.json`, `main.ts`, `README.md`,
  `LICENSE` untouched. No existing draft file overwritten or edited
  (peter-a, worth-a/b/c, the game-case crop, and the receipt crop were
  only read). The user's mockup and receipt photo untouched (crops went
  to new files / in-memory only). No commit, push, submit, X post, or
  recording.

### Status
Peter Parker sad→happy $79.9 → $0 receipt draft ready for the user to
look at. No evaluation or submission step taken — parent decides next.

## meme-v3-peter-c.png (parent fix of peter-b, 01:0x WIB 20 Nov)
- Concept: same as peter-b (user's sad→happy mockup, tidied). FIX: peter-b's
  game case filled only ~72% of the top-left quadrant width (measured sunset
  bbox 367x326 of 512x512) — the user explicitly asked for it FITTED to the
  panel. Parent tight-cropped the case source (gta-vi-case-79.9.png → crop
  (105,0,565,405), saved as drafts/gta-vi-case-tight.png, 460x405), scaled it
  to the full 512px quadrant width (512x451), centered vertically on the violet
  background, pasted into a copy of peter-b, and redrew the 4px black cross
  dividers.
- File: drafts/meme-v3-peter-c.png, 1024x1024, sha256
  57e2f95022ecc80fcc185babdbbba6466c324cd3ca0ce5bb84527c6ffdec0261.
  480px check: drafts/check480/meme-v3-peter-c-480.png, sha256
  0714548d59b3775a712cf866687e6b67782505557354c4dfda9b710c0beb1aef.
- 480px verdict (parent-verified): PASS — game case readable as GTA VI, $79.9
  tag fully visible and readable, crying vs smiling clearly distinguishable,
  TOTAL COST: $0.00 large and readable, PAID IN FULL BY MY AGENT ON make.fun
  legible, ghost logo visible, no text cut off or occluded.
- Defects (cosmetic, inherited): white blob at bottom-right of the game case
  (ghost's hand from the worth-c crop); PAID IN FULL lines are the smallest
  text at 480px (legible); both Peter crops cut the chin slightly (eyes, nose,
  mouth fully in frame, expressions read completely).
- Sources: peter-b composition (draft session) + parent's tight-fit fix above.
  Entry-1 files untouched.

## meme-v3-peter-d.png (parent fix of peter-c, 01:0x WIB 20 Nov)
- User feedback on peter-c: the ghost logo (magenta circle) was not clear
  enough. FIX: enlarged the logo from ~100px to 150px in the bottom-left
  receipt panel (re-cropped from the original receipt photo at (80,199,259,378)
  — 179x179 source, so 150px render loses no detail; intermediate saved as
  drafts/ghost-logo-150.png). Rebuilt the panel's bottom block: cream fill,
  logo at (25,833), text re-rendered in DejaVu Sans Mono Bold 26px at x=195,
  vertically centered on the logo. Top of the panel (TOTAL COST: / $0.00) and
  the other three quadrants are pixel-identical to peter-c.
- File: drafts/meme-v3-peter-d.png, 1024x1024, sha256
  112c4228b2c3513b636dc7432b2e7851defa199845d9956864bec457b8db77c3.
  480px check: drafts/check480/meme-v3-peter-d-480.png, sha256
  fdbedefb809b03d66e6c68f82c41a7d008b9952cba0080592e558e5ca31a6cb4.
- 480px verdict (parent-verified): PASS — logo now ~70px at 480px, ghost +
  gem + magenta circle recognizable; all text readable; game case + $79.9 tag
  clear; crying vs smiling distinguishable; no text cut off or occluded.
- Defects (cosmetic, inherited): white blob at bottom-right of the game case
  (ghost's hand from the worth-c crop); PAID IN FULL lines are the smallest
  text at 480px (legible); "MY AGENT ON make.fun" ends 2px from the center
  divider (tight but not touching); Peter chins slightly cut (expressions
  fully readable).
- Entry-1 files untouched.

## meme-v3-peter-e.png (parent fix of peter-d, 01:1x WIB 20 Nov)
- User feedback on peter-d: "make.fun nya mepet banget" — the "make.fun" text
  ended 2px from the center divider. FIX: re-rendered the two PAID IN FULL
  lines in DejaVu Sans Mono Bold 24px (was 26px) at the same x=195; "MY AGENT
  ON make.fun" now ends at x=484, leaving a 26px margin to the divider. Logo
  stays 150px; everything else pixel-identical to peter-d.
- File: drafts/meme-v3-peter-e.png, 1024x1024, sha256
  4162cb21b324be8b5e8a5b8ebacb9aa98d519b4f0de518a6008784b150ae4d11.
  480px check: drafts/check480/meme-v3-peter-e-480.png, sha256
  5dd1406cb49adfbc3b70ebc996917297e70a1d31356f45e8729ffacb3a106d00.
- 480px verdict (parent-verified): PASS — all text readable with clear
  margins, logo recognizable, game case + $79.9 tag clear, crying vs smiling
  distinguishable, no text cut off or occluded.
- Defects (cosmetic, inherited): white blob at bottom-right of the game case
  (ghost's hand from the worth-c crop); PAID IN FULL lines are the smallest
  text at 480px (legible); Peter chins slightly cut (expressions fully
  readable).
- Entry-1 files untouched.
