# Ishak AI: Cashback 6000$ (v1)

- **Export:** `export/ishak-ai_cashback-6000_v1.mp4` (1080x1920, 30fps, 28.9s, H.264 + AAC)
- **Composition:** `hf/index.html` (one HTML page renders every frame: footage + green grade + motion + captions)
- **Cue sheet:** `work/plan.json` · word timings: `work/transcript.json`
- **v2 images:** `prompts/asset-prompts.md` (master prompt for the Flow agent)

## Rebuild
```bash
# 1) footage frames (source talking head, not committed)
ffmpeg -i SOURCE.mp4 -vf "scale=1080:1920:flags=lanczos,unsharp=5:5:0.6" -q:v 2 hf/vf/%04d.jpg
# 2) frames (813 video + 54 end-card hold)
node tools/render.mjs "$PWD/hf" "$PWD/frames" 867 4
# 3) sfx + mux
python3 tools/sfx.py hf/sfx.wav
tools/mux.sh frames SOURCE.mp4 hf/sfx.wav export/ishak-ai_cashback-6000_v1.mp4
```
