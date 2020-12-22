from tkinter import *
from tkinter import ttk

def login():
    print("Login sessioned started")
    
    global screen2
    global username_login_2
    global password_login_2
   
    #===========================================SCREEN AFTER CLICKING LOGIN BUTTON====================================================================
    screen2= Tk()#create a screen after clicking on login button
    screen2.geometry("400x400")

    username_login= StringVar()
    password_login= StringVar()
    
    Label(screen2,text="Enter your details", font="Calibri 16", bg="grey", height="1",width="300").pack() # heading
    Label(screen2,text="").pack()
    Label(screen2,text="Username",font="calibri 14").pack()
    username_login_2 = Entry(screen2, textvariable=username_login, width="30")
    username_login_2.pack(pady=10)
    Label(screen2,text="").pack()
    Label(screen2,text="Password",font="calibri 14").pack()
    password_login_2 = Entry(screen2, textvariable=password_login, width="30")
    password_login_2.pack(pady=10)
    Label(screen2,text="").pack()
    Button(screen2,text="Login",font="calibri",width="15",fg="green",command= login_button).pack()
   
    
def login_button():
     username_login_button= username_login_2.get()
     password_login_button= password_login_2.get()
      #===================================================================USING FILE HANDLING TO SAVE INFO IN THE FILE==============================================
     file=open( username_login_button+".txt","w")
     file.write("Login information \n")
     file.write("================================= \n")
     file.write("Username:"+username_login_button+"\n")
     file.write("Password:"+password_login_button+"\n")
     file.write("=================================")
     print("=================================")
     print("Username:"+ username_login_button)
     print("Ps:"+password_login_button)
     print("=================================")
     print("Login Completed")
     Label(screen2,text="Login Sucessfully",font="calibri 14",fg="green").pack(pady=10)
    

def register():
    print("Registration started")
    global screen1
    #=========================================SCREEN AFTER CLICKING REGISTER BUTTON======================================================================
    screen1= Tk()
    screen1.geometry("350x400")
    screen1.title("Registration")
    
    global username
    global password
    global username_entry
    global password_entry
    global username_info
    global password_info
    global contact_info
    global contact_entry
    global convert_to_int
    global int_contact_info
    
    global username_login_2
    global password_login_2
   #globalize variable to access from anywhere
   
    username = StringVar()#declaring variable
    password = StringVar()#declaring variable
    contact  = IntVar()#declaring variable

    Label(screen1, text="Enter details below",font="calibri 16",bg="grey",width="300").pack()#heading
    Label(screen1, text="").pack(pady=20)
    Label(screen1, text="Email",font="calibri 13",width="30").pack()#label
    username_entry= Entry(screen1, textvariable=username,width="30")#taking value from user
    username_entry.pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Password",font="calibri 13").pack()
    password_entry= Entry(screen1, textvariable=password, width="30")#taking value from user
    password_entry.pack()
    Label(screen1, text="").pack()
    Label(screen1,text="Contact No.",font="calibri 13").pack()
    contact_entry= Entry(screen1, textvariable=contact,width="30")
    contact_entry.pack()
    
    Label(screen1, text="").pack()
    
    Button(screen1, text="Register",fg="green",width="15",font="calibri 13",command= register_entry).pack()#Button
    
    
def register_entry():
    
    username_info= username_entry.get()
    password_info= password_entry.get()
    contact_info= contact_entry.get()
    #int_contact_info= int(contact_info)
    #convert_to_int= int(contact_info)
    print("=================================")
    print("Email:"+username_info)
    print("Ps:"+password_info)
    print("Contact no.:"+contact_info)
    print("=================================")
    #===================================================================USING FILE HANDLING TO SAVE INFO IN THE FILE==============================================
    file=open(username_info+".txt","w+")#to create file using file handling
    file.write("Registration\n")
    file.write("================================= \n")
    file.write("Email:"+username_info+"\n")#saving username enter by user in file
    file.write("Ps:"+password_info+"\n")#saving password enter by user in file
    file.write("Contact no.:"+contact_info+"\n")#saving contact enter by user in file
    file.write("=================================")
    file.close
    #======================================================================RESET VALUE IN THE BOX=====================================================================
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    contact_entry.delete(0,END)
 
    
    Label(screen1,text="Registration Successful", fg="green",font="calibri").pack()#message of completion
    print("Registration completed")
    #==============================================================================================================================================================

    #======================================================================FIRST SCREEN=======================================================================#
global screen #to get Screen
screen = Tk()
screen.title("Welcome")
screen.geometry("450x300")#screen size


#welcome_text = Label(text="Submit your detail",font="Calibri 16", bg="grey", height="1",width="300")#heading
#welcome_text.pack()
Label(text = "").pack()#space between

click_me=Button(text="Login",height="1",width="15",font="Calibri 16",bg="grey",fg="Black",command=login)#button for submit
click_me.pack(pady=30)

Label(text = "").pack()

click_me2=Button(text="Register",height="1",width="15",font="Calibri 16",bg="grey",command=register)#button for register
click_me2.pack(pady=30)

screen.mainloop()
