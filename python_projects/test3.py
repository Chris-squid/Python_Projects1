#import sql for use 
import sqlite3

conn = sqlite3.connect('test3.db')#Create the Connection

with conn:
    cur = conn.cursor()#Create the Table statement to the execute method of cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_Files TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect('test3.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_fileList(col_Files) VALUES (?)",\
                ('information.docx',))
    cur.execute("INSERT INTO tbl_fileList(col_Files) VALUES (?)",\
                ('Hello.txt',))
    cur.execute("INSERT INTO tbl_fileList(col_Files) VALUES (?)",\
                ('myImage.png',))
    cur.execute("INSERT INTO tbl_fileList(col_Files) VALUES (?)",\
                ('myMovie.mpg',))
    cur.execute("INSERT INTO tbl_fileList(col_Files) VALUES (?)",\
                ('World.txt',))
    cur.execute("INSERT INTO tbl_fileList(col_Files) VALUES (?)",\
                ('data.pdf',))
    cur.execute("INSERT INTO tbl_fileList(col_Files) VALUES (?)",\
                ('myPhoto.jpg',))
    conn.commit()
conn.close()
    
    
    


       
