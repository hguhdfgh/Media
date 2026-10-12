# Ishak AI: asset prompts for v2 ("Cashback 6000$")

> **للـ Agent (Flow):** ولّد الصور هادو كامل، صورة بصورة، بنفس الستايل بالضبط. كل صورة تكون وحدها (ملف واحد لكل رقم). سمّي كل ملف بالاسم المكتوب (مثلاً `01_coin.png`).
>
> **علاش الخلفية Magenta ماشي Green screen؟** لأن البراند تاعنا أخضر (#2EF59A). إذا الخلفية خضراء، الـ key ينحّي الأخضر تاع الأشياء معاها. الماجنتا (#FF00FF) ما كايناش في الباليت، نقدر ننحيها نقية.

---

## MASTER PROMPT (copy this whole block to the agent once)

```
You will generate a set of 14 separate images for a premium tech brand called "Ishak AI".
Generate them ONE BY ONE, in order, one image per item, and keep the EXACT same visual style across all of them so they look like one 3D asset pack.

=== SHARED STYLE (apply to every image unless the item says otherwise) ===
- Premium photoreal 3D product render, Octane/Redshift look, ultra clean, sharp, high detail.
- Materials: dark smoked glass (almost black with a green tint, #030504 base), polished emerald-green glass (#2EF59A), and brushed silver-white metal like chrome with soft reflections.
- Lighting: soft studio key light from the top-left, strong mint-green rim light (#2EF59A) outlining the edges, small lime highlights (#C6FF3D) on bevels and edges only.
- Edges: beveled, rounded corners, thin glowing mint outline on the edges (like a neon edge inside the glass), same as a glossy emblem logo with a white-silver half and an emerald-green half.
- Mood: calm confidence, luxury fintech, trustworthy. Never cartoonish, never toy-like, never cheap.
- Colour palette ONLY: near-black, emerald/mint green, lime accent, silver-white. NO blue, NO cyan, NO red, NO gold, NO purple, NO rainbow.
- Background: a perfectly flat, solid, uniform pure magenta #FF00FF chroma-key background, no gradient, no texture, no floor, no reflections on the floor, no shadow cast on the background, no glow spilling onto the background, crisp clean silhouette edges.
- Composition: single object, centered, fully visible with generous margin (object fills about 70% of the frame), 3/4 hero angle slightly from below, square 1:1, 2048x2048.
- ABSOLUTELY NO text, NO letters, NO numbers, NO watermark, NO signature, NO logos unless the item explicitly asks for one.

=== IMAGES ===

01_coin.png
A single thick 3D coin made of emerald-green glass with a polished silver rim, a raised embossed dollar symbol "$" in the center made of silver-white metal (this "$" symbol is the only allowed glyph), mint rim light, slightly tilted toward the camera.

02_coin_stack.png
A neat tall stack of 7 identical coins from image 01 (emerald glass with silver rims and embossed silver "$"), slightly offset stack, one coin on top tilted and floating above the stack.

03_cashback_loop.png
A 3D circular arrow loop (two curved arrows chasing each other forming a circle, like a refresh/refund icon) made of emerald glass with silver metal arrow heads, with a small emerald glass coin with an embossed silver "$" floating in the middle of the loop.

04_shield.png
A 3D protective shield emblem, thick beveled shape, the left half made of brushed silver-white metal and the right half made of emerald-green glass (split vertically down the middle), with a bold lime-green check mark embossed in the center, mint glowing outline on the edges.

05_card.png
A premium payment card floating at a dynamic 3D angle, made of dark smoked black glass with a subtle green tint, a silver EMV chip, a contactless wave symbol, a thin holographic mint-to-lime edge glow, a soft diagonal light sheen across the surface. NO brand logo, NO numbers, NO text on the card.

06_clock_24h.png
A 3D round stopwatch / timer made of dark smoked glass with a silver-white metal frame and crown button, the dial ring filled with a glowing lime progress arc covering almost the whole circle, minimalist dial with no numbers.

07_headset.png
A 3D customer-support headset with a microphone boom, the headband and ear cups made of brushed silver-white metal and emerald glass cushions, mint rim light.

08_briefcase.png
A 3D business briefcase made of dark smoked glass with silver-white metal handle and corners, a small emerald glass verified badge with a lime check mark attached on its front.

09_calendar_year.png
A 3D desk calendar block made of dark smoked glass with silver rings on top, the front page is a clean emerald glass panel with a large glowing lime check mark (no numbers, no text).

10_paper_plane.png
A 3D paper plane (direct message / send icon) made of emerald glass with silver-white edges, flying diagonally up-right with a short soft mint light trail behind it.

11_ads_dashboard.png
A floating 3D smartphone with thin silver-white frame, screen shows an abstract minimalist dark advertising dashboard: one rising lime line chart, three emerald bar columns, two rounded rectangle cards, a toggle switch, all abstract shapes only, absolutely no readable text or numbers. Phone tilted at a 3/4 angle.

12_coin_burst.png
An explosion of 20 to 30 emerald glass coins with silver rims and embossed "$" flying outward from the center in all directions toward the camera, with motion blur on the outer coins and small lime sparkles, empty center.

13_bg_plate.png  (DIFFERENT BACKGROUND RULE FOR THIS ONE)
A full-bleed vertical background plate, 9:16, 1080x1920 (or 2160x3840): deep near-black environment (#030504) with a subtle green tint, two large soft mint-green (#2EF59A) light blooms (one top-left, one bottom-right), a faint glowing perspective floor grid in mint at the bottom third fading into darkness, light atmospheric haze, very subtle film grain. No objects, no text. NO magenta for this one.

14_light_streaks.png  (DIFFERENT BACKGROUND RULE FOR THIS ONE)
A full-bleed vertical 9:16 image on a PURE BLACK #000000 background (not magenta): several elegant diagonal light streaks and soft lens flares in mint green and lime, anamorphic, like a premium light leak overlay. Nothing else. (This will be used with a screen blend mode.)

=== OPTIONAL (only if your tool allows brand logos) ===

15_tiktok_glass.png
The TikTok music-note logo shape re-imagined as a 3D object made of emerald glass and silver-white metal (no cyan, no red, only the brand palette), mint rim light, on the same flat magenta #FF00FF background.

16_visa_card.png
Same card as image 05, but with the word "VISA" in clean white italic letters in the top-right corner of the card.

=== FINAL CHECK FOR EVERY IMAGE ===
Same lighting direction, same materials, same palette, same camera height, flat magenta background (except 13 and 14), no text (except 16), nothing cropped at the frame edges.
```

---

## Where each image goes in the video

| # | File | Scene (time) | Use |
|---|---|---|---|
| 01 | `01_coin.png` | Hook 0–3s | Coin flips in behind the `$6,000` counter |
| 02 | `02_coin_stack.png` | S3 8.5–15s | Replaces the "you get back" bar (the stack grows) |
| 03 | `03_cashback_loop.png` | S2 7.7s "كاش باك" | Icon on the Cashback chip / card |
| 04 | `04_shield.png` | S5 21.5s "الضمان" | Replaces the SVG shield |
| 05 | `05_card.png` | S4 16.1s "كارد فيزا" | Replaces the CSS card (more realistic) |
| 06 | `06_clock_24h.png` | S4 18.2s "24 ساعة" | Behind the 24h ring |
| 07 | `07_headset.png` | S5 20.2s "متابعة" | Pill icon |
| 08 | `08_briefcase.png` | S2 4.1s "حسابات" | Account card icon |
| 09 | `09_calendar_year.png` | S5 23.2s "سنة كاملة" | Next to the 12-month counter |
| 10 | `10_paper_plane.png` | CTA 26.3s "ابعثلنا فالخاص" | Flies into the IG button |
| 11 | `11_ads_dashboard.png` | S2 3.3s "وفرت لكم" | Phone behind the account card |
| 12 | `12_coin_burst.png` | S3 14.9s "100% CASHBACK" | Burst behind the stamp |
| 13 | `13_bg_plate.png` | S3 + CTA | Background for the full-motion scene |
| 14 | `14_light_streaks.png` | Transitions | Light leak (screen blend) |
| 15–16 | optional | S1 / S4 | Only if you want the real logos (TikTok ads review may reject official third-party logos) |

**How to send them back:** drop all the PNGs into one folder (or a zip) and send them. I'll remove the magenta (chroma key + despill), then rebuild v2 at exactly the same timings without changing anything else.
