#Entry Form
import tkinter
import tkinter as tk
from tkinter import W, ttk
from tkinter import messagebox
from tkinter import *
from tkcalendar import DateEntry
import customtkinter as ck

class Entry_Form(ck.CTk):
    def __init__(self,Main):
        super
        self.title("Modify Member Information")
        
        self.frame = ck.CTkFrame(self)
        self.frame.pack()
        
        user_info_frame =ck.CTkFrame(self.frame, text="User Information")
        user_info_frame.grid(row= 0, column=0, padx=20, pady=10)
        
        first_name_label = ck.CTkLabel(user_info_frame, text="First Name", anchor= W)
        first_name_label.grid(row=0, column=0)
        last_name_label = tkinter.Label(user_info_frame, text="Last Name", anchor=W)
        last_name_label.grid(row=0, column=1)
        
        first_name_entry = ck.CTkEntry(user_info_frame)
        last_name_entry = tkinter.Entry(user_info_frame)
        first_name_entry.grid(row=1, column=0, padx=15, sticky="ew")
        last_name_entry.grid(row=1, column=1, padx=15, sticky="ew")
        
        Address1_label = ck.CTkLabel(user_info_frame, text="Address", anchor=W )
        Address1_field = ck.CTkEntry(user_info_frame)
        Address1_label.grid(row=3, column=0, sticky="w",padx=15)
        Address1_field.grid(row=4, column=0, columnspan=3, rowspan=1 ,sticky="ew", padx=15)
        
        Address2_label = ck.CTkLabel(user_info_frame, text="Address Line 2", anchor=W )
        Address2_field = ck.CTkEntry(user_info_frame)
        Address2_label.grid(row=5, column=0, padx=15, sticky="w")
        Address2_field.grid(row=6, column=0, columnspan=3, rowspan=1 , sticky="ew", padx=15)
        
        Town_label = tkinter.Label(user_info_frame, text="Town", anchor=W )
        Town_field = tkinter.Entry(user_info_frame)
        Town_label.grid(row=7, column=0)
        Town_field.grid(row=8, column=0, padx=15, sticky="ew")
        
        City_label = tkinter.Label(user_info_frame, text="City", anchor=W )
        City_field = tkinter.Entry(user_info_frame)
        City_label.grid(row=7, column=1)
        City_field.grid(row=8, column=1, columnspan=1, rowspan=1 , padx=15, sticky ="ew")
        
        Postcode_label = tkinter.Label(user_info_frame, text="Post Code", anchor=W )
        Postcode_field = tkinter.Entry(user_info_frame)
        Postcode_label.grid(row=7, column=2)
        Postcode_field.grid(row=8, column=2)
        
        Contact_Number_label = tkinter.Label(user_info_frame, text="Contact Number", anchor=W )
        Contact_Number = tkinter.Entry(user_info_frame)
        Contact_Number_label.grid(row=9, column=0, sticky="w", padx=15)
        Contact_Number.grid(row=10, column=0, columnspan=1, rowspan=1 , padx= 15, sticky="ew")
        
        Email_Address_label = tkinter.Label(user_info_frame, text="Email Address", anchor=W )
        Email_Address_entry = tkinter.Entry(user_info_frame)
        Email_Address_label.grid(row=9, column=1, sticky="w",padx=15)
        Email_Address_entry.grid(row=10, column=1, columnspan=2, rowspan=1, sticky="ew", padx= 15)
        
        Residental_Status_label = tkinter.Label(user_info_frame, text="Residental Status", anchor=W )
        Residental_Status_entry = tkinter.Entry(user_info_frame)
        Residental_Status_label.grid(row=13, column=0, sticky="w", padx=15)
        Residental_Status_entry.grid(row=14, column=0, columnspan=1, rowspan=1 , padx=15, sticky="ew")
        
        Highest_Level_Of_Qualification_label = tkinter.Label(user_info_frame, text="Highest Level Of Qualification", anchor=W )
        Highest_Level_Of_Qualification_entry = ttk.Combobox(user_info_frame, values=["Python", "C", "C++", "Java"])
        Highest_Level_Of_Qualification_label.grid(row=11, column=0, sticky="w", padx=15)
        Highest_Level_Of_Qualification_entry.grid(row=12, column=0, columnspan=1, rowspan=1 , padx=15, sticky="ew")
        
        Course_Name_label = tkinter.Label(user_info_frame, text="Name Of Course")
        Course_Name_entry = tkinter.Entry(user_info_frame)
        Course_Name_label.grid(row=11, column=1, sticky="w", padx=15)
        Course_Name_entry.grid(row=12, column=1, columnspan=2, sticky="ew", padx=15)
        
        Employment_Status_label = tkinter.Label(user_info_frame, text="Employment Status")
        Employment_Status_entry = ttk.Combobox(user_info_frame,values=["Python", "C", "C++", "Java"])
        Employment_Status_label.grid(row=13, column=1, sticky="w", padx=15)
        Employment_Status_entry.grid(row=14, column=1, padx= 15)
        
        Employer_label = tkinter.Label(user_info_frame, text="Employer/Agency")
        Employer_entry = ttk.Entry(user_info_frame)
        Employer_label.grid(row=13, column=2, sticky="w", padx=15)
        Employer_entry.grid(row=14, column=2, padx=15)
        
        Department_Served_in_label = tkinter.Label(user_info_frame, text="Department Served In")
        Department_Served_in_entry = ttk.Entry(user_info_frame)
        Department_Served_in_label.grid(row=15, column=0, sticky="w", padx=15)
        Department_Served_in_entry.grid(row=16, column=0, padx=15, sticky="ew")
        
        dob_entry=DateEntry(user_info_frame,selectmode='day', width= 18)
        dob_label = tkinter.Label(user_info_frame, text="Date Of Birth", anchor=W)
        dob_entry.grid(row=1,column=2, padx=15)
        dob_label.grid(row=0,column=2)
        
        Additional_Info = tkinter.LabelFrame(frame, text="Notes", padx=10, pady=5)
        Additional_Info.grid(row=1,column = 0, padx=20, pady=10)
        
        Notes_entry = Text(Additional_Info, bg= "White", height=10, width = 64)
        Notes_entry.pack()
        
    
                
    def save_Record():
        self.members.append(Entry_Form)
                
button = tkinter.Button(self.frame, text="Update Information", command= Entry_Form.save_Record, width= 20, height=2)
button.grid(row=0, column=1, padx=10, pady=10)
button.grid_rowconfigure(0, weight=1)
button1 = tkinter.Button(terms_frame, text="Cancel", command= exit,  width= 20, height=2)
button1.grid(row=0, column=2,padx=10, pady=10)
    
if __name__ == "__main__":
    Entry_Form = Entry_Form()
    Entry_Form.mainloop()


Entry_Form()
