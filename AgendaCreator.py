###
#  Kim Kaufman
#  CSC 217
#  4/4/22
#  This file will create the database for the Agenda Creator program

import sqlite3


def main():
    #creates connection object
    conn = sqlite3.connect('Agenda_Creator.db')

    my_cursor = conn.cursor()
    # drops table if it exists
    my_cursor.execute('DROP TABLE IF EXISTS agenda')

    query = "CREATE TABLE agenda (" \
    + "agenda_id INTEGER," \
    + "meeting_date_time DATE," \
    + "presenter_fname TEXT," \
    + "presenter_lname TEXT," \
    + "agenda_item TEXT," \
    + "bullet_point1 TEXT," \
    + "bullet_point2 TEXT," \
    + "item_length TEXT," \
    + "department TEXT," \
    + "PRIMARY KEY('agenda_id' AUTOINCREMENT) " \
    + ")"
        
        
    my_cursor.execute(query) #creates table in Agenda_Creator database
        
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    main()    