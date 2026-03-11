import os
import sys
import subprocess
import json

def transcribe_with_whisperx(file_path, output_dir=None, language="es", model="base"):
    if output_dir is None:
        output_dir = os.path.dirname(file_path)
    
    # Ensure absolute paths
    file_path = os.path.abspath(file_path)
    output_dir = os.path.abspath(output_dir)
    
    # Virtualenv paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    venv_bin_whisperx = os.path.join(script_dir, "venv", "bin", "whisperx")
    
    # WhisperX command
    device = "cpu"
    compute_type = "int8"
    
    cmd = [
        venv_bin_whisperx,
        file_path,
        "--model", model,
        "--language", language,
        "--output_dir", output_dir,
        "--device", device,
        "--compute_type", compute_type,
        "--output_format", "txt"
    ]
    
    print(f"Executing: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error during transcription: {result.stderr}")
        return False
    
    print(colored_text(f"Success! Transcription saved to {output_dir}", "green"))
    return True

def colored_text(text, color):
    colors = {"green": "\033[92m", "red": "\033[91m", "end": "\033[0m"}
    return f"{colors.get(color, '')}{text}{colors.get('end', '')}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python whisperx_tool.py <file_path> [output_dir] [language]")
        sys.exit(1)
    
    path = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    lang = sys.argv[3] if len(sys.argv) > 3 else "es"
    
    transcribe_with_whisperx(path, out, lang)
