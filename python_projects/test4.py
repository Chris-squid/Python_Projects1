#import sql for use 
import sqlite3

conn = sqlite3.connect('test4.db')#Create the Connection

with conn:
    cur = conn.cursor()#Create the Table statement to the execute method of cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_Files TEXT)")
    conn.commit()

conn = sqlite3.connect('test4.db')

#Creating Tuple for fieList names
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg',)


# loop through each object in tuple to find the .txt names to add to DB
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_Files(col_Files) VALUES (?)", (x,))
            print(x)
conn.close()


