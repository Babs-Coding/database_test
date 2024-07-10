#Entry Form
import tkinter
import tkinter  as tk
from tkinter import W, ttk
from tkinter import messagebox
from tkinter import *
from tkcalendar import DateEntry
import customtkinter as ck
import sqlite3

    
window = ck.CTk()
    
window.title("Modify Member Information")


frame = ck.CTkFrame(window)
frame.pack()


# Saving User Info
user_info_frame =ck.CTkFrame(frame)
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)


first_name_label = ck.CTkLabel(user_info_frame, text="First Name", anchor= W)
first_name_label.grid(row=0, column=0)
last_name_label = ck.CTkLabel(user_info_frame, text="Last Name", anchor=W)
last_name_label.grid(row=0, column=1)

first_name_entry = ck.CTkEntry(user_info_frame)
last_name_entry = ck.CTkEntry(user_info_frame)
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

Town_label = ck.CTkLabel(user_info_frame, text="Town", anchor=W )
Town_field = ck.CTkEntry(user_info_frame)
Town_label.grid(row=7, column=0)
Town_field.grid(row=8, column=0, padx=15, sticky="ew")

City_label = ck.CTkLabel(user_info_frame, text="City", anchor=W )
City_field = ck.CTkEntry(user_info_frame)
City_label.grid(row=7, column=1)
City_field.grid(row=8, column=1, columnspan=1, rowspan=1 , padx=15, sticky ="ew")

Postcode_label = ck.CTkLabel(user_info_frame, text="Post Code", anchor=W )
Postcode_field = ck.CTkEntry(user_info_frame)
Postcode_label.grid(row=7, column=2)
Postcode_field.grid(row=8, column=2)

Contact_Number_label = ck.CTkLabel(user_info_frame, text="Contact Number", anchor=W )
Contact_Number = ck.CTkEntry(user_info_frame)
Contact_Number_label.grid(row=9, column=0, sticky="w", padx=15)
Contact_Number.grid(row=10, column=0, columnspan=1, rowspan=1 , padx= 15, sticky="ew")

Email_Address_label = ck.CTkLabel(user_info_frame, text="Email Address", anchor=W )
Email_Address_entry = ck.CTkEntry(user_info_frame)
Email_Address_label.grid(row=9, column=1, sticky="w",padx=15)
Email_Address_entry.grid(row=10, column=1, columnspan=2, rowspan=1, sticky="ew", padx= 15)


Residental_Status_label = ck.CTkLabel(user_info_frame, text="Residental Status", anchor=W )
Residental_Status_entry = ck.CTkEntry(user_info_frame)
Residental_Status_label.grid(row=13, column=0, sticky="w", padx=15)
Residental_Status_entry.grid(row=14, column=0, columnspan=1, rowspan=1 , padx=15, sticky="ew")

Highest_Level_Of_Qualification_label = ck.CTkLabel(user_info_frame, text="Highest Level Of Qualification", anchor=W )
Highest_Level_Of_Qualification_entry = ck.CTkComboBox(user_info_frame, values=["Python", "C", "C++", "Java"])
Highest_Level_Of_Qualification_label.grid(row=11, column=0, sticky="w", padx=15)
Highest_Level_Of_Qualification_entry.grid(row=12, column=0, columnspan=1, rowspan=1 , padx=15, sticky="ew")

Course_Name_label = ck.CTkLabel(user_info_frame, text="Name Of Course")
Course_Name_entry = ck.CTkEntry(user_info_frame)
Course_Name_label.grid(row=11, column=1, sticky="w", padx=15)
Course_Name_entry.grid(row=12, column=1, columnspan=2, sticky="ew", padx=15)

Employment_Status_label = ck.CTkLabel(user_info_frame, text="Employment Status")
Employment_Status_entry = ck.CTkComboBox(user_info_frame,values=["Python", "C", "C++", "Java"])
Employment_Status_label.grid(row=13, column=1, sticky="w", padx=15)
Employment_Status_entry.grid(row=14, column=1, padx= 15)

Employer_label = ck.CTkLabel(user_info_frame, text="Employer/Agency")
Employer_entry = ck.CTkEntry(user_info_frame)
Employer_label.grid(row=13, column=2, sticky="w", padx=15)
Employer_entry.grid(row=14, column=2, padx=15)

Department_Served_in_label = ck.CTkLabel(user_info_frame, text="Department Served In")
Department_Served_in_entry = ck.CTkEntry(user_info_frame)
Department_Served_in_label.grid(row=15, column=0, sticky="w", padx=15)
Department_Served_in_entry.grid(row=16, column=0, padx=15, sticky="ew")


dob_entry=DateEntry(user_info_frame,selectmode='day', width= 18)
dob_label = ck.CTkLabel(user_info_frame, text="Date Of Birth", anchor=W)
dob_entry.grid(row=1,column=2, padx=15, sticky="ew", ipady = 3)
dob_label.grid(row=0,column=2)

#age_label = ck.CTkLabel(user_info_frame, text="Age")
#age_spinbox = tkinter.Spinbox(user_info_frame, from_=10, to=110)
#age_label.grid(row=0, column=3)
#age_spinbox.grid(row=1, column=3)

Additional_Info = tk.LabelFrame(frame, text="Notes", padx=10, pady=5)
Additional_Info.grid(row=1,column = 0, padx=20, pady=10)

Notes_entry = Text(Additional_Info, bg= "White", height=10, width = 64)
Notes_entry.pack()

def exit() :
    quit()

# Buttons
terms_frame = Frame(frame,  borderwidth = 0, highlightthickness = 0)
terms_frame.grid(row=2, column=0, padx=20, pady=10)

def enter_data():
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()

    if firstname and lastname:
        DOB = dob_entry.combobox.get()
        Address = Address1_field.get() + ", " + Address2_field.get() + ", " + Town_field.get() + "," + City_field.get() + Postcode_field.get()
        Phone_Number = Contact_Number.get()
        Email_Address = Email_Address_entry.get()
        Residental_Status = Residental_Status_entry.get()
        Highest_Level_Of_Qualification = Highest_Level_Of_Qualification_entry.get()
        Course_Name = Course_Name_entry.get()
        Employment_Status = Employment_Status_entry.get()
        Employer = Employer_entry.get()
        Department_Served_in = Department_Served_in_entry.get()
        
        # Create Table
        conn = sqlite3.connect("Database3\Life Family.db")
        
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
        tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")

button = ck.CTkButton(terms_frame, text="Update Information", command= enter_data, width= 20, height=30)
button.grid(row=0, column=1)
button1 = ck.CTkButton(terms_frame, text="Cancel", command= exit,  width= 120, height=30)
button1.grid(row=0, column=2)

    


window.mainloop()