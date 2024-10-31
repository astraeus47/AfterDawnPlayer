from src.settings import audio_extensions, playlist
from tkinter import filedialog
from pygame import mixer
import os, random

# Imports to music files.
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.ogg import OggFileType
from mutagen.mp4 import MP4
import wave
import contextlib


def load_music_files():
    try:
        folder = filedialog.askdirectory(title = "Select your music folder.")
        files = os.listdir(folder)

        for music in files:
            if music.lower().endswith(audio_extensions):

                if os.path.join(folder, music) in playlist:
                    print("this song was just added.")
                    return

                else:
                    playlist.append(os.path.join(folder, music))
                
        print("all songs have been added.")
        return True

    except Exception as error:
        print(error)

def check_audio_lenght(music_name):
    extension = os.path.splitext(music_name)[1].lower()

    try:
        if extension == ".mp3":
            audio = MP3(music_name)
            return audio.info.length

        elif extension == ".flac":
            audio = FLAC(music_name)
            return audio.info.length

        elif extension == ".ogg":
            audio = OggFileType(music_name)
            return audio.info.length

        elif extension in (".m4a", ".aac"):
            audio = MP4(music_name)
            return audio.info.length

        elif extension == ".wav":
            with contextlib.closing(wave.open(music_name, 'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                return frames / float(rate)

        else:
            raise ValueError(f"Unsupported file type: {extension}")

    except Exception as e:
        print(f"Error getting length for {music_name}: {e}")
        return None
    
# def music_progress(self, get_lenght):
#     if mixer.music.get_busy():
#         current_time = mixer.music.get_pos() / 1000
#         progress = (current_time / get_lenght) * 100
#         print(f"Progress: {progress:.2f}%")
#         self.after(1000, lambda: self.music_progress(get_lenght))