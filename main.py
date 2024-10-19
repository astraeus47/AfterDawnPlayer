from src.ui_elements import *
from src.functions import *

app_width = 720 # window width
app_height = 400 # window height


class MainFrame(ctk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width = width, height = height, fg_color = '#5d5d5d')

        #  Configure the grid for MainFrame layout.
        self.grid_columnconfigure(1, weight  = 1)
        self.grid_rowconfigure(1, weight = 1)

        # List of music files and path of music files.
        self.music_list, self.music_path = load_music_list()

        self.draw_buttons()
        self.draw_play_list()
        self.draw_title()

    def draw_buttons(self):
        self.buttons_frame = DrawFrame(self, width = 100, height = 40, fg_color = '#008bff')
        self.buttons_frame.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "nsew")

        self.play_btn = DrawButton(self.buttons_frame, text = "Play")
        self.play_btn.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")

    def draw_play_list(self):
        self.play_list_frame = DrawScrollableFrame(self, width = 600, height = 100, command = self.radio_btn_event, item_list = self.music_list)
        self.play_list_frame.grid(row = 1, column = 0, padx = 10, pady = 0, sticky = "nsew")

    def draw_title(self):
        self.title = DrawFrame(self, width = 700, height = 40, fg_color = '#008bff')
        self.title.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nsew")

        self.title_text = DrawText(self.title, text = "Music Player", fg_color = "transparent", font = ('Arial', 20))
        self.title_text.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")

    # Button events.
    def radio_btn_event(self):
        print(f"radiobutton frame modified: {self.play_list_frame.get_checked_item()}")
        music_name = self.play_list_frame.get_checked_item()
        if music_name in self.music_list:
            index = self.music_list.index(music_name)
            # return self.music_path[index]
            mixer.music.load(self.music_path[index])
            mixer.music.play()


class MusicPlayer(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry(f'{app_width}x{app_height}')
        self.resizable(False, False)

        # Configure the grid for main layout of window.
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        width = app_width
        height = app_height

        # Main frame to group all frames.
        self.main_frame = MainFrame(self, width, height)
        self.main_frame.grid(row = 0, column = 0, sticky = "nsew")

        # Start the Pygame sound system.
        mixer.init()


if __name__ == '__main__':
    app = MusicPlayer()
    app.mainloop()