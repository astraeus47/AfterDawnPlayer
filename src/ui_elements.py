import customtkinter as ctk
from pygame import mixer
from tkinter import filedialog
import tkinter as tk
import os

class DrawButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class DrawScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class DrawLabel(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class DrawFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_propagate(False) # on the frame will make it maintain the specified size, ignoring the size of the content.
