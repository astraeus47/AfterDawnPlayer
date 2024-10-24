from src.ui_elements import *

app_width = 620 # window width
app_height = 300 # window height

audio_extensions = (".mp3", ".wav", ".flac", ".ogg", ".aac", ".wma", ".m4a", ".aiff")
playlist = []
playlist_path = []


class MainFrame(ctk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width = width, height = height, fg_color = '#232323')

        # Configure the grid for MainFrame layout.
        self.grid_columnconfigure(0, weight  = 1)
        self.grid_rowconfigure(0, weight = 1)

        self.app_title()
        self.control_buttons()
        self.music_list()
        self.app_title()

    def add_music(self): # precisa ser terminado, modificado para adionar a musica no scrollable frame.
        try:
            folder = filedialog.askdirectory(title = "Select your music folder.")
            files = os.listdir(folder)

            for music in files:
                if music.lower().endswith(audio_extensions):
                    if os.path.join(folder, music) in playlist:
                        print("this song was just added.")
                        return
                    else:
                        playlist.insert(tk.END, os.path.basename(music))
                        playlist_path.append(os.path.join(folder, music))

        except Exception as error:
            print(error)

    def control_buttons(self):
        # Configure Control Buttons.
        width = app_width - 40
        height = 30
        fg_color = '#0078ff'

        # Control Buttons frame.
        self.buttons_frame = DrawFrame(self, width= width, height = height, fg_color = fg_color)
        self.buttons_frame.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'nsew')

        # Add music button.
        self.add_music_btn = DrawButton(self.buttons_frame, text = "Add Music", command = self.add_music)
        self.add_music_btn.grid(row = 0, column = 0, sticky = 'nsew')

    def music_list(self):
        # Configure Music List.
        width = app_width - 40
        height = 100
        fg_color = '#3d3d3d'

        # Music list, scrollable frame.
        self.music_list_frame = DrawScrollableFrame(self, width = width, height = height, fg_color = fg_color)
        self.music_list_frame.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nsew')

    def app_title(self):
        # Configure Title:
        text = "After Dawn Music Player"
        width = app_width
        height = 20
        fg_color = '#8300ff'
        corner_radius = 0
        text_fg_color = 'transparent'
        font = ('Impact', 30)

        # Title frame.
        self.title_frame = DrawFrame(self, width = width, height = height, fg_color = fg_color, corner_radius = corner_radius)
        self.title_frame.grid(row = 0, column = 0, sticky = 'nsew')

        # Title text label.
        self.title_label = DrawLabel(
            self.title_frame,
            text = text,
            width = width,
            height = height,
            fg_color = text_fg_color,
            font = font
            )
        self.title_label.grid(row = 0, column = 0)

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
                        #playlist.insert(tk.END, os.path.basename(music))
                        playlist_path.append(os.path.join(folder, music))
                        print(playlist_path)

            self.update_music_list()

        except Exception as error:
            print(error)


    def update_music_list(self):
        # Detroy other widgets.
        for widget in self.music_list_frame.winfo_children():
            widget.destroy()

        # Configure Music List.
        width = app_width - 40
        height = 100
        fg_color = '#3d3d3d'

        # Music list, scrollable frame.
        self.music_list_frame = DrawScrollableFrame(self, width = width, height = height, fg_color = fg_color, command = self.button_events, music_list = playlist_path)
        self.music_list_frame.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nsew')

    def button_events(self):
        # Print select music.
        print(f"playing this music: {self.music_list_frame.get_checked_item()}")

    def button_events(self):
        print(f"radiobutton frame modified: {self.music_list_frame.get_checked_item()}")
        music_name = self.music_list_frame.get_checked_item()
        if music_name in playlist_path:
            index = playlist_path.index(music_name)
            # return self.music_path[index]
            mixer.music.load(playlist_path[index])
            mixer.music.play()

class MusicPlayer(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(" After Dawn Music Player")
        self.geometry(f'{app_width}x{app_height}')
        self.resizable(False, False)

<<<<<<< HEAD
    # Set music volume.
    def set_volume(self, volume):
        set_volume = int(volume) / 100

    # Remove all music.
    def remove_all(self):
        mixer.music.stop()
        playlist.clear()
        self.update_music_list()
        print("playlist cleaned successfully!")

        # Initialize mixer from Pygame.
=======
        # Configure the grid for main layout of window.
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
<<<<<<< HEAD
=======

        # Main frame to group all frames.
        self.main_frame = MainFrame(self, width = app_width, height = app_height)
        self.main_frame.grid(row = 0, column = 0, sticky = "nsew")

if __name__ == '__main__':
    app = MusicPlayer()
>>>>>>> parent of 93539e2 (fixed)
    app.mainloop()