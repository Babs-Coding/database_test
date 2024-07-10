import customtkinter as ck
from PIL import Image
from PIL import *
from tkinter import *
import PIL as PIL
import os
class Login_Window(ck.CTk):
    def __init__(self, *args, **kwargs):
        ck.CTk.__init__(self, *args, **kwargs)
       

        width = 500
        height = 500
        
        x= (self.winfo_screenwidth()//2)-(width//2)
        y= (self.winfo_screenheight()//2)-(height//2)
        self.geometry("{}x{}+{}+{}".format(width, height, x, y))
       
        container = ck.CTkFrame(self)
        container.place(relx=0, y=0, relwidth = 1, relheight = 1) 
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.Heading_Font = ("Arial", 35, "bold")
        self.Text_Font= ("Arial", 12, "bold")

        self.title("Login")
        self.overrideredirect(True)

        self.frames = {}
        for F in (Login_Prompt, Sucessful_Login):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login_Prompt")
          

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        frame.winfo_toplevel().geometry("500x500")


        


class Login_Prompt(ck.CTkFrame):
    def __init__(self, parent, controller):
        ck.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.parent= parent
        self.Heading_Font = ("Arial", 35, "bold")
        self.Text_Font= ("Arial", 12, "bold")
        #self.configure(fg_color="#000000")

        Login_Image=PhotoImage(file="3dcopy.png")
        Login_IMG= ck.CTkLabel(self, image = Login_Image)
        Login_IMG.place(x=0, relwidth=1, relheight=1)
        
        def login():
            usernames = ["Femi Sowemimo", "Sylvia Otieno"]
            Passwords = ["Soniran17!", "NxtionFamily"]
            username = Username_Entry.get()
            password = Password_Entry.get()

            for x in usernames:
                for y in Passwords:
                    if username in x and password in y:
                        self.controller.show_frame("Sucessful_Login")
                
            else:
                self.parent.Info_Label.configure(text="Incorrect Username or Password")

        Login_Label = ck.CTkLabel(self, text="Login", font=self.Heading_Font, text_color="#FFFFFF", fg_color="transparent")
        Login_Label.place(x=200, y=130)#
        
        Username_Label = ck.CTkLabel(self, text="Username: ",text_color="#FFFFFF", font= self.Text_Font)
        Username_Label.place( x=110, y=200)
        Username_Entry = ck.CTkEntry(self,placeholder_text="Please Enter a Username ",width=170)
        Username_Entry.place( x=190, y=200)

        Password_Label = ck.CTkLabel(self, text="Password: ", text_color="#FFFFFF", font= self.Text_Font)
        Password_Label.place(x=112, y=250)
        Password_Entry = ck.CTkEntry(self,placeholder_text="Please Enter a Password ", width=170)
        Password_Entry.place( x=190, y=250)

        self.parent.Login_Button = ck.CTkButton(self, text="Login ", font= self.Text_Font, width= 125, command= login)
        self.parent.Login_Button.place(x= 235, y=310)
        self.FP_Button = ck.CTkButton(self, text="Forgot Password?", font= self.Text_Font, width= 125)
        self.FP_Button.place(x= 106, y=310)
        
        self.parent.Info_Label = ck.CTkLabel(self, text="", font= self.Text_Font, width= 125) 
        self.parent.Info_Label.place(x=170, y=350)




class Sucessful_Login(ck.CTkFrame):
    def __init__(self, parent, controller):
        ck.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.parent = parent 
        self.after(3000,)

        self.configure(fg_color="#000000")

        Login_Image=PhotoImage(file="loading.gif")
        Login_IMG= ck.CTkLabel(self, image = Login_Image)
        Login_IMG.pack

        Loading_Image="loading.gif"
        openImage = PIL.Image.open(Loading_Image) 
        frames = openImage.n_frames
        imageObject = [PhotoImage(file=Loading_Image, format=f"gif -index {i}") for i in range(frames)]
        count=0
        showAnimation = None

        def animation(count):
            global showAnimation
            newImage = imageObject[count]

            LoadingLabel.configure(image = newImage)
            count +=1

            if count == frames:
                count = 0

            showAnimation = self.after(50, lambda: animation(count))
        
        
        LoadingLabel= ck.CTkLabel(self, image="", width=450, height=500)
        LoadingLabel.place(x=7, y=10, )
        animation(count)


        

app = Login_Window()
app.mainloop()                             