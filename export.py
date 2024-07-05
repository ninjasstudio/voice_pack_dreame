from pathlib import Path
from subprocess import run
from typing import Dict

import yaml

from main import data_dir, load_csv

output_dir = Path("output\\")

tmpfile = output_dir / "tmp.mp3"

with open("choices.yaml") as f:
    choices: Dict[int, int] = yaml.safe_load(f)

files = []

for id, text in load_csv().items():
    file_dir = data_dir / str(id)
    if id in choices:
        chosen_num = choices[id]
    else:
        chosen_num = 0
    chosen_file = file_dir /"output.mp3"
    output_file = output_dir / f"{id}.ogg"
    run([
        "ffmpeg",
        "-i", str(chosen_file),
        "-filter:a", "loudnorm=I=-14:LRA=1:dual_mono=true:tp=-1",
        str(tmpfile)
    ])
 
    run([
        "ffmpeg",
        "-i", str(tmpfile),
        "-c:a", "libvorbis",
        "-b:a", "100k",
        "-ar", "16000",
        str(output_file)
    ])

    tmpfile.unlink()
    files.append(output_file.name)
    run(["7z", "a", "-ttar", "archive.tar", output_file.name], cwd="output\\")
filelist=[*files]
print (f"7z a --tar archive.tar "+" output\\".join(filelist))

run([
    "7z", "a", "-tgzip", "../voice_pack.tar.gz", "archive.tar"
], cwd="output\\")