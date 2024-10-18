from src.ui_elements import *

app_width = 720 # window width
app_height = 400 # window height

class MainFrame(ctk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width = width, height = height, fg_color = '#5d5d5d')

        #  Configure the grid for MainFrame layout.
        self.grid_columnconfigure(1, weight  = 1)
        self.grid_rowconfigure(1, weight = 1)

        self.draw_title()
        self.draw_buttons()
        self.draw_play_list()

    def draw_play_list(self):
        self.play_list_frame = DrawScrollableFrame(self, width = 600, height = 100, command = self.radio_btn_event,
                                                   item_list = [f"item {i}" for i in range(100)]
                                                   )
        self.play_list_frame.grid(row = 1, column = 0, padx = 10, pady = 0, sticky = "nsew")

    def radio_btn_event(self):
        print(f"radiobutton frame modified: {self.play_list_frame.get_checked_item()}")
    
    def draw_buttons(self):
        self.buttons_frame = DrawFrame(self, width = 100, height = 40, fg_color = '#008bff')
        self.buttons_frame.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "nsew")

    def draw_title(self):
        self.title = DrawFrame(self, width = 700, height = 40, fg_color = '#008bff')
        self.title.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nsew")

        self.title_text = DrawText(self.title, text = "Music Player", fg_color = "transparent", font = ('Arial', 20))
        self.title_text.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")

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

if __name__ == '__main__':
    app = MusicPlayer()
    app.mainloop()