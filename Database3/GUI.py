#Imports
from tkinter import *
from tkinter import ttk, scrolledtext


#GUI Window
root = Tk()
root.title("Life Family")
root.geometry("1920x1080")


#Style
Theme = ttk.Style()
Theme.theme_use('default')

Theme.configure("Treeview", background= '#FDBD01', foreground= '#3A3B3C', rowheight= 25, fieldbackground= "#F0FFFF"   )

Theme.map("Treeview",
    background=[('selected', "#347083")])

tree_frame = Frame(root, width = 170, height = 15)
tree_frame.pack(pady=10,expand="yes")
ID = [1,2,3,4,5,6]
Names = [ "femi", "Benny", "Lauren","Remi"]
Ages = [30, 30, 24, 30]
Gender = ["Male", "Male", "Female", "Female"]
Occupation = [ "IT Technician", "IT Technician", "Director", "UI-UX Developer"]
App_Name = "Life Family Database"
data = [ID, Names, Ages, Gender, Occupation]

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

Life_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
Life_tree.pack(fill="x",expand= "yes", )

tree_scroll.config(command=Life_tree.yview)

Life_tree['columns'] = ("First Name", "Last Name", "Age", "Occupation", "DOB")
Life_tree.column("#0", width=0, stretch=YES) 
Life_tree.column("First Name", anchor=W, width=140)
Life_tree.column("Last Name", anchor=W , width=140)
Life_tree.column("Age", anchor=CENTER, width=100) 
Life_tree.column("Occupation", anchor=CENTER, width=140) 
Life_tree.column("DOB", anchor=CENTER, width=100) 


Life_tree.heading("#0", text="", anchor=W)
Life_tree.heading("First Name", text="First Name", anchor=W)
Life_tree.heading("Last Name", text="Last Name",  anchor=W)
Life_tree.heading("Age", text="Age", anchor=CENTER)
Life_tree.heading("Occupation", text="Occupation", anchor=CENTER)
Life_tree.heading("DOB", text="DOB", anchor=CENTER)


Life_tree.tag_configure('oddrow', background="white")
Life_tree.tag_configure('evenrow', background="lightblue")

global count
count = 0

for record in data:
    if count % 2 == 0:
        Life_tree.insert(parent='', index= 'end', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
else:
    Life_tree.insert(parent='', index= 'end', values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
    count+=1
    
    data_frame = LabelFrame(root, text="Record") 
    data_frame.pack(expand="yes", padx=20)
    
    Information_Label = scrolledtext.ScrolledText(data_frame, width = 120, height = 15, font = ("Times New Roman",15))
    Information_Label.pack(pady = 10, padx = 10)
    Information_Label.configure(state ='disabled')
    
    #Buttons
    
    #Button Frame
    Button_frame = LabelFrame(root, text="Entry") 
    Button_frame.pack(fill="x", expand="yes", padx=20)
    
    
        
        
        
    #Buttons
    Update_button = Button(Button_frame, text="Update/Edit Record", command=Update_info)
    Update_button.grid(row=0, column=3, padx=10, pady=10)
    
    remove_button = Button(Button_frame, text="Remove Selected Record")
    remove_button.grid(row=0, column=2, padx=10, pady=10)
    def Add_entry():
        import Entry_Form
    
    add_button = Button(Button_frame, text="Add Record", command=Add_entry)
    add_button.grid(row=0, column=1, padx=10, pady=10)
    
    a_button = Button(Button_frame, text="Remove Selected Record")
    a_button.grid(row=0, column=4, padx=10, pady=10)
    
    root.mainloop()
    