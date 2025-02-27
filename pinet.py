import os
import customtkinter as ctk
from tkinter import messagebox

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PiNet")
        self.geometry("1280x720")
        self.resizable(True, True)
        ctk.set_appearance_mode('dark')
        ctk.set_widget_scaling(1.0)
        self.center_window(1280, 720)
        #self.create_widgets()
    
    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width/2) - (width/2))
        y = int((screen_height/2) - (height/2))
        self.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == '__main__':
    app = App()
    app.mainloop()