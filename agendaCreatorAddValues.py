###
#  Kim Kaufman
#  CSC 217
#  4/4/22
#  This python code inserts values into the agenda table and runs a select query to output data

import sqlite3

def main():
    conn = sqlite3.connect('Agenda_Creator.db')
    my_cursor = conn.cursor()
    
    sql = '''INSERT INTO agenda (meeting_date, presenter_fname, presenter_lname, agenda_item, 
    bullet_point1, bullet_point2, meeting_start_time, item_length, department)
    VALUES ('2022-05-23','Sally', 'McGregor', 'leadership change', 'Ellen Mann will now lead accounting and HR', 
    'Ted Williams will take over as direct supervisor for accounting', '10:45', '10 minutes', 'Accounting')'''
    
    my_cursor.execute(sql)
    conn.commit()
    print(my_cursor.rowcount, "record inserted.")
    
    
    sql = '''INSERT INTO agenda (meeting_date, presenter_fname, presenter_lname, agenda_item, 
    bullet_point1, bullet_point2, meeting_start_time, item_length, department)
    VALUES ('2022-05-23', 'Ellen', 'Mann', 'New Report Procedure', 'Submit monthly reports to Ted Williams', 
    'Make sure new department code is on report', '10:45', '15 minutes', 'Accounting')'''
    
    my_cursor.execute(sql)
    conn.commit()
    print(my_cursor.rowcount, "record inserted.")
    
    sql = '''INSERT INTO agenda (meeting_date, presenter_fname, presenter_lname, agenda_item, 
    bullet_point1, bullet_point2, meeting_start_time, item_length, department)
    VALUES ('2022-05-23', 'Alan', 'Borg', 'New Procedure', 'Submit reports on time', 
    'code is on report', '10:55', '11 minutes', 'Accounting')'''
    
    my_cursor.execute(sql)
    conn.commit()
    print(my_cursor.rowcount, "record inserted.")
    
    sql = '''INSERT INTO agenda (meeting_date, presenter_fname, presenter_lname, agenda_item, 
    bullet_point1, bullet_point2, meeting_start_time, item_length, department)
    VALUES ('2022-05-23', 'Gretchen', 'Bleeker', 'Software update', 'All staff should schedule an appt with IT', 
    'Fixes security concern', '10:45', '5 minutes', 'IT')'''
    
    my_cursor.execute(sql)
    conn.commit()
    print(my_cursor.rowcount, "record inserted.")
    conn.close()
    
if __name__ == "__main__":
    main()    
    
