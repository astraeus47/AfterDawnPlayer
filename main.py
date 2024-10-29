from src.ui_elements import *
from src.top_levels import *
from src.functions import *
from src.settings import *

# pyinstaller command.
# pyinstaller --noconfirm --onedir --windowed --add-data "C:\Development\Python\Python312\Lib\site-packages/customtkinter;customtkinter/"  "<Path to Python Script>"

from pygame import mixer
from PIL import Image


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
        height = 46
        corner_radius = 0

        # Title frame.
        self.title_frame = DrawFrame(self, width = width, height = height, fg_color = purple_one)
        self.title_frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.bg_image = ctk.CTkImage(light_image = Image.open(bg_img_path), dark_image = Image.open(bg_img_path), size = (app_width, height))

        # self.bg_img_label = ctk.CTkLabel(self.title_frame, image = self.bg_image, text = "")
        # self.bg_img_label.grid(row = 0, column = 0, sticky = 'nsew')

        # Title text label.
        self.title_label = DrawLabel(
            self.title_frame,
            text = text,
            width = width,
            height = height,
            fg_color = text_fg_color,
            font = title_font,
            image = self.bg_image
            )
        self.title_label.grid(row = 0, column = 0, pady = 2)


    def control_buttons(self):
        # Configure Control Buttons.
        width = app_width - 40
        height = 42

        # Control Buttons frame.
        self.buttons_frame = DrawFrame(self, width= width, height = height, fg_color = grey_one)
        self.buttons_frame.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'new')

        # X position calc.
        width_btn = 10
        y_btn = 7
        x_add_btn = 8
        x_return_btn = x_add_btn + (width_btn * 5) - x_add_btn
        x_pause_unpause_btn = x_return_btn + (width_btn * 5) - x_add_btn
        x_next_btn = x_pause_unpause_btn + (width_btn * 5) - x_add_btn
        x_remove_btn = x_next_btn + (width_btn * 5) - x_add_btn

        # Button
        self.add_icon = ctk.CTkImage(light_image = Image.open(add_icon_path), dark_image = Image.open(add_icon_path), size = (20, 20))
        self.play_icon = ctk.CTkImage(light_image = Image.open(play_icon_path), dark_image = Image.open(play_icon_path), size = (20, 20))
        self.pause_icon = ctk.CTkImage(light_image = Image.open(pause_icon_path), dark_image = Image.open(pause_icon_path), size = (20, 20))
        self.next_icon = ctk.CTkImage(light_image = Image.open(next_icon_path), dark_image = Image.open(next_icon_path), size = (20, 20))
        self.return_icon = ctk.CTkImage(light_image = Image.open(return_icon_path), dark_image = Image.open(return_icon_path), size = (20, 20))
        self.remove_icon = ctk.CTkImage(light_image = Image.open(remove_icon_path), dark_image = Image.open(remove_icon_path), size = (20, 20))

        # Add music button.
        self.add_music_btn = DrawButton(
            self.buttons_frame,
            width = width_btn,
            text = "",
            font = button_font,
            fg_color = purple_one,
            hover_color = hover_button,
            image = self.add_icon,
            command = self.add_music
            )
        self.add_music_btn.place(x = x_add_btn, y = y_btn)

        # Back song.
        self.return_music_btn = DrawButton(
            self.buttons_frame,
            width = width_btn,
            text = "",
            fg_color = purple_one,
            hover_color = hover_button,
            image = self.return_icon,
            command = self.play_return_music
            )
        self.return_music_btn.place(x = x_return_btn, y = y_btn)

        # Unpause and unpause music button.
        self.pause_and_unpause = DrawButton(
            self.buttons_frame,
            width = width_btn,
            text = "",
            fg_color = purple_one,
            hover_color = hover_button,
            image = self.play_icon,
            command = self.pause_music
            )
        self.pause_and_unpause.place(x = x_pause_unpause_btn, y = y_btn)

        # Next song.
        self.next_music_btn = DrawButton(
            self.buttons_frame,
            width = width_btn,
            text = "",
            fg_color = purple_one,
            hover_color = hover_button,
            image = self.next_icon,
            command = self.play_next_music
            )
        self.next_music_btn.place(x = x_next_btn, y = y_btn)

        # Remove all music button.
        self.remove_all_btn = DrawButton(
            self.buttons_frame,
            width = width_btn,
            text = "",
            font = button_font,
            fg_color = purple_one,
            hover_color = hover_button,
            image = self.remove_icon,
            command = self.remove_all
            )
        self.remove_all_btn.place(x = x_remove_btn, y = y_btn)

        # Music volume slider.
        self.volume_slider = ctk.CTkSlider(
            self.buttons_frame,
            from_= 0,
            to = 100,
            progress_color = blue_one,
            button_color = purple_one,
            button_hover_color = hover_button,
            orientation = 'horizontal',
            command = self.set_volume
            )
        self.volume_slider.set(50)
        self.volume_slider.place(x = 400, y = 12)


    def music_list(self):
        # Configure Music List.
        width = app_width - 40
        height = 80

        # Music list, scrollable frame.
        self.music_list_frame = DrawScrollableFrame(self, width = width, height = height, fg_color = grey_one, label_anchor = 's', command = self.play_checked_music, music_list = playlist)
        self.music_list_frame.grid(row = 2, column = 0, padx = 5, pady = (0, 5), sticky = 'nsew')


    def add_music(self):
        loaded = load_music_files()
        if loaded == True:
            self.music_list()


    # Based on the checked item, music is played.
    def play_checked_music(self):
        music_name = self.music_list_frame.get_checked_item()
        if music_name in playlist:
            index = playlist.index(music_name)
            self.play_music(index)


    def play_next_music(self):
        try:
            index = self.get_music_positon
            self.play_music(index)
        except:
            print("no songs in playlist")


    def play_return_music(self):
        try:
            index = self.get_music_positon - 2
            self.play_music(index)
        except:
            print("no songs in playlist")


    # Play music.
    def play_music(self, index):
        # change the button icon.
        self.pause_and_unpause.configure(image = self.pause_icon, command = self.pause_music)

        self.get_music_positon = index + 1

        music_name = playlist[index]
        print(f"playing this song: {music_name}")

        self.music_list_frame.set_checked_item(index)

        mixer.music.load(playlist[index])
        mixer.music.play()


    # Pause current music.
    def pause_music(self):
        mixer.music.pause()
        self.pause_and_unpause.configure(image = self.play_icon, command = self.unpause_music)


    # Unpause current music.
    def unpause_music(self):
        mixer.music.unpause()
        self.pause_and_unpause.configure(image = self.pause_icon, command = self.pause_music)


    # Set music volume.
    def set_volume(self, volume):
        music_volume = int(volume) / 100
        mixer.music.set_volume(music_volume)


    # Remove all music.
    def remove_all(self):
        mixer.music.stop()
        playlist.clear()
        self.music_list()
        self.pause_and_unpause.configure(image = self.play_icon, command = self.unpause_music)
        print("playlist cleaned successfully!")


    def music_progress_bar(self):
        self.progress_bar = DrawProgressBar(self, orientation = 'horizontal')
        self.progress_bar.grid(row = 3, column = 0)


    # def get_music_length(self):
    #     filename = self.music_list_frame.get_checked_item()
    #     self.audio_lenght = check_audio_lenght(filename)


if __name__ == '__main__':
    app = MusicPlayer()
    app.mainloop()