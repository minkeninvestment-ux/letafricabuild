# Minken Livestock Wealth — Antler Kenya Pitch

**Stage:** Proposed venture concept. **Format:** Approximately one-minute narrated animated pitch. **Presenter:** Synthetic voiceover with graphics, not a live video of Hukun Dabar.

### Pitch focus

- Livestock owners need easier connections to qualified veterinarians and market participants.
- Proposed product: a mobile-first service marketplace for veterinary access, buyer discovery and herd-support information.
- First milestone: customer interviews and prototype testing in Kenya.
- Antler goal: validate customer needs, build a focused product, and develop a repeatable model.

### Video file

The GitHub Actions workflow [Build Antler Livestock Pitch Video](../../.github/workflows/antler-video.yml) runs `build_video.py`, publishes the generated MP4 as an Actions artifact, and attempts to commit `minken_antler_livestock_pitch.mp4` to this directory. Check [Actions](https://github.com/minkeninvestment-ux/letafricabuild/actions) for status.

**Antler personal-introduction note:** A personal founder video should ideally feature Hukun speaking on camera about his background and this idea. Do not describe the synthetic narration here as his own recorded voice or personal video.

### Rebuild locally

Requires `python3`, `Pillow`, `espeak`, `ffmpeg`, `ffprobe`, and DejaVu fonts.

```bash
python antler/livestock-wealth/build_video.py
```

Minken Investment Ltd (Minken Africa), Nairobi, Kenya.
