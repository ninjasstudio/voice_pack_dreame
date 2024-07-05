import hashlib
from pathlib import Path
from time import sleep
from typing import Dict

import yaml

from elevenlabs_api import ElevenLabsAPI

data_dir = Path(".\\data\\")

replacements = {
    "3D": "Three-Dee"
}

def replace_text(text: str) -> str:
    for find, replace in replacements.items():
        text = text.replace(find, replace)
    return text

class DB:
    def __init__(self):
        self.done_hashes = {}

    @classmethod
    def load(cls, file: Path):
        with file.open() as f:
            db = cls()
            db.__dict__ = yaml.safe_load(f)
            return db

    def save(self, file: Path):
        with file.open("w") as f:
            yaml.safe_dump(self.__dict__, f)

def load_csv() -> Dict[int, str]:
    data = {}
    with open("sound_list.csv") as f:
        for line in f:
            filename, text = line.replace('"', "").strip().split(",", maxsplit=1)
            id = int(filename.split(".")[0])
            data[id] = text
    return data

def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    db_file = Path("db.yaml")
    # Replace 'your_api_key_here' with your actual Eleven Labs API key
    api = ElevenLabsAPI(api_key="", voice_id="wiB0qsyacAiijGDUmghU")
    if db_file.exists():
        db = DB.load(db_file)
    else:
        db = DB()

    for id, text in load_csv().items():
        text = replace_text(text)
        hash = hash_text(text)
        if id in {-1, 201}:
            # don't load startup and shutdown sound
            continue
        file_dir = data_dir / str(id)
        if not file_dir.exists():
            file_dir.mkdir(parents=True)
        if id in db.done_hashes:
            if db.done_hashes[id] == hash:
                continue
            else:
                print(f"{id} changed, regenerating")
                for file in file_dir.glob("*"):
                    file.unlink()

        print("starting download")
        api.tts_to_wav(file_dir, text)
        db.done_hashes[id] = hash
        db.save(db_file)
        sleep(3)

    db.save(db_file)
