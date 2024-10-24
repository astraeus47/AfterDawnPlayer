import customtkinter as ctk
from pygame import mixer
from tkinter import filedialog
import tkinter as tk
import os

<<<<<<< HEAD
=======

>>>>>>> parent of fc01d3d (version-1.20)
class DrawButton(ctk.CTkButton):
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
<<<<<<< HEAD
        radio_button = ctk.CTkRadioButton(self, text = music_name, value = music_path, variable = self.radio_button_var)
=======
        # Configure Radio Button.
        hover = True
        hover_color = '#00ff5d'

        radio_button = ctk.CTkRadioButton(self, text = music_name, hover = hover, hover_color = hover_color, value = music_path, variable = self.radio_button_var)
>>>>>>> parent of fc01d3d (version-1.20)

        if self.command is not None:
            radio_button.configure(command = self.command)
        radio_button.grid(row = len(self.radio_button_list), column = 0, pady = 10)
        
        self.radio_button_list.append(radio_button)

    def get_checked_item(self):
        return self.radio_button_var.get()

<<<<<<< HEAD
=======

>>>>>>> parent of fc01d3d (version-1.20)
class DrawLabel(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

<<<<<<< HEAD
=======

>>>>>>> parent of fc01d3d (version-1.20)
class DrawFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_propagate(False) # on the frame will make it maintain the specified size, ignoring the size of the content.
<<<<<<< HEAD
=======


>>>>>>> parent of fc01d3d (version-1.20)
