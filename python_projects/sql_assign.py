import sqlite3

peopleValues = (('Ron', 'obvious', 42,), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite.connect('C:/Users/15039/OneDrive/Desktop/test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FisrtName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)",
                  peopleValues)

# select all first and last names from people over 30
    c.execute("SE:ECT FirstName, LastName FROM People WHERE Age > 30")
    for row in c.fetchall():
        print (row)
