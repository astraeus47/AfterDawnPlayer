from src.ui_elements import *
from src.settings import *

from pygame import mixer
from tkinter import filedialog
from PIL import Image

# Imports to music files.
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.ogg import OggFileType
from mutagen.mp4 import MP4
import wave
import contextlib

class MusicPlayer(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ 27ᴘʀxʙʟᴍꜱ")
        self.geometry(f'{app_width}x{app_height}')
        self.resizable(False, False)

        # Configure the grid for main layout of window.
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        # Main frame to group all frames.
        self.main_frame = MainFrame(self, width = app_width, height = app_height)
        self.main_frame.grid(row = 0, column = 0, sticky = 'nsew')

        # Initialize Pygame mixer.
        mixer.init()


class MainFrame(ctk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width = width, height = height, fg_color = dark_one)

        # Configure the grid for MainFrame layout.
        self.grid_columnconfigure(1, weight  = 1)
        self.grid_rowconfigure(1, weight = 1)

        self.app_title()
        self.control_buttons()
        #self.music_list()
        #self.music_progress_bar()

    def app_title(self):
        # Configure Title:
        text = "After Dawn Music Player"
        width = app_width
        height = 20
        corner_radius = 0

        # Title frame.
        self.title_frame = DrawFrame(self, width = width, height = height, fg_color = purple_one)
        self.title_frame.grid(row = 0, column = 0, sticky = 'nsew')

        # Title text label.
        self.title_label = DrawLabel(
            self.title_frame,
            text = text,
            width = width,
            height = height,
            fg_color = text_fg_color,
            font = title_font
            )
        self.title_label.grid(row = 0, column = 0)


    def control_buttons(self):
        # Configure Control Buttons.
        width = app_width - 40
        height = 50

        # Buttons icons.
        play_icon_path = "musicplayer/icons/play.png"
        pause_icon_path = "musicplayer/icons/pause.png"
        play_icon = ctk.CTkImage(light_image = Image.open(play_icon_path), dark_image = Image.open(play_icon_path), size = (20, 20))
        pause_icon = ctk.CTkImage(light_image = Image.open(pause_icon_path), dark_image = Image.open(pause_icon_path), size = (20, 20))

        # Control Buttons frame.
        self.buttons_frame = DrawFrame(self, width= width, height = height, fg_color = grey_one)
        self.buttons_frame.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nsew')

        # Add music button.
        self.add_music_btn = DrawButton(
            self.buttons_frame,
            text = "Add",
            font = button_font,
            fg_color = purple_one,
            hover_color = hover_button,
            command = self.add_music
            )
        self.add_music_btn.grid(row = 0, column = 0, padx = 5, pady = 5)

        # Unpause music button.
        self.unpause_btn = DrawButton(
            self.buttons_frame,
            width = 10,
            text = "",
            fg_color = purple_one,
            hover_color = hover_button,
            image = play_icon,
            command = self.unpause_music
            )
        self.unpause_btn.grid(row = 0, column = 1, padx = 5, pady = 5)

        # Pause music button.
        self.pause_btn = DrawButton(
            self.buttons_frame,
            width = 10,
            text = "",
            fg_color = purple_one,
            hover_color = hover_button,
            image = pause_icon,
            command = self.pause_music
            )
        self.pause_btn.grid(row = 0, column = 2, padx = 5, pady = 5)

        # Remove all music button.
        self.remove_all_btn = DrawButton(
            self.buttons_frame,
            text = "Remove All",
            font = button_font,
            fg_color = purple_one,
            hover_color = hover_button,
            command = self.remove_all
            )
        self.remove_all_btn.grid(row = 0, column = 3, padx = 5, pady = 5)

        # Music volume slider.
        self.volume_slider = ctk.CTkSlider(
            self.buttons_frame,
            from_= 0,
            to = 100,
            orientation = 'horizontal',
            command = self.set_volume
            )
        self.volume_slider.set(50)
        self.volume_slider.grid(row = 0, column = 4)


    def music_list(self):
        # Configure Music List.
        width = app_width - 40
        height = 80

        # Music list, scrollable frame.
        self.music_list_frame = DrawScrollableFrame(self, width = width, height = height, fg_color = grey_one, label_anchor = 's', command = self.button_events, music_list = playlist)
        self.music_list_frame.grid(row = 2, column = 0, padx = 5, pady = (0, 5), sticky = 'nsew')


    def add_music(self):
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
                        print(playlist)

            self.update_music_list()

        except Exception as error:
            print(error)


    def update_music_list(self):
        # Configure Music List.
        width = app_width - 40
        height = 60
        
        self.music_list()

        # Music list, scrollable frame.
        # self.music_list_frame = DrawScrollableFrame(self, width = width, height = height, fg_color = fg_color, command = self.button_events, music_list = playlist)
        # self.music_list_frame.grid(row = 2, column = 0, padx = 5, pady = 5)

    # Based on the checked item, music is played.
    def button_events(self):
        print(f"radiobutton frame modified: {self.music_list_frame.get_checked_item()}")
        music_name = self.music_list_frame.get_checked_item()
        if music_name in playlist:
            index = playlist.index(music_name)
            mixer.music.load(playlist[index])
            mixer.music.play()

    # Pause current music.
    def pause_music(self):
        mixer.music.pause()

    # Unpause current music.
    def unpause_music(self):
        mixer.music.unpause()

    # Set music volume.
    def set_volume(self, volume):
        music_volume = int(volume) / 100
        mixer.music.set_volume(music_volume)

    # Remove all music.
    def remove_all(self):
        mixer.music.stop()
        playlist.clear()
        self.update_music_list()
        print("playlist cleaned successfully!")

    def music_progress_bar(self):
        self.progress_bar = DrawProgressBar(self, orientation = 'horizontal')
        self.progress_bar.grid(row = 3, column = 0)

    def get_music_length(self):
        filename = self.music_list_frame.get_checked_item()
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


if __name__ == '__main__':
    app = MusicPlayer()
    app.mainloop()