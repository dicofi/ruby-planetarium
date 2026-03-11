---
name: whisperx-transcriber
description: Transcribe audio files using WhisperX for high accuracy and alignment. Use this skill whenever the user says "transcribir", "transcribe", or asks for a transcription of an audio/video file. It handles Spanish by default and uses the ruby-planetarium whisperX installation.
---

# 🎙️ WhisperX Transcriber

This skill automates the transcription of audio files using the WhisperX repository installed in `playground/ruby-planetarium`.

## Primary Usage

When a user asks to transcribe a file:
1. Locate the file (usually in `Downloads` or `Documents`).
2. Use the `whisperx_tool.py` script located in `/Users/diegocorrales/.gemini/antigravity/playground/ruby-planetarium/`.

## Execution Protocol

Run the following command structure:
```bash
/Users/diegocorrales/.gemini/antigravity/playground/ruby-planetarium/venv/bin/python /Users/diegocorrales/.gemini/antigravity/playground/ruby-planetarium/whisperx_tool.py [path_to_audio] [output_directory] [language]
```

## Supported Languages
- Default: `es` (Spanish)
- Can be overridden if the user specifies another language.

## Dependencies
- Requires `ffmpeg` (already installed via brew).
- Uses `python@3.13` and a dedicated `venv` in the `ruby-planetarium` directory.
