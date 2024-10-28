from src.settings import audio_extensions, playlist
from tkinter import filedialog
import os

# Imports to music files.
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.ogg import OggFileType
from mutagen.mp4 import MP4
import wave
import contextlib

def check_audio_lenght(filename):
    extension = os.path.splitext(filename)[1].lower()

    try:
        if extension == ".mp3":
            audio = MP3(filename)
            return audio.info.length

        elif extension == ".flac":
            audio = FLAC(filename)
            return audio.info.length

        elif extension == ".ogg":
            audio = OggFileType(filename)
            return audio.info.length

        elif extension in (".m4a", ".aac"):
            audio = MP4(filename)
            return audio.info.length

        elif extension == ".wav":
            with contextlib.closing(wave.open(filename, 'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                return frames / float(rate)

        else:
            raise ValueError(f"Unsupported file type: {extension}")

    except Exception as e:
        print(f"Error getting length for {filename}: {e}")
        return None
    
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