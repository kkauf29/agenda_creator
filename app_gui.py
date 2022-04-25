###
# Kim Kaufman
# CSC 217
# 4-11-22
# This file will create the GUI for the agenda creator app

import tkinter as tk
from tkinter import messagebox
import sqlite3




def display_agenda(): 
    #this function will display the info from the form enteries and the database
    pass

#def clicked(): # displays message when the submit button is clicked
#   messagebox.showinfo('Message title', 'Thank you for submitting your agenda items')

def main():
    
    window = tk.Tk() # creates root window object

    window.title("Agenda Creator")
    window.geometry("500x500") 
    
    content = tk.Frame(window) #creates frame for content within root window
    content.grid(padx=5, pady=5)

    prompt = tk.Label(content, text="Fill out this form to add your items to the agenda")
    prompt.grid(column=0, row=0, pady=15, sticky="w", columnspan=2)

    # label and entry pairs are created for all of the form fields with tk.Label and tk.Entry
    # grid is used to position the elements 
    label1 = tk.Label(content, text="Date:")
    label1.grid(column=0, row=1, sticky="w")
    
    dateEntry = tk.StringVar()
    entry1 = tk.Entry(content, width=10, textvariable=dateEntry)
    entry1.grid(column=1, row=1, sticky="w")
    
    label2 = tk.Label(content, text="Meeting Start Time:")
    label2.grid(column=0, row=7, sticky="w")
    
    startTime = tk.StringVar()
    entry2 = tk.Entry(content, width=10, textvariable=startTime)
    entry2.grid(column=1, row=7, sticky="w")    
    
    label3 = tk.Label(content, text="Item Length:")
    label3.grid(column=0, row=8, sticky="w")
    
    itemLength = tk.StringVar()
    entry3 = tk.Entry(content, width=10, textvariable=itemLength)
    entry3.grid(column=1, row=8, sticky="w")  
    
    label4 = tk.Label(content,text="Presenter First Name:")
    label4.grid(column=0, row=2, sticky="w")
    
    presenterFName = tk.StringVar()
    entry4 = tk.Entry(content, width=25, textvariable=presenterFName)
    entry4.grid(column=1, row=2, sticky="w")
    
    label5 = tk.Label(content, text="Presenter Last Name:")
    label5.grid(column=0, row=3, sticky="w")
    
    presenterLName = tk.StringVar()
    entry5 = tk.Entry(content, width=25, textvariable=presenterLName)
    entry5.grid(column=1, row=3, sticky="w")
    
    label6 = tk.Label(content, text="Agenda Item:")
    label6.grid(column=0, row=4, sticky="w")
    
    agendaItem = tk.StringVar()
    entry6 = tk.Entry(content, width=25, textvariable=agendaItem)
    entry6.grid(column=1, row=4, sticky="w")    
    
    label7 = tk.Label(content, text="Bullet Point 1:")
    label7.grid(column=0, row=5, sticky="w")
    
    bulletPoint1 = tk.StringVar()
    entry7 = tk.Entry(content, width=25, textvariable=bulletPoint1)
    entry7.grid(column=1, row=5, sticky="w")    
    
    label8 = tk.Label(content, text="Bullet Point 2:")
    label8.grid(column=0, row=6, sticky="w")
    
    bulletPoint2 = tk.StringVar()
    entry8 = tk.Entry(content, width=25, textvariable=bulletPoint2)
    entry8.grid(column=1, row=6, sticky="w")      
    
    label9 = tk.Label(content, text="Department:")
    label9.grid(column=0, row=9, sticky="w")
    
    departmentSelected = tk.IntVar()
    rad1 = tk.Radiobutton(content, text="Sales", value=1, variable=departmentSelected)
    rad1.grid(column=0, row=10, sticky="w") 
    
    rad2 = tk.Radiobutton(content, text="Accounting", value=2, variable=departmentSelected)
    rad2.grid(column=0, row=11, sticky="w")
    
    rad3 = tk.Radiobutton(content, text="IT", value=3, variable=departmentSelected)
    rad3.grid(column=0, row=12, sticky="w")
    
    rad4 = tk.Radiobutton(content, text="HR", value=4, variable=departmentSelected)
    rad4.grid(column=0, row=13, sticky="w")
    
    def get_entries():
    # this function will get information for the form entries
        dateE = dateEntry.get()
        startT = startTime.get()
        itemL = itemLength.get()
        presenterF = presenterFName.get()
        presenterL = presenterLName.get() 
        agendaI = agendaItem.get()
        bulletP1 = bulletPoint1.get()
        bulletP2 = bulletPoint2.get()
        departmentS = departmentSelected.get()
        
        departmentType = 'Unknown'
        if departmentS == 1:
            departmentType = 'Sales'
        elif departmentS == 2:
            departmentType = 'Accounting'
        elif departmentS == 3:
            departmentType = 'IT'        
        elif departmentS == 4:
            departmentType = 'HR'
        else:
            departmentType = 'Unkown'        
        

    
        mydb = sqlite3.connect('Agenda_Creator.db')
        myCursor = mydb.cursor()
        myCursor.execute("Insert INTO agenda (meeting_date, presenter_fname, presenter_lname, agenda_item, bullet_point1, bullet_point2, meeting_start_time, item_length, department) VALUES (?,?,?,?,?,?,?,?,?)",
                    [dateE,presenterF,presenterL,agendaI,bulletP1,bulletP2,startT,itemL,departmentType] )
        mydb.commit()
    
        mydb.close()
        labelAction['text'] = 'Database Updated.'
        messagebox.showinfo('Message title', 'Thank you for submitting your agenda items')
    
        entry1.delete(0, tk.END)    
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)
        entry5.delete(0, tk.END)
        entry6.delete(0, tk.END)
        entry7.delete(0, tk.END)
        entry8.delete(0, tk.END)
        departmentSelected.set(0)
        
    def display_agenda():
        display_window = tk.Tk() # creates root window object

        display_window.title("Agenda Creator")
        display_window.geometry("500x500") 
    
        content = tk.Frame(window) #creates frame for content within root window
        content.grid(padx=5, pady=5) 
        
        mydb = sqlite3.connect('Agenda_Creator.db')
        myCursor = mydb.cursor()   
        myCursor.execute('SELECT ')
        
        
    btn = tk.Button(content, text="Submit", command=get_entries)
    btn.grid(column=0, row=14, sticky="w")   
    
    btn2 = tk.Button(content, text="Get Agenda", command=display_agenda)
    btn2.grid(column=0, row=15, sticky="w")

   # get_entries(dateEntry, startTime, itemLength, presenterFName, presenterLName, agendaItem, bulletPoint1, bulletPoint2, departmentSelected)
    
    labelAction = tk.Label(text="No Action taken yet.")
    labelAction.grid(column=0,row=19)
    
    window.mainloop()


if __name__ == "__main__":
    main()
        

