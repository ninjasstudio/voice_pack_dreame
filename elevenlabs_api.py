"""

APIKEy=
"""
from pathlib import Path
from typing import TypedDict, List, Union

import requests
from requests import Session
import os
import uuid
from elevenlabs import Model, VoiceSettings
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = ""

client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)
class Response(TypedDict):
    audio_url: str


class ElevenLabsAPI:
    tts_url = "https://api.elevenlabs.io/v1/text-to-speech"
    max_text_len = 500

    def __init__(self, api_key: str, voice_id: str):
        self.api_key = api_key
        self.voice_id = voice_id
        self.s = Session()
        self.s.headers.update({
        "xi-api-key": "",
        "Content-Type": "application/json"
        })

    def get_tts(self, text: str, dir: Path) -> Response:
        assert len(text) <= self.max_text_len
        response = client.text_to_speech.convert(
                voice_id="wiB0qsyacAiijGDUmghU",
                optimize_streaming_latency="0",
                output_format="mp3_22050_32",
                text=text,
                voice_settings=VoiceSettings(
                    stability=0.55,
                    similarity_boost=0.75,
                    use_speaker_boost=True,
                ),
            )
        
        save_file_path = dir / 'output.mp3'
        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)
        print(f"{save_file_path}: A new audio file was saved successfully!")
                        

    def tts_to_wav(self, dir: Path, text: str) -> None:
        data = self.get_tts(text, dir)
        
       


if __name__ == '__main__':
    # Replace 'your_api_key_here' with your actual Eleven Labs API key
    api = ElevenLabsAPI(api_key="APIKEy=", voice_id="wiB0qsyacAiijGDUmghU")
    print(api.get_tts("This is an example!"))
