import customtkinter
import tkinter
from CTkTable import *

class App(customtkinter.CTk):
    def __init__(Life):
        super().__init__()

        # configure window
        Life.title("CustomTkinter complex_example.py")
        Life.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        Life.grid_columnconfigure(1, weight=1)
        Life.grid_columnconfigure((2, 3), weight=0)
        Life.grid_rowconfigure((0, 1, 2), weight=1)
        
        Life.Tabview = customtkinter.CTkTabview(Life, width=200)
        Life.Tabview.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        Life.Tabview.grid_rowconfigure(5, weight=1)
        Life.Tabview.add("tab 1")  # add tab at the end
        Life.Tabview.add("tab 2")  # add tab at the end
        Life.Tabview.add("tab 3")
        Life.Tabview.set("tab 2")  # set currently visible tab
        
        Life.sidebar_frame = customtkinter.CTkFrame(Life, width=350, corner_radius=1)
        Life.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        Life.sidebar_frame.grid_rowconfigure(3, weight=1)
        Life.sidebar_frame.grid_columnconfigure(3, weight = 0)
        Life.Tabview = customtkinter.CTkTabview(Life, width=200)
        Life.Tabview.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        Life.Tabview.grid_rowconfigure(5, weight=1)
        
        Life.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
                                                        command=self.open_input_dialog_event)
        
        Life.button = customtkinter.CTkButton(Life.Tabview.tab("tab 1"))
        Life.button.pack(padx=20, pady=20)
        Life.Menubutton = customtkinter.CTkButton(Life.sidebar_frame, height= 80, text="Home")
        Life.Menubutton.grid( row=0, column=0)
        
        Life.second_frame= customtkinter.CTkFrame()
        
        def Lifebutton():
            second_frame = second_ui_class()
            second_frame.show()
            
        
        
        Life.Menubutton2 = customtkinter.CTkButton(Life.sidebar_frame, height= 80, text="Life", command=Lifebutton)
        Life.Menubutton2.grid( row=1, column=0)
        Life.Menubutton3 = customtkinter.CTkButton(Life.sidebar_frame, height= 80, text="Finance")
        Life.Menubutton3.grid( row=2, column=0)
        
        
        Life.Menubutton4 = customtkinter.CTkButton(Life.sidebar_frame, height= 80, text="Finance")
        Life.Menubutton4.grid( row=3, column=0)
        
        
        
        Life.Database = customtkinter.CTkTable(Life, width=200)
        Life.Database.pack()
        App.mainloop()