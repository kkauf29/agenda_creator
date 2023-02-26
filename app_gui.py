###
# Kim Kaufman
# CSC 217
# 4-25-22
# This file will create the GUI for the agenda creator app and use this 
# form to submit values to the Agenda_Creator database

import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import date, time, datetime


class Agenda_Form(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.title("Agenda Creator")
        self.geometry("500x500")
        self.configure(bg="black") 
    
        #creates frame for content within root window
        self.content = tk.Frame() 
        self.content.grid(padx=5, pady=5)
        self.content.configure(bg="black")

        self.prompt = tk.Label(
            self.content, 
            text="Fill out this form to add your items to the agenda",
            bg="black",
            fg="white"
            )            
        self.prompt.grid(column=0, row=0, pady=15, sticky="w", columnspan=2)

        # label and entry pairs are created for all of the form fields with tk.Label and tk.Entry
        # grid is used to position the elements
        #Date 
        self.label1 = tk.Label(self.content, text="Date (YYYY-MM-DD):", bg="black", fg="white")
        self.label1.grid(column=0, row=1, sticky="w")    
        self.dateEntry = tk.StringVar()
        self.entry1 = tk.Entry(self.content, width=10, textvariable=self.dateEntry)
        self.entry1.config(highlightbackground="black")
        self.entry1.grid(column=1, row=1, sticky="w")
    
        #meeting start time label and entry field
        self.label2 = tk.Label(
            self.content, 
            text="Meeting Start Time (24 hour HH:MM):", 
            bg="black", 
            fg="white"
            )
        self.label2.grid(column=0, row=7, sticky="w")    
        self.startTime = tk.StringVar()
        self.entry2 = tk.Entry(self.content, width=10, textvariable=self.startTime)
        self.entry2.config(highlightbackground="black")
        self.entry2.grid(column=1, row=7, sticky="w")    
    
        #item length 
        self.label3 = tk.Label(
            self.content, 
            text="Item Length (use minutes):",
            bg="black",
            fg="white"
            )
        self.label3.grid(column=0, row=8, sticky="w")
        self.itemLength = tk.StringVar()
        self.entry3 = tk.Entry(self.content, width=10, textvariable=self.itemLength)
        self.entry3.config(highlightbackground="black")
        self.entry3.grid(column=1, row=8, sticky="w")  
    
        #presenter first name
        self.label4 = tk.Label(self.content,text="Presenter First Name:", bg="black", fg="white")
        self.label4.grid(column=0, row=2, sticky="w")
        self.presenterFName = tk.StringVar()
        self.entry4 = tk.Entry(self.content, width=25, textvariable=self.presenterFName)
        self.entry4.config(highlightbackground="black")
        self.entry4.grid(column=1, row=2, sticky="w")
    
        #presenter first name
        self.label5 = tk.Label(self.content, text="Presenter Last Name:", bg="black", fg="white")
        self.label5.grid(column=0, row=3, sticky="w")
        self.presenterLName = tk.StringVar()
        self.entry5 = tk.Entry(self.content, width=25, textvariable=self.presenterLName)
        self.entry5.config(highlightbackground="black")
        self.entry5.grid(column=1, row=3, sticky="w")
    
        #agenda item label and entry field
        self.label6 = tk.Label(self.content, text="Agenda Item:", bg="black", fg="white")
        self.label6.grid(column=0, row=4, sticky="w")
        self.agendaItem = tk.StringVar()
        self.entry6 = tk.Entry(self.content, width=25, textvariable=self.agendaItem)
        self.entry6.config(highlightbackground="black")
        self.entry6.grid(column=1, row=4, sticky="w")    
    
        #bullet point 1 label and entry field
        self.label7 = tk.Label(self.content, text="Bullet Point 1:", bg="black", fg="white")
        self.label7.grid(column=0, row=5, sticky="w")
        self.bulletPoint1 = tk.StringVar()
        self.entry7 = tk.Entry(self.content, width=25, textvariable=self.bulletPoint1)
        self.entry7.config(highlightbackground="black")
        self.entry7.grid(column=1, row=5, sticky="w")    
    
        # bullet point 2 label and entry field
        self.label8 = tk.Label(self.content, text="Bullet Point 2:", bg="black", fg="white")
        self.label8.grid(column=0, row=6, sticky="w")
        self.bulletPoint2 = tk.StringVar()
        self.entry8 = tk.Entry(self.content, width=25, textvariable=self.bulletPoint2)
        self.entry8.config(highlightbackground="black")
        self.entry8.grid(column=1, row=6, sticky="w")      
    
        #Department label and radio buttons
        self.label9 = tk.Label(self.content, text="Department:", bg="black", fg="white")
        self.label9.grid(column=0, row=9, sticky="w")
        self.departmentSelected = tk.IntVar()
        self.rad1 = tk.Radiobutton(
            self.content, 
            text="Sales", 
            value=1, 
            variable=self.departmentSelected,
            bg="black",
            fg="white"
            )
        self.rad1.grid(column=0, row=10, sticky="w") 
    
        self.rad2 = tk.Radiobutton(
            self.content, 
            text="Accounting", 
            value=2, 
            variable=self.departmentSelected,
            bg="black",
            fg="white"
            )
        self.rad2.grid(column=0, row=11, sticky="w")
    
        self.rad3 = tk.Radiobutton(
            self.content, 
            text="IT", 
            value=3, 
            variable=self.departmentSelected,
            bg="black",
            fg="white"
            )
        self.rad3.grid(column=0, row=12, sticky="w")
    
        self.rad4 = tk.Radiobutton(
            self.content, 
            text="HR", 
            value=4, 
            variable=self.departmentSelected,
            bg="black",
            fg="white"
            )
        self.rad4.grid(column=0, row=13, sticky="w")
    
        btn = tk.Button(
            self.content, 
            text="Submit", 
            command=self.get_entries, 
            highlightbackground="black"
            )
        btn.grid(column=0, row=14, sticky="w")   
    
        btn2 = tk.Button(
            self.content, 
            text="Get Agenda", 
            command=self.date_prompt, 
            highlightbackground="black"
            )
        btn2.grid(column=0, row=15, sticky="w")

    
        self.labelAction = tk.Label(text="No Action taken yet.", bg="black", fg="white")
        self.labelAction.grid(column=0,row=19)
    
    def get_entries(self):
        # this function will get information from the form entries 
        # and insert this info into the SQLite database
        dateE = self.dateEntry.get()
        startT = self.startTime.get()
        itemL = self.itemLength.get()
        presenterF = self.presenterFName.get()
        presenterL = self.presenterLName.get() 
        agendaI = self.agendaItem.get()
        bulletP1 = self.bulletPoint1.get()
        bulletP2 = self.bulletPoint2.get()
        departmentS = self.departmentSelected.get()
        
        # gets the departments from the radio button values
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
        
        #concatenates meeting start date and time to be in one column that takes datetime values 
        agendaDateTime = dateE + " " + startT
        agendaDateTime = datetime.strptime(agendaDateTime, "%Y-%m-%d %H:%M")
        

        #inserts form values into database
        mydb = sqlite3.connect('Agenda_Creator.db')
        myCursor = mydb.cursor()
        myCursor.execute("Insert INTO agenda (meeting_date_time, presenter_fname, presenter_lname, agenda_item, bullet_point1, bullet_point2, item_length, department) VALUES (?,?,?,?,?,?,?,?)",
                    [agendaDateTime,presenterF,presenterL,agendaI,bulletP1,bulletP2,itemL,departmentType] )
        mydb.commit()
    
        mydb.close()
        self.labelAction['text'] = 'Database Updated.'
        messagebox.showinfo('Message title', 'Thank you for submitting your agenda items')
    
        self.entry1.delete(0, tk.END)    
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)
        self.entry5.delete(0, tk.END)
        self.entry6.delete(0, tk.END)
        self.entry7.delete(0, tk.END)
        self.entry8.delete(0, tk.END)
        self.departmentSelected.set(0)
        
    def date_prompt(self):
        # This function will eventually display information from the database
       
        self.display_window = tk.Tk() # creates root window object

        self.display_window.title("Agenda Creator")
        self.display_window.geometry("500x500")
        self.display_window.configure(bg="black")
    
        self.frame1 = tk.Frame(self.display_window) #creates frame for content within root window
        self.frame1.grid(padx=5, pady=5)
        self.frame1.configure(bg="black")
        
        self.prompt = tk.Label(
            self.frame1, 
            text="Please select the date and time for your meeting:",
            bg="black",
            fg="white"
            )            
        self.prompt.grid(column=0, row=0, pady=15, sticky="w", columnspan=2)
        
        mydb = sqlite3.connect('Agenda_Creator.db')
        myCursor = mydb.cursor()
        query = '''SELECT DISTINCT meeting_date_time FROM agenda'''
        myCursor.execute(query)
        dateTimes = myCursor.fetchall()
    
        self.clicked = tk.StringVar(self.frame1)
        self.clicked.set("select")
        self.dropDown = tk.OptionMenu(self.frame1, self.clicked, *dateTimes)
        self.dropDown.config(fg="white", bg="black")
        self.dropDown.grid(column=0, row=1)
        
        
        displayButton = tk.Button(
             self.frame1, 
             text="Display Agenda", 
             command=self.display_agenda, 
             highlightbackground="black")
        displayButton.grid(column=3, row=1, sticky="w") 
                    
        mydb.close()
        
         
    def display_agenda(self):
        
        #self.frame2 = tk.Frame(self.display_window) 

        selectedMeeting = self.clicked.get()
        print(selectedMeeting)
        
        selectedMeet = ""
        for item in selectedMeeting:
            selectedMeet = selectedMeet + item
            selectedMeet = selectedMeet.strip("(),''")
        print(selectedMeet)
        
        selectedMeetDT = datetime.strptime(selectedMeet, "%Y-%m-%d %H:%M:%S")
        
        conn = sqlite3.connect('Agenda_Creator.db')
        cursor2 = conn.cursor()
        query2 = '''SELECT * FROM agenda 
                    WHERE meeting_date_time = ?'''
        cursor2.execute(query2, [selectedMeetDT])
       
        agendaItems = cursor2.fetchall() 
        

        self.labelMeeting = tk.Label(
            self.frame1, 
            text=f"Agenda for Meeting {selectedMeetDT}", 
            bg="black", 
            fg="white"
            )
        self.labelMeeting.grid(column=0, row=10, columnspan=2)
        
        today = datetime.now()
        time_span = (selectedMeetDT - today).days
        self.labelTime = tk.Label(
            self.frame1, 
            text=f"This meeting will take place in {time_span} days", 
            bg="black", 
            fg="white"
            )
        self.labelTime.grid(column=0, row=11, columnspan=2, sticky="W")
        
        
        row_index=12
        for i, row in enumerate(agendaItems):
            self.labelAgendaItem = tk.Label(
                self.frame1,
                text=f"{row[4]} - {row[2]} {row[3]} - {row[8]} - {row[7]} mins",
                bg="black",
                fg="white"
            )
            self.labelAgendaItem.grid(column=0, row=row_index + i, sticky="W")
            
            self.labelBP1 = tk.Label(
                self.frame1,
                text=f"--- {row[5]}",
                bg="black",
                fg="white"
            )
            self.labelBP1.grid(column=0, row=row_index + i + 1, sticky="W")
            
            self.labelBP2 = tk.Label(
                self.frame1,
                text=f"--- {row[6]}",
                bg="black",
                fg="white"
            )
            self.labelBP2.grid(column=0, row=row_index + i + 2, sticky="W")
            row_index += 3
        conn.close()
        

    
    
def main():
    agenda = Agenda_Form()
    Agenda_Form.mainloop(agenda)


if __name__ == "__main__":
    main()
        

