import tkinter
import tkinter  as tk
from tkinter import W, ttk
from tkinter import messagebox
from tkinter import *
from tkcalendar import DateEntry
import customtkinter as ck
from CTkTable import *
class App(ck.CTk):
    def __init__(self): 
        super().__init__()
        self.title("Life Family")
        self.geometry("800x800")
        self.Menu = Menu(self)
        self.Main = Main(self)
        self.mainloop() 
        
        container = ck.CTkFrame(self)
        container.place(relx=0.2, y=0, relwidth = 0.8, relheight = 1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (Home,Life_Directory, Reporting_Analytics, Finance, Life_EDC, SOULS_Admin):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        #frame.winfo_toplevel().overrideredirect(1)  #pentru teste se comenteaza
        frame.winfo_toplevel().geometry("800x800")
        
        
        container = ck.CTkFrame(self)
        container.place(relx=0.2, y=0, relwidth = 0.8, relheight = 1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
    
        
        
        
        
        
class Menu(ck.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        
        # Setting Menu Dimensions
        self.place(relx=0, y=0, relwidth = 0.2, relheight = 1) 
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Menu Buttons
        self.Member_information = ck.CTkButton(self, width = 20, height=2, text="Life Directory")
        self.Reporting_button = ck.CTkButton(self, width = 20, height=2, text="Reporting & Analytics")
        self.Finance_button = ck.CTkButton(self, width = 20, height=2, text="Finance")
        self.Life_button = ck.CTkButton(self, width = 20, height=2, text="Life EDC's")
        self.soul_button = ck.CTkButton(self, width = 20, height=2, text="SOULS Admin", anchor=CENTER)
        
        #Buttons Layout
        self.Member_information.grid(row=0, column=0,sticky="nsew")
        self.Reporting_button.grid(row=1, column=0, sticky="nsew")
        self.Finance_button.grid(row=2, column=0, sticky="nsew")
        self.Life_button.grid(row=3, column=0, sticky="nsew")
        self.soul_button.grid(row=4, column= 0, sticky="nsew")
        

class Main(ck.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        
        
        
        
        
        
class Home(ck.CTkFrame):
    def __init__(self, parent, controller):
        ck.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page")
        label.pack(side="top", fill="x", pady=10)
    
        self.Splash_Label = ck.CTkLabel(self)
        self.Splash_Label.place(relx=0.2, y=0, relwidth = 0.8, relheight = 1)
        
class Life_Directory(ck.CTkFrame):
    def __init__(self, parent, controller):
        ck.CTkFrame.__init__(self, parent)
    

class Reporting_Analytics(ck.CTkFrame):
    def __init__(self, parent, controller):
        ck.CTkFrame.__init__(self, parent)
        
        
class Finance(ck.CTkFrame):
    def __init__(self, parent, controller):
        ck.CTkFrame.__init__(self, parent)
        
        
        
class Life_EDC (ck.CTkFrame):
    def __init__(self, parent, controller):
        ck.CTkFrame.__init__(self, parent)

class SOULS_Admin (ck.CTkFrame): 
    def __init__(self, parent, controller):
        ck.CTkFrame.__init__(self, parent)   




App()