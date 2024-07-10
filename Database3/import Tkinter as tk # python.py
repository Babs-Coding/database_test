
import subprocess
import tkinter  as tk
from tkinter import W, ttk
from tkinter import messagebox
from tkinter import *
from tkcalendar import DateEntry
import customtkinter as ck

import sqlite3
import PIL as PIL
import time
import datetime
import os
import random
from math import *
import matplotlib as plt

import csv

TITLE_FONT = ("Helvetica", 18, "bold")


class SampleApp(ck.CTk):

    def __init__(self, *args, **kwargs):
        ck.CTk.__init__(self, *args, **kwargs)

        def flexx( o, r = 0, c = 0, rw = 1, cw = 1 ):
            '''flexx will control grid manager static|dymanic growth'''
            if r != None:
                o.rowconfigure( r, weight = rw )
            if c != None:
                o.columnconfigure( c, weight = cw )

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        Menu = ck.CTkFrame(self, fg_color="black")
        Menu.place(relx=0, y=0, relwidth = 0.15, relheight = 1) 
        Menu.grid_rowconfigure((0,1,2,3,4), weight=1)
        Menu.grid_columnconfigure(0, weight=1)
        flexx(Menu)
    
        #Menu Buttons
        my_font = ck.CTkFont(family="montserrat",weight= "bold", size= 14)
        
        self.Member_information = ck.CTkButton(Menu, width = 20, height=2, text="Life Directory",command=lambda: self.show_frame("LifeDirectory"), font= my_font)
        self.Reporting_button = ck.CTkButton(Menu, width = 20, height=2, text="Dashboard", command=lambda: self.show_frame("Dashboard"), font= my_font)
        self.Finance_button = ck.CTkButton(Menu, width = 20, height=2, text="Finance", command=lambda: self.show_frame("Finance"), font= my_font)
        self.About_button = ck.CTkButton(Menu, width = 20, height=2, text="About",command=lambda: self.show_frame("About"), font= my_font)
        self.Settings_button = ck.CTkButton(Menu, width = 20, height=2, text="Settings", command=lambda: self.show_frame("Settings"), font= my_font)
        
        #Menu Layout
        self.Member_information.grid(row=1,pady= 1, column=0,sticky="nsew")
        self.Reporting_button.grid(row=0,pady= 1, column=0, sticky="nsew")
        self.Finance_button.grid(row=2,pady= 1, column=0, sticky="nsew")
        self.About_button.grid(row=4,pady= 1, column=0, sticky="nsew")
        self.Settings_button.grid(row=3,pady= 1, column= 0, sticky="nsew")
        
        container = ck.CTkFrame(self, fg_color="black")
        container.place(relx=0.15, y=0, relwidth = 0.85, relheight = 1) 
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        flexx(container)

        self.frames = {}
        for F in (StartPage, LifeDirectory, Dashboard, Finance, Settings, About_Page, Modify_Info,ExpenseForm,SeedTracker):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            Frame(bg = "black")
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

        def change_appearance_mode_event(self, new_appearance_mode: str):
            self.ck.set_appearance_mode(new_appearance_mode)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        #frame.winfo_toplevel().overrideredirect(1)  #pentru teste se comenteaza
        frame.winfo_toplevel().geometry("1280x720")

class StartPage(ck.CTkFrame):

    def __init__(self, parent, controller):
        ck.CTkFrame.__init__(self, parent)
        self.controller = controller
        
        self.picture = PhotoImage(file="3d.png")
        self.picture2 = self.picture
        self.label = Label(self, image=self.picture)
        self.label.pack(fill="both", expand = "yes")

class LifeDirectory(ck.CTkFrame):

    def __init__(self, parent, controller):
        ck.CTkFrame.__init__(self, parent)
        
        self.parent = parent
        self.controller = controller
        
        # The code `self.table = CTkTable(master=self, row=5, column=3)` creates an instance of the
        # `CTkTable` class with 5 rows and 3 columns.
        
        self1= ck.CTkFrame(self)
        self1.place(relx=0, y=0,relwidth= 1, relheight = 0.95) 
        self2= ck.CTkFrame(self)
        self2.place(relx=0, y=935,relwidth= 1, relheight = 0.053) 
        self2.grid_rowconfigure(0, weight=1)
        self2.grid_columnconfigure(9, weight=1)
        Search_Frame = ck.CTkEntry(self2,width= 300)
        Search_Frame.grid(row=0, column=0,padx=5,columnspan= 2, sticky="EW")
        Search_button = ck.CTkButton(self2, text="Search")
        Search_button.grid(row=0, column=2)
        Surname_Label= ck.CTkLabel(self2, text="Surname", anchor=E, padx=6)
        Surname_Label.grid(row=0, column=3,padx=3,sticky="EW", ipadx=20)
        Surname_Entry = ck.CTkEntry(self2, width= 200)
        Surname_Entry.grid(row=0, column=4)
        FirstName_Label= ck.CTkLabel(self2, text="First Name", anchor=E, padx=6)
        FirstName_Label.grid(row=0, column=5,padx=3,sticky="EW", ipadx=20)
        FirstName_Entry = ck.CTkEntry(self2, width=200)
        FirstName_Entry.grid(row=0, column=6)
        
        tabview = ck.CTkTabview(self1)
        tabview.place(relx=0, y=2,relwidth= 1, relheight = 1) 
        tabview.add("Core Members")  # add tab at the end
        tabview.add("Life Family")
        tabview.add("EDC's")
        tabview.add("Outreach")# add tab at the end, 
        tabview.set("Core Members")  # set currently visible tab


        
        scrollbar = ttk.Scrollbar(tabview.tab("Core Members"))
        scrollbar.pack(side="right", fill="y")
                 
          
        self.treeview = ttk.Treeview(tabview.tab("Core Members"),
                    selectmode="browse",
                    yscrollcommand=scrollbar.set,
                    columns=(0,1, 2, 3, 4, 5),
                    height=10,)
        self.treeview.pack(expand=True, fill="both")

        self.treeview['columns'] = ("ID","Surname", "First Name", "Gender", "Date Of Birth", "Address")

        # self.treeview columns
        self.treeview.column("#0", anchor="w", width=20)
        self.treeview.column("ID", anchor="n", width=30)
        self.treeview.column("Surname", anchor="n", width=120)
        self.treeview.column("First Name", anchor="n", width=120)
        self.treeview.column("Gender", anchor="n", width=50)
        self.treeview.column("Date Of Birth", anchor="n", width=80)
        self.treeview.column("Address", anchor="n", width=200)

        # self.treeview headings

        self.treeview.heading("#0", text="", anchor="w")
        self.treeview.heading("ID", text="ID", anchor="center")
        self.treeview.heading("Surname", text="Surname", anchor="center")
        self.treeview.heading("First Name", text="First Name ", anchor="center")
        self.treeview.heading("Gender", text="Gender", anchor="center")
        self.treeview.heading("Date Of Birth", text="Date Of Birth", anchor="center")
        self.treeview.heading("Address", text="Address", anchor="center")
        scrollbar.config(command=self.treeview.yview)

        self.treeview.tag_configure('oddrow', background="white")
        self.treeview.tag_configure('evenrow', background="lightblue")


        conn = sqlite3.connect("Database3\Life_Family.db")
        
        table_create_query = '''CREATE TABLE IF NOT EXISTS Life_Family_Members 
(
                            "ID"	INTEGER NOT NULL UNIQUE,
                            "Surname"	TEXT NOT NULL,
                            "First Name"	TEXT NOT NULL,
                            "Gender"	INTEGER NOT NULL,
                            "Date Of Birth"	TEXT NOT NULL,
                            "Address"	TEXT,
                            "Occupation"	TEXT,
                            "Contact Number"	NUMERIC,
                            "Email Address"	TEXT,
                            "Residental Status"	TEXT,
                            "Highest Level of Qualification "	TEXT,
                            "Course Name "	TEXT,
                            "Employment Status"	TEXT,
                            "Employer"	TEXT,
                            "Service Department"	TEXT,
                            PRIMARY KEY("ID" AUTOINCREMENT)
)
                    '''
                    
        conn.execute(table_create_query)
                    
                    

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT * FROM Life_Family_Members")
        records = c.fetchall()

        # Add our data to the screen
        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                self.treeview.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14]), tags=('evenrow',))
            else:
                self.treeview.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14]), tags=('oddrow',))
            # increment counter
            count += 1
        
         

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        class LifeFamily:
            scrollbar1 = ttk.Scrollbar(tabview.tab("Life Family"))
            scrollbar1.pack(side="right", fill="y")

            self.treeview1 = ttk.Treeview(tabview.tab("Life Family"),
                        selectmode="browse",
                        yscrollcommand=scrollbar.set,
                        columns=(0,1, 2, 3, 4, 5),
                        height=10,)
            self.treeview1.pack(expand=True, fill="both")

            # self.treeview columns
            self.treeview1.column("#0", anchor="w", width=20)
            self.treeview1.column(0, anchor="n", width=30)
            self.treeview1.column(1, anchor="n", width=120)
            self.treeview1.column(2, anchor="n", width=120)
            self.treeview1.column(3, anchor="n", width=50)
            self.treeview1.column(4, anchor="n", width=80)
            self.treeview1.column(5, anchor="n", width=200)

            # self.treeview headings

            self.treeview1.heading("#0", text="", anchor="w")
            self.treeview1.heading(0, text="ID", anchor="center")
            self.treeview1.heading(1, text="Surname", anchor="center")
            self.treeview1.heading(2, text="First Name ", anchor="center")
            self.treeview1.heading(3, text="Gender", anchor="center")
            self.treeview1.heading(4, text="Date Of Birth", anchor="center")
            self.treeview1.heading(5, text="Address", anchor="center")
            scrollbar1.config(command=self.treeview.yview)

            self.treeview1.tag_configure('oddrow', background="white")
            self.treeview1.tag_configure('evenrow', background="lightblue")


            conn1 = sqlite3.connect("Database3\Life_Family.db")
            
            table1_create_query = '''CREATE TABLE IF NOT EXISTS Life_Family_Members 
                                (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT, 
                                registration_status TEXT, num_courses INT, num_semesters INT)
                        '''
                        
            conn1.execute(table1_create_query)
                        
                        

            # Create a cursor instance
            c1 = conn1.cursor()

            c1.execute("SELECT rowid, * FROM Life_Family_Members")
            records1 = c1.fetchall()

            # Add our data to the screen
            global count1
            count1 = 0

            for record in records1:
                if count1 % 2 == 0:
                    self.treeview1.insert(parent='', index='end', iid=count1, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
                else:
                    self.treeview1.insert(parent='', index='end', iid=count1, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
                # increment counter
                count1 += 1
            
            # Commit changes
            conn1.commit()

            # Close our connection
            conn1.close()

        class EDC:
            scrollbar2 = ttk.Scrollbar(tabview.tab("EDC's"))
            scrollbar2.pack(side="right", fill="y")

            self.treeview2 = ttk.Treeview(tabview.tab("EDC's"),
                        selectmode="browse",
                        yscrollcommand=scrollbar.set,
                        columns=(0,1, 2, 3, 4, 5),
                        height=10,)
            self.treeview2.pack(expand=True, fill="both")

            # self.treeview columns
            self.treeview2.column("#0", anchor="w", width=20)
            self.treeview2.column(0, anchor="n", width=30)
            self.treeview2.column(1, anchor="n", width=220)
            self.treeview2.column(2, anchor="n", width=220)
            self.treeview2.column(3, anchor="n", width=50)
            self.treeview2.column(4, anchor="n", width=80)
            self.treeview2.column(5, anchor="n", width=200)

            # self.treeview headings

            self.treeview2.heading("#0", text="", anchor="w")
            self.treeview2.heading(0, text="ID", anchor="center")
            self.treeview2.heading(1, text="Name Of Property", anchor="center")
            self.treeview2.heading(2, text=" Address", anchor="center")
            self.treeview2.heading(3, text="Point Of Contact", anchor="center")
            self.treeview2.heading(4, text="Contact Details", anchor="center")
            scrollbar2.config(command=self.treeview2.yview)

            self.treeview2.tag_configure('oddrow', background="white")
            self.treeview2.tag_configure('evenrow', background="lightblue")

            conn2 = sqlite3.connect("Database3\Life_Family.db")
            
            table2_create_query = '''CREATE TABLE IF NOT EXISTS EDCs 
                                (Name_of_Property TEXT, Address TEXT, Postcode TEXT, Point_Of_Contact TEXT, Contact_Number TEXT)
                        '''
                        
            conn2.execute(table2_create_query)
                        
                        
            # Create a cursor instance
            c2 = conn2.cursor()

            c2.execute("SELECT * FROM EDCs")
            records2 = c2.fetchall()

            # Add our data to the screen
            global count2
            count2 = 0

            for record in records2:
                if count2 % 2 == 0:
                    self.treeview2.insert(parent='', index='end', iid=count2, text='', values2=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
                else:
                    self.treeview2.insert(parent='', index='end', iid=count2, text='', values2=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
                # increment counter
                count2 += 1
            
            # Commit changes
            conn2.commit()

            # Close our connection
            conn2.close()

        
            
        
        def SelectRecord(e):

            selected= self.treeview.focus()
            values = self.treeview.item(selected, 'values')
      
            self.parent.first_name_entry.delete(0, END)
            self.parent.first_name_entry.delete(0,END)
            self.parent.last_name_entry.delete(0,END)
            self.parent.dob_entry.delete(0,END)
            self.parent.Address1_field.delete(0,END)
            self.parent.Address2_field.delete(0,END)
            self.parent.Town_field.delete(0,END)
            self.parent.City_field.delete(0,END)
            self.parent.Postcode_field.delete(0,END)
            self.parent.Contact_Number.delete(0,END)
            self.parent.Email_Address_entry.delete(0,END)
            self.parent.Residental_Status_entry.delete(0,END)
            self.parent.Highest_Level_Of_Qualification_entry.delete(0,END)
            self.parent.Course_Name_entry.delete(0,END)
            self.parent.Employment_Status_entry.delete(0,END)
            self.parent.Employer_entry.delete(0,END)
            self.parent.Department_Served_in_entry.delete(0,END)
            self.parent = parent
            self.controller.show_frame("Modify_Info")
            self.parent.first_name_entry.insert(0,values[2])
            self.parent.last_name_entry.insert(0,values[1])
            self.parent.dob_entry.insert(0,values[4])
            self.parent.Address1_field.insert(0,values[5])
            self.parent.Address2_field.insert(0,values[1])
            self.parent.Town_field.insert(0,values[1])
            self.parent.City_field.insert(0,values[1])
            self.parent.Postcode_field.insert(0,values[1])
            self.parent.Occupation_entry.insert(0,values[6])
            self.parent.Contact_Number.insert(0,values[7])
            self.parent.Email_Address_entry.insert(0,values[8])
            self.parent.Residental_Status_entry.insert(0,values[9])
            self.parent.Highest_Level_Of_Qualification_entry.insert(0,values[10])
            self.parent.Course_Name_entry.insert(0,values[11])
            self.parent.Employment_Status_entry.insert(0,values[12])
            self.parent.Employer_entry.insert(0,values[13])
            self.parent.Department_Served_in_entry.insert(0,values[14])
           
            
        self.treeview.bind ("<Double-1>", SelectRecord)  
                   
class Dashboard(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self2= ck.CTkFrame(self, fg_color="white")
        #self2.place(relx=0, y=0.0,relwidth= 1, relheight = 1) 

        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        #label.pack(side="top", fill="x", pady=10)

        #label4.place(x=480, y=5)

        
        conn = sqlite3.connect("Database3\Life_Family.db")
    
        c = conn.cursor()

        c.execute("select strftime('%d/%m/%Y',datetime(substr(Date, 7, 4) || '-' || substr(Date, 4, 2) || '-' || substr(Date, 1, 2))) from Expenses;")

        c.execute("SELECT SUM FROM Expenses where DATE >= DATE('now','-7 Days')")

        Expense_Week=c.fetchone()[0]

        conn.commit()

        # Close our connection
        conn.close()

        
        conn = sqlite3.connect("Database3\Life_Family.db")
    
        c = conn.cursor()

        c.execute("SELECT SUM(Expense_Amount) FROM Expenses where DATE = DATE('now','-1 Days')")
        Expense_Month=c.fetchone()[0]

        conn.commit()

        # Close our connection
        conn.close()



        nx = 41 ; ny = 10                                      # canvas size
        Income_Totalweek = tk.Label(self, text = " Income This Week: ", anchor="n", font=(TITLE_FONT, 9, "bold"), fg= "white", pady= 3, height=ny, bg = "teal", relief="raised", highlightbackground="#F5F5F5")  # create canvas w
        Income_Totalweek.place(relx=0.012,rely=0.025, relwidth= 0.23, relheight=0.1575)                                     # make canvas visible

        Exp_Total = tk.Label(self,text= "Expenditure This Week: " + "\n\n\n" + "£" + str(Expense_Week), anchor="n", font=(TITLE_FONT,9, "bold"),pady=3, fg="white", height=ny, bg = "turquoise2", relief="raised", highlightbackground="#F5F5F5")  # create canvas w
        Exp_Total.place(relx=0.2589,rely=0.025,relwidth= 0.23,relheight=0.1575)  
                 # make canvas visible

        Income_TotalMonth = tk.Label(self, text= " Income This Month: ", anchor="n", font=(TITLE_FONT,9, "bold"),pady=3, fg="white", height=ny, bg = "orange", relief="raised", highlightbackground="#F5F5F5")  # create canvas w
        Income_TotalMonth.place(relx=0.5061,rely=0.025, relwidth= 0.23,relheight=0.1575)  

        Exp_TotalMonth = tk.Label(self, text= "Expenditure This Month: " + "\n\n\n" + "£" + str(Expense_Month) ,anchor="n", font=(TITLE_FONT,9, "bold"),pady=3, fg="white",height=ny, bg = "#FF6103", relief="raised", highlightbackground="#F5F5F5")  # create canvas w
        Exp_TotalMonth.place(relx=0.758, rely=0.025, relwidth= 0.23,relheight=0.1575) 



        Graph = ck.CTkCanvas(self, height= 350, bg = "white", relief="raised", highlightbackground="#FFFAFA", highlightthickness=4)
        Graph.place(relx=0.012,rely=0.2075,relwidth= 0.7244, relheight=0.37) 

        Graph2 = ck.CTkCanvas(self, height= 350, bg = "white", relief="raised", highlightbackground="#FFFAFA", highlightthickness=4)
        Graph2.place(relx=0.758,rely=0.2075, relwidth=0.23, relheight=0.37) 

        Graph4 = ck.CTkCanvas(self, width=625, height= 390, bg = "white", relief="raised", highlightbackground="#FFFAFA", highlightthickness=4)
        Graph4.place(relx=0.758,rely=0.6025, relwidth=0.23, relheight=0.37) 

        Graph5 = ck.CTkCanvas(self, width=290, height= 390, bg = "white", relief="raised", highlightbackground="#FFFAFA", highlightthickness=4)
        Graph5.place(relx=0.012,rely=0.6025,relwidth=0.23,relheight=0.37)

        Graph6 = ck.CTkCanvas(self, width=290, height= 390, bg = "white", relief="raised", highlightbackground="#FFFAFA", highlightthickness=4)
        Graph6.place(relx=0.2589,rely=0.6025, relwidth= 0.4772,relheight=0.37) 
        
                                           # make canvas visible


class Finance(tk.Frame):   # Parametrii AC

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Button_Font = font=("Times", 30,"bold")

        parent.Expense_Form_Button  = ck.CTkButton(self, text="Expense Form", font= Button_Font, width=1100, height=400, command=lambda:self.controller.show_frame("ExpenseForm"))
        parent.Expense_Form_Button.place(relx=0.020, y=25,relwidth= 0.45, relheight=0.45)

        parent.Seed_Tracker_App = ck.CTkButton(self,text="Seed Tracker", font= Button_Font, width=1150, height=400, command=lambda:self.controller.show_frame("SeedTracker"))
        parent.Seed_Tracker_App.place(relx=0.53, y=25,relwidth=0.45, relheight=0.45)

       
class Settings(tk.Frame):   # Parametrii AC

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller



        settings_label = ck.CTkLabel(self, text="Settings", font=TITLE_FONT)
        settings_label.pack()

        class ToggledFrame(tk.Frame):

            def __init__(self, parent, text="", *args, **options):
                tk.Frame.__init__(self, parent, *args, **options)


                self.show = tk.IntVar()
                self.show.set(0)

                self.title_frame = ck.CTkFrame(self)
                self.title_frame.pack(fill="x", expand=1)

                
                

                self.toggle_button = ck.CTkCheckBox(self.title_frame, width=2, text='+', command=self.toggle,
                                                    variable=self.show)
                self.toggle_button.pack(side="right")

                self.sub_frame = tk.Frame(self, relief="sunken", borderwidth=1)

            def toggle(self):
                if bool(self.show.get()):
                    self.sub_frame.pack(fill="x", expand=1)
                    self.toggle_button.configure(text='-')
                else:
                    self.sub_frame.forget()
                    self.toggle_button.configure(text='+')

        
        t = ToggledFrame(self, text="Femi", relief="raised", borderwidth=1)
        t.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")
        ck.CTkLabel(t.title_frame, text="Apperance").pack(side="left", fill="x", expand=1)
        parent.Expense_form_frame=ck.CTkFrame(t.sub_frame)
        parent.Expense_form_frame.pack( fill="x", expand=1)

        Theme_Label= ck.CTkLabel(parent.Expense_form_frame, text="Application Theme")
        Theme_Label.pack(side=LEFT,padx=10)
        self.appearance_mode_optionemenu = ck.CTkOptionMenu(parent.Expense_form_frame, values=["Light", "Dark", "System"])
        self.appearance_mode_optionemenu.pack(side= RIGHT, padx=10)
         
            

        t2 = ToggledFrame(self, text='Resize', relief="raised", borderwidth=1)
        t2.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

        for i in range(10):
            ttk.Treeview(t2.sub_frame).pack()

        t3 = ToggledFrame(self, text='Femi2', relief="raised", borderwidth=1)
        t3.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

        for i in range(10):
            ttk.Label(t3.sub_frame, text='Bar' + str(i)).pack()

class About_Page(tk.Frame):   # Parametrii AC

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        About_Label = ck.CTkLabel(self, text= "Life Family", font=TITLE_FONT)
        About_Label.pack()

    
        Text_Label = ck.CTkLabel(self, text= "Created in 2023 " + "\n" + "Developed by Femi Sowemimo" + "\n" + "Copyright © 2023", font=TITLE_FONT)
        Text_Label.place(relx=0.4,  rely=0.9)

class Modify_Info(tk.Frame): 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        self.parent = parent

        self4=ck.CTkFrame(self,)
        self4.place(relx=0, y=0, relwidth =1, relheight =1) 

        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self4.grid_rowconfigure(20, weight=1)
        self4.grid_columnconfigure(0, weight=1)

        self.parent.first_name_label = ck.CTkLabel(self4, text="First Name", anchor= W)
        self.parent.first_name_label.grid(row=0, column=1)
        self.parent.last_name_label = ck.CTkLabel(self4, text="Last Name", anchor=W)
        self.parent.last_name_label.grid(row=0, column=0)

        self.parent.first_name_entry = ck.CTkEntry(self4)
        self.parent.last_name_entry = ck.CTkEntry(self4)
        self.parent.first_name_entry.grid(row=1, column=1, padx=15, sticky="ew")
        self.parent.last_name_entry.grid(row=1, column=0, padx=15, sticky="ew")

        self.parent.dob_entry=DateEntry(self4,selectmode='day', width= 18)
        self.parent.dob_label = ck.CTkLabel(self4, text="Date Of Birth", anchor=W)
        self.parent.dob_entry.grid(row=1,column=2, padx=15, sticky="ew", ipady = 3)
        self.parent.dob_label.grid(row=0,column=2)        

        self.parent.Address1_label = ck.CTkLabel(self4, text="Address", anchor=W )
        self.parent.Address1_field = ck.CTkEntry(self4)
        self.parent.Address1_label.grid(row=3, column=0, sticky="w",padx=15)
        self.parent.Address1_field.grid(row=4, column=0, columnspan=3, rowspan=1 ,sticky="ew", padx=15)

        self.parent.Address2_label = ck.CTkLabel(self4, text="Address Line 2", anchor=W )
        self.parent.Address2_field = ck.CTkEntry(self4)
        self.parent.Address2_label.grid(row=5, column=0, padx=15, sticky="w")
        self.parent.Address2_field.grid(row=6, column=0, columnspan=3, rowspan=1 , sticky="ew", padx=15)

        self.parent.Town_label = ck.CTkLabel(self4, text="Town", anchor=W )
        self.parent.Town_field = ck.CTkEntry(self4)
        self.parent.Town_label.grid(row=7, column=0)
        self.parent.Town_field.grid(row=8, column=0, padx=15, sticky="ew")

        self.parent.City_label = ck.CTkLabel(self4, text="City", anchor=W )
        self.parent.City_field = ck.CTkEntry(self4)
        self.parent.City_label.grid(row=7, column=1)
        self.parent.City_field.grid(row=8, column=1, columnspan=1, rowspan=1 , padx=15, sticky ="ew")

        self.parent.Postcode_label = ck.CTkLabel(self4, text="Post Code", anchor=W )
        self.parent.Postcode_field = ck.CTkEntry(self4)
        self.parent.Postcode_label.grid(row=7, column=2)
        self.parent.Postcode_field.grid(row=8, column=2)

        self.parent.Contact_Number_label = ck.CTkLabel(self4, text="Contact Number", anchor=W )
        self.parent.Contact_Number = ck.CTkEntry(self4)
        self.parent.Contact_Number_label.grid(row=9, column=0, sticky="w", padx=15)
        self.parent.Contact_Number.grid(row=10, column=0, columnspan=1, rowspan=1 , padx= 15, sticky="ew")

        self.parent.Email_Address_label = ck.CTkLabel(self4, text="Email Address", anchor=W )
        self.parent.Email_Address_entry = ck.CTkEntry(self4)
        self.parent.Email_Address_label.grid(row=9, column=1, sticky="w",padx=15)
        self.parent.Email_Address_entry.grid(row=10, column=1, columnspan=2, rowspan=1, sticky="ew", padx= 15)

        self.parent.Residental_Status_label = ck.CTkLabel(self4, text="Residental Status", anchor=W )
        self.parent.Residental_Status_entry = ck.CTkEntry(self4)
        self.parent.Residental_Status_label.grid(row=13, column=0, sticky="w", padx=15)
        self.parent.Residental_Status_entry.grid(row=14, column=0, columnspan=1, rowspan=1 , padx=15, sticky="ew")

        self.parent.Highest_Level_Of_Qualification_label = ck.CTkLabel(self4, text="Highest Level Of Qualification", anchor=W )
        self.parent.Highest_Level_Of_Qualification_entry = ck.CTkEntry(self4)
        self.parent.Highest_Level_Of_Qualification_label.grid(row=11, column=0, sticky="w", padx=15)
        self.parent.Highest_Level_Of_Qualification_entry.grid(row=12, column=0, columnspan=1, rowspan=1 , padx=15, sticky="ew")

        self.parent.Course_Name_label = ck.CTkLabel(self4, text="Name Of Course")
        self.parent.Course_Name_entry = ck.CTkEntry(self4)
        self.parent.Course_Name_label.grid(row=11, column=1, sticky="w", padx=15)
        self.parent.Course_Name_entry.grid(row=12, column=1, columnspan=2, sticky="ew", padx=15)

        self.parent.Employment_Status_label = ck.CTkLabel(self4, text="Employment Status")
        self.parent.Employment_Status_entry = ck.CTkEntry(self4)
        self.parent.Employment_Status_label.grid(row=13, column=1, sticky="w", padx=15)
        self.parent.Employment_Status_entry.grid(row=14, column=1, padx= 15)

        self.parent.Employer_label = ck.CTkLabel(self4, text="Employer/Agency")
        self.parent.Employer_entry = ck.CTkEntry(self4)
        self.parent.Employer_label.grid(row=13, column=2, sticky="w", padx=15)
        self.parent.Employer_entry.grid(row=14, column=2, padx=15)

        self.parent.Department_Served_in_label = ck.CTkLabel(self4, text="Department Served In")
        self.parent.Department_Served_in_entry = ck.CTkEntry(self4)
        self.parent.Department_Served_in_label.grid(row=15, column=0, sticky="w", padx=15)
        self.parent.Department_Served_in_entry.grid(row=16, column=0, padx=15, sticky="ew")

        
        self.parent.Occupation_Label = ck.CTkLabel(self4, text="Occupation")
        self.parent.Occupation_Label.grid(row=15, column=1, padx=15, sticky="ew")

        self.parent.Occupation_entry = ck.CTkEntry(self4)
        self.parent.Occupation_entry.grid(row=16, column=1, padx=15, sticky="ew")

        self.parent.blank=ck.CTkLabel(self4, text="")
        self.parent.blank.grid(row=17, pady=20)

        self.parent.Notes_Label= ck.CTkLabel(self4, text="Notes")
        self.parent.Notes_Label.grid(row=18, column=0, sticky="w", padx=15,)

        self.parent.Notes_entry = ck.CTkTextbox(self4)
        self.parent.Notes_entry.grid(row=19,column=0, columnspan= 2,padx= 15, sticky="ew")

        


        # Buttons
    

        def enter_data():
            firstname = self.parent.first_name_entry.get()
            lastname = self.parent.last_name_entry.get()

            if firstname and lastname:
                DOB = self.parent.dob_entry.get()
                Address = self.parentAddress1_field.get() + ", " + self.parent.Address2_field.get() + ", " + self.parent.Town_field.get() + "," + self.parent.City_field.get() + self.parent.Postcode_field.get()
                Phone_Number = self.parent.Contact_Number.get()
                Email_Address = self.parent.Email_Address_entry.get()
                Residental_Status = self.parent.Residental_Status_entry.get()
                Highest_Level_Of_Qualification = self.parent.Highest_Level_Of_Qualification_entry.get()
                Course_Name = self.parent.Course_Name_entry.get()
                Employment_Status = self.parent.Employment_Status_entry.get()
                Employer = self.parent.Employer_entry.get()
                Department_Served_in = self.parent.Department_Served_in_entry.get()

                
                # Create Table
                conn = sqlite3.connect("Database3\Life_Family.db")
                
                # Insert Data
                data_insert_query = '''INSERT INTO Life_Family_Members(firstname, lastname, title, 
                age, nationality, registration_status, num_courses, num_semesters) VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?)'''
                data_insert_tuple = (lastname, firstname, DOB,
                                    Address, Phone_Number, Email_Address, Residental_Status, Highest_Level_Of_Qualification, Course_Name, Employment_Status, Employer,Department_Served_in )
                cursor = conn.cursor()
                cursor.execute(data_insert_query, data_insert_tuple)
                conn.commit()
                conn.close()
                
                    
            else:
                tk.messagebox.showwarning(title="Error", message="First name and last name are required.")

        self.button = ck.CTkButton(self4, text="Update Information", command= enter_data, width= 20, height=30)
        self.button.grid(row=20, column=0, sticky="n", ipadx= 30, pady=90)
        self.button1 = ck.CTkButton(self4, text="Cancel", command=lambda: self.controller.show_frame("LifeDirectory"),  width= 120, height=30)
        self.button1.grid(row=20, column=0, sticky="e", ipadx= 30)

class ExpenseForm(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller= controller
        self.expenses = []
        self.categories = [
            "Food",
            "Transportation",
            "Utilities",
            "Entertainment",
            "Other",
        ]
        self.category_var = tk.StringVar(self)
        self.category_var.set(self.categories[0])
        self.currencies = ["USD", "EUR", "GBP", "JPY", "INR"]
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(
            self, text="Expense Tracker", font=("Helvetica", 20, "bold")
        )
        self.label.pack(pady=10)
        self.frame_input = tk.Frame(self)
        self.frame_input.pack(pady=10)
        self.expense_label = tk.Label(
            self.frame_input, text="Expense Amount:", font=("Helvetica", 12)
        )
        self.expense_label.grid(row=0, column=0, padx=5)
        self.expense_entry = tk.Entry(
            self.frame_input, font=("Helvetica", 12), width=15
        )
        self.expense_entry.grid(row=0, column=1, padx=5)
        self.item_label = tk.Label(
            self.frame_input, text="Item Description:", font=("Helvetica", 12)
        )
        self.item_label.grid(row=0, column=2, padx=5)
        self.item_entry = tk.Entry(self.frame_input, font=("Helvetica", 12), width=20)
        self.item_entry.grid(row=0, column=3, padx=5)
        self.category_label = tk.Label(
            self.frame_input, text="Category:", font=("Helvetica", 12)
        )
        self.category_label.grid(row=0, column=4, padx=5)
        self.category_dropdown = ttk.Combobox(
            self.frame_input,
            textvariable=self.category_var,
            values=self.categories,
            font=("Helvetica", 12),
            width=15,
        )
        self.category_dropdown.grid(row=0, column=5, padx=5)
        self.date_label = tk.Label(
            self.frame_input, text="Date (YYYY-MM-DD):", font=("Helvetica", 12)
        )
        self.date_label.grid(row=0, column=6, padx=5)
        self.date_entry = DateEntry(self.frame_input, font=("Helvetica", 12), width=15)
        self.date_entry.grid(row=0, column=7, padx=5)
        self.add_button = tk.Button(self, text="Add Expense", command=self.add_expense)
        self.add_button.pack(pady=5)
        self.frame_list = tk.Frame(self)
        self.frame_list.pack(pady=10)
        self.scrollbar = tk.Scrollbar(self.frame_list)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.expense_listbox = tk.Listbox(
            self.frame_list,
            font=("Helvetica", 12),
            width=70,
            yscrollcommand=self.scrollbar.set,
        )
        self.expense_listbox.pack(pady=5)
        self.scrollbar.config(command=self.expense_listbox.yview)
        self.edit_button = tk.Button(
            self, text="Edit Expense", command=self.edit_expense
        )
        self.edit_button.place(relx=0.20, y=367)
        self.delete_button = tk.Button(
            self, text="Delete Expense", command=self.delete_expense
        )
        self.delete_button.place(relx=0.40, y=367)
        self.save_button = tk.Button(
            self, text="Save Expenses", command=self.save_expenses
        )
        self.save_button.place(relx=0.30, y=367)
        self.total_label = tk.Label(
            self, text="Total Expenses:", font=("Helvetica", 12)
        )
        self.total_label.place(relx=0.50, y=367)
        self.show_chart_button = tk.Button(
            self, text="Show Expenses Chart", command=self.show_expenses_chart
        )
        self.show_chart_button.place(relx=0.66, y=367)
        self.update_total_label()

    def add_expense(self):
        expense = self.expense_entry.get()
        item = self.item_entry.get()
        category = self.category_var.get()
        date = self.date_entry.get()
        if expense and date:
            self.expenses.append((expense, item, category, date))
            self.expense_listbox.insert(tk.END, f"£{expense} - {item} - {category} - ({date})")
            
            conn = sqlite3.connect("Database3\Life_Family.db")

             # Create a cursor instance
            c = conn.cursor()
            
            query=''' INSERT INTO Expenses ("Expense_Amount", "Item_Description", "Catergory", "Date") 
            VALUES (?,?,?,?)
            '''                        
            Expense_data=(expense,item,category,date)
            c.execute(query,Expense_data)
            
            # Commit changes
            conn.commit()

            # Close our connection
            conn.close()

            self.expense_entry.delete(0, tk.END)
            self.item_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Expense and Date cannot be empty.")
            self.update_total_label()
    
    def edit_expense(self):
        selected_index = self.expense_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            selected_expense = self.expenses[selected_index]
            new_expense = simpledialog.askstring(
                "Edit Expense", "Enter new expense:", initialvalue=selected_expense[0]
            )
            if new_expense:
                self.expenses[selected_index] = (
                    new_expense,
                    selected_expense[1],
                    selected_expense[2],
                    selected_expense[3],
                )
                self.refresh_list()
                self.update_total_label()

    def delete_expense(self):
        selected_index = self.expense_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            del self.expenses[selected_index]
            self.expense_listbox.delete(selected_index)
            self.update_total_label()

    def refresh_list(self):
        self.expense_listbox.delete(0, tk.END)
        for expense, item, category, date in self.expenses:
            self.expense_listbox.insert(
                tk.END, f"{expense} - {item} - {category} ({date})"
            )

    def update_total_label(self):
        total_expenses = sum(float(expense[0])
                             for expense in self.expenses)
        self.total_label.config(text=f"Total Expenses: £{total_expenses:.2f}")
        
    def save_expenses(self):

        with open("expenses.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            column_headers = ["Expense Amount", "Item Description", "Category", "Date"]
            writer.writerow(column_headers)
            for expense in self.expenses:
                writer.writerow(expense)

    def show_expenses_chart(self):
        category_totals = {}
        for expense, _, category, _ in self.expenses:
            try:
                amount = float(expense)
            except ValueError:
                continue
            category_totals[category] = category_totals.get(category, 0) + amount
        categories = list(category_totals.keys())
        expenses = list(category_totals.values())
        plt.figure(figsize=(8, 6))
        plt.pie(
            expenses, labels=categories, autopct="%1.1f%%", startangle=140, shadow=True
        )
        plt.axis("equal")
        plt.title(f"Expense Categories Distribution (USD)")
        plt.show()

class SeedTracker(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller= controller
        self.expenses = []
        self.categories = [
            "Funding Partners",
            "Givers Clubs",
            "N/A",
            "Other",
        ]
        self.category_var = tk.StringVar(self)
        self.category_var.set(self.categories[0])
        self.currencies = ["GBP"]
        self.create_widgets()

    def create_widgets(self):
        self.label = ck.CTkLabel(
            self, text="Giving Tracker", font=("Helvetica", 20, "bold")
        )
        self.label.pack(pady=10)
        self.frame_input = tk.Frame(self)
        self.frame_input.pack(pady=10)
        self.expense_label = ck.CTkLabel(
            self.frame_input, text="Amount Submitted:", font=("Helvetica", 16)
        )
        self.expense_label.grid(row=0, column=0, padx=5)
        self.expense_entry = ck.CTkEntry(
            self.frame_input, font=("Helvetica", 12), width=139
        )
        self.expense_entry.grid(row=0, column=1, padx=5)
        self.item_label = ck.CTkLabel(
            self.frame_input, text="Name:", font=("Helvetica", 16)
        )
        self.item_label.grid(row=0, column=2, padx=5)
        self.item_entry = ck.CTkEntry(self.frame_input, font=("Helvetica", 16), width=170)
        self.item_entry.grid(row=0, column=3, padx=5)
        self.category_label = ck.CTkLabel(
            self.frame_input, text="Financial Group:", font=("Helvetica", 16)
        )
        self.category_label.grid(row=0, column=4, padx=5)
        self.category_dropdown = ttk.Combobox(
            self.frame_input,
            textvariable=self.category_var,
            values=self.categories,
            font=("Helvetica", 12),
            width=15,
        )
        self.category_dropdown.grid(row=0, column=5, padx=5)
        self.date_label = tk.Label(
            self.frame_input, text="Date (YYYY-MM-DD):", font=("Helvetica", 12)
        )
        self.date_label.grid(row=0, column=6, padx=5)
        self.date_entry = DateEntry(self.frame_input, font=("Helvetica", 12), width=15)
        self.date_entry.grid(row=0, column=7, padx=5)
        self.add_button = tk.Button(self, text="Add Expense", command=self.add_expense)
        self.add_button.pack(pady=5)
        self.frame_list = tk.Frame(self)
        self.frame_list.pack(pady=10)
        self.scrollbar = tk.Scrollbar(self.frame_list)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.expense_listbox = tk.Listbox(
            self.frame_list,
            font=("Helvetica", 12),
            width=70,
            yscrollcommand=self.scrollbar.set,
        )
        self.expense_listbox.pack(pady=5)
        self.scrollbar.config(command=self.expense_listbox.yview)
        self.edit_button = tk.Button(
            self, text="Edit Expense", command=self.edit_expense
        )
        self.edit_button.pack(pady=5)
        self.delete_button = tk.Button(
            self, text="Delete Expense", command=self.delete_expense
        )
        self.delete_button.pack(pady=5)
        self.save_button = tk.Button(
            self, text="Save Expenses", command=self.save_expenses
        )
        self.save_button.pack(pady=5)
        self.total_label = tk.Label(
            self, text="Total Expenses:", font=("Helvetica", 12)
        )
        self.total_label.pack(pady=5)
        self.show_chart_button = tk.Button(
            self, text="Show Expenses Chart", command=self.show_expenses_chart
        )
        self.show_chart_button.pack(pady=5)
        self.update_total_label()

    def add_expense(self):
        expense = self.expense_entry.get()
        item = self.item_entry.get()
        category = self.category_var.get()
        date = self.date_entry.get()
        if expense and date:
            self.expenses.append((expense, item, category, date))
            self.expense_listbox.insert(
                tk.END, f"{expense} - {item} - {category} ({date})"
            )
            self.expense_entry.delete(0, tk.END)
            self.item_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Expense and Date cannot be empty.")
        self.update_total_label()

    def edit_expense(self):
        selected_index = self.expense_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            selected_expense = self.expenses[selected_index]
            new_expense = simpledialog.askstring(
                "Edit Expense", "Enter new expense:", initialvalue=selected_expense[0]
            )
            if new_expense:
                self.expenses[selected_index] = (
                    new_expense,
                    selected_expense[1],
                    selected_expense[2],
                    selected_expense[3],
                )
                self.refresh_list()
                self.update_total_label()

    def delete_expense(self):
        selected_index = self.expense_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            del self.expenses[selected_index]
            self.expense_listbox.delete(selected_index)
            self.update_total_label()

    def refresh_list(self):
        self.expense_listbox.delete(0, tk.END)
        for expense, item, category, date in self.expenses:
            self.expense_listbox.insert(
                tk.END, f"{expense} - {item} - {category} ({date})"
            )

    def update_total_label(self):
        total_expenses = sum(float(expense[0]) for expense in self.expenses)
        self.total_label.config(text=f"Total Expenses: USD {total_expenses:.2f}")
        
    def save_expenses(self):
        with open("expenses.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            column_headers = ["Expense Amount", "Item Description", "Category", "Date"]
            writer.writerow(column_headers)
            for expense in self.expenses:
                writer.writerow(expense)

    def show_expenses_chart(self):
        category_totals = {}
        for expense, _, category, _ in self.expenses:
            try:
                amount = float(expense)
            except ValueError:
                continue
            category_totals[category] = category_totals.get(category, 0) + amount
        categories = list(category_totals.keys())
        expenses = list(category_totals.values())
        plt.figure(figsize=(8, 6))
        plt.pie(
            expenses, labels=categories, autopct="%1.1f%%", startangle=140, shadow=True
        )
        plt.axis("equal")
        plt.title(f"Expense Categories Distribution (USD)")
        plt.show()    


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()