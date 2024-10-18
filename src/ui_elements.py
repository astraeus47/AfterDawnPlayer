import customtkinter as ctk

# This class was created to make scrollable frames.
class DrawScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, item_list, command = None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.radio_btn_var = ctk.StringVar()
        self.radio_btn_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)
    
    def add_item(self, item):
        radio_btn = ctk.CTkRadioButton(self, text = item, value = item, variable = self.radio_btn_var)

        if self.command is not None:
            radio_btn.configure(command = self.command)
        radio_btn.grid(row = len(self.radio_btn_list), column = 0, pady = (0, 10))
        self.radio_btn_list.append(radio_btn)

    def get_checked_item(self):
        return self.radio_btn_var.get()

# This class was created to make other labels.
class DrawText(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

# This class was created to make other frames.
class DrawFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_propagate(False) # on the frame will make it maintain the specified size, ignoring the size of the content.