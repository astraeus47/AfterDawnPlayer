import os
from pygame import mixer
from tkinter import filedialog
import tkinter as tk

def load_music_list():
    music_list = []
    music_path = []
    music_file = filedialog.askopenfilename(
        defaultextension=".mp3",  # Definindo o .mp3 como padrão
        filetypes=[
            ("Audio files", "*.mp3 *.wav *.ogg *.flac *.aac *.m4a"),
            ("MP3 files", "*.mp3"),
            ("WAV files", "*.wav"),
            ("OGG files", "*.ogg"),
            ("FLAC files", "*.flac"),
            ("AAC files", "*.aac"),
            ("M4A files", "*.m4a"),
            # ("All files", "*.*")
        ]
    )

    if music_file:
        music_list.append(os.path.basename(music_file))
        music_path.append(music_file)
    
    return music_list, music_path