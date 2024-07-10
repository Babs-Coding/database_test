#Imports
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess


#GUI Window

Main = Tk()


class App(Tk):
    def __init__(self):
        super().__init()
        self.title("Life Family")
        self.geometry("800x800")
        
        
        self.mainloop()


Frame1 = Canvas(Main)
Frame1.pack(fill = "both", expand = True)

Frame1.create_image( 0, 0, image = bg, anchor = "nw")

#my_label= Label(Frame1, image=bg)
#my_label.place(x=0, y=0, relwidth=1, relheight=1)

#my_canvas = Canvas(, width=800, height=800)
#my_canvas.pack(fill="both", expand=True) 

def Life_Directory() :
    import GUI
    subprocess.call(GUI)                   

def EDC():
    import GUI_copy


Member_information = Button(Frame1, width = 20, height=2, text=" Life Directory", command = Life_Directory)
Member_information.grid(row=1, column=1, padx= 140, pady= 100, sticky="n")

Reporting_button = Button(Frame1, width = 20, height=2, text="Reporting & Analytics")
Reporting_button.grid(row=1, column=2, padx= 20, pady= 100, sticky="ew")

Finance_button = Button(Frame1, width = 20, height=2, text="Finance")
Finance_button.grid(row=2, column=1, padx= 20, pady= 30, sticky="n")

Life_button = Button(Frame1, width = 20, height=2, text="Life EDC's", command= EDC)
Life_button.grid(row=2, column=2, padx= 20, pady= 30, sticky="ew")

soul_button = Button(Frame1, width = 20, height=2, text="SOULS Admin", anchor=CENTER)
soul_button.grid(row=3, column= 1,columnspan=2,padx=0, pady=90 , sticky="n")



