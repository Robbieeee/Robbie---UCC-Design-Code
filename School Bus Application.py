# Import libraries
from tkinter import ttk
from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
import sqlite3

# Creates title
win = Tk()
win.title("Bus Service Information")
text = Text(win)

# Set the background colour
win.configure(background="#07baa2")

#Used to inform user that information is missing
def dataMissing():
    popupDataMissingWindow = Tk()
    popupDataMissingWindow.wm_title("Information Missing")
    labelDataMissing = Label(popupDataMissingWindow, text="Please enter the missing information.")
    labelDataMissing.grid(row=0, column=0)

# Gets information from database and displays it in the bottom screen
def viewRecords():
        x = bottomscreen.get_children()

        #Clears the screen before displaying on screen
        for item in x:
            bottomscreen.delete(item)

        #Connects to the database and selects the records to be displayed on the screen
        #The try/except informes the user  if the database file is missing
        try:
            conn = sqlite3.connect('bus.db')
            c = conn.cursor()
            list = c.execute("SELECT ParentName, PhoneNumber, ChildGrade, BusStop FROM bus ORDER BY busid")
            for row in list:
                print(row)
                bottomscreen.insert("", 0, values=row)
            c.close()           
        except:
           print("Can't find database")
        

#Creates records in the database        
def createRecord():
        parentname = e1.get()
        phonenumber = e2.get()
        childgrade = e3.get()
        mainIntersection = e4.get()
        
        #Checks if parent name is empty
        if (parentname == ""):
            dataMissing()

        #Checks if phonenumber is empty
        if (phonenumber == ""):
            dataMissing()

        #Checks if childgrade is empty
        if (childgrade == ""):
            dataMissing()

        #Checks if mainIntersection is empty
        if (mainIntersection == ""):
                dataMissing()
            
        #Connect to the database and inserts the records       
        conn = sqlite3.connect('bus.db')
        c = conn.cursor()
        c.execute("INSERT INTO bus (busid, ParentName, PhoneNumber, ChildGrade, BusStop) VALUES(NULL,?,?,?,?)" ,(parentname,phonenumber,childgrade,mainIntersection))
        conn.commit()
        #Closes the cursor and empties the variables
        c.close()
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)

#Exits program
def quit(): 
    win.destroy()
            
# Inserts the Image of the bus
photo = PhotoImage(file='buss.gif')       
l = Label(image=photo)
l.image = photo
l.grid(row=0, column=0, rowspan=2)

# Frame around the entry boxes     
frame1 = LabelFrame(win,borderwidth=10, text= 'Bus Participant Information')
frame1.grid(row=0, column=1, sticky='ew')

# Label 1, at the top, is Parent's name
l1 = Label(frame1,text="Parent's Name: ")
l1.config(font=("Helvetica",20))
l1.grid(row=0,column=1, sticky=W)

# Label 2, is the phone number
l2 = Label(frame1,text="Phone Number: ")
l2.config(font=("Helvetica",20))
l2.grid(row=1,column=1,sticky=W)

# Label 3 is the child's grade
l3 = Label(frame1,text="Child's Grade: ")
l3.config(font=("Helvetica",20))
l3.grid(row=2,column=1,sticky=W)

# Label 4 is the main intersection
l4 = Label(frame1,text="Main Intersection: ")
l4.config(font=("Helvetica",20))
l4.grid(row=3,column=1,sticky=W)

# Entry box 1, with the frame surrounding it
e1 = Entry(frame1)
e1.grid(row=0, column=2, sticky=W+E)

# Entry box 2, with the frame surrounding it
e2 = Entry(frame1)
e2.grid(row=1,column=2, sticky=W+E)

# Entry box 3, with the frame surrounding it
e3 = Entry(frame1)
e3.grid(row=2,column=2, sticky=W+E)

# Entry box 4, with the frame surrounding it
e4 = Entry(frame1)
e4.grid(row=3,column=2, sticky=W+E)

# When this button is clicked, the "thank you" window appears
b1 = Button(frame1,text="Submit",fg="#4e21b8",command=createRecord)
b1.grid(row=5,column=2, sticky=E)

# Creates the table at the bottom of the screen
bottomscreen = ttk.Treeview(column=("col1","col2","col3","col4","col5"))
bottomscreen.grid(row=2, column=0, columnspan=2)
bottomscreen.heading("0", text="Parent's Name")
bottomscreen.heading("1", text="Phone Number")
bottomscreen.heading("2", text="Child's Grade")
bottomscreen.heading("3", text="Main Intersection")

# When this button is clicked the inputted data appears in the table view in the bottom screen
b2 = Button(text="Show Records",fg="#4e21b8", command=viewRecords)
b2.grid(row=1,column=0, sticky=N+W)

#When this button is clicked the program quits
b3 = Button(frame1, text="Quit",fg="#4e21b8", command=quit)
b3.grid(row=5,column=3, sticky=E)
