# Ruby Planetarium - Audio Transcriber

Antigravity Project for high-accuracy audio transcription using **WhisperX**.

## Setup

This project uses **WhisperX** as a git submodule to ensure it can stay updated with the latest improvements from the upstream repository.

### Initializing Submodules
If you just cloned this repo, run:
```bash
git submodule update --init --recursive
```

### Keeping WhisperX Updated
To update the WhisperX component to the latest version available in its official repository:
```bash
git submodule update --remote --merge
```

## Usage

This project includes a dedicated **Skill** for the Antigravity ecosystem. 

1. **Skill Name**: `whisperx-transcriber`
2. **Trigger**: "transcribir", "transcribe"
3. **Execution**: Automated via `whisperx_tool.py`.

### Manual Transcription
```bash
./venv/bin/python whisperx_tool.py <audio_file> <output_dir> <language>
```

## Structure
- `whisperX/`: Git Submodule (Upstream)
- `.agent/skills/`: Transcription skill definition
- `whisperx_tool.py`: Wrapper for CLI execution
- `venv/`: Local python environment (ignored by git)
