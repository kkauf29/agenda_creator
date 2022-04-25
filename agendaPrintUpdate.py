###
#  Kim Kaufman
#  CSC 217
#  4/4/22
#  This code will print out the rows in the table and update a value

import sqlite3

def main():
    print('connecting to database')
    conn = sqlite3.connect('Agenda_Creator.db')
    my_cursor = conn.cursor()
    query = "UPDATE agenda " \
             + "SET presenter_fname = 'Mary' " \
             + "WHERE agenda_id = 3 "
            
    my_cursor.execute(query)
    conn.commit()
    print(my_cursor.rowcount, "record changed")
    
    
    my_cursor = conn.cursor()
    my_cursor.execute("SELECT * FROM agenda")
    results = my_cursor.fetchall()
    for row in results:
        print(row)
    
            
    conn.close()   
    
if __name__ == "__main__":
    main()    
