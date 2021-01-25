class Parent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname


    def printname(self):
      print(self.firstname, self.lastname)

#use the parent class to create an object, and then execute the printname method:


class Child(Parent):
    def __init__(self, fname, lname):
        Parent.__init__(self, fname, lname)


x = Child("John", "Doe")
x.printname()
   

