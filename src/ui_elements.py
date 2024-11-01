import customtkinter as ctk
import os
from src.settings import *


class DrawFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class DrawScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, music_list, command = None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.radio_button_var = ctk.StringVar()
        self.radio_button_list = []

        for i, item in enumerate(music_list):
            music_name = os.path.basename(item)
            music_path = item
            self.add_item(music_name, music_path)
    
    def add_item(self, music_name, music_path):
        # Configure Radio Button.
        hover = True

        self.item_frame = DrawFrame(
            self,
            width = 584,
            height = 40,
            fg_color = item_list,
            corner_radius = 2
            )
        self.item_frame.grid(row = len(self.radio_button_list), column = 0, pady = 1, sticky = 'nsew')

        radio_button = DrawRadioButton(
            self.item_frame,
            text = music_name,
            hover = hover,
            hover_color = hover_color,
            border_color = '#ffffff',
            fg_color = '#ffffff',
            text_color = '#ffffff',
            value = music_path,
            variable = self.radio_button_var
            )

        if self.command is not None:
            radio_button.configure(command = self.command)
        radio_button.grid(row = len(self.radio_button_list), column = 0, padx = 10, pady = 10)
        
        self.radio_button_list.append(radio_button)

    def get_checked_item(self):
        return self.radio_button_var.get()
    
    def set_checked_item(self, index):
        self.radio_button_list[index].select()


class DrawRadioButton(ctk.CTkRadioButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class DrawButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class DrawLabel(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class DrawProgressBar(ctk.CTkProgressBar):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
