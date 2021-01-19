#create the Parent class to pass data onto the child class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Child class where data is passed onto
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Chris", "Robinson")
x.printname()
#output of data from both classes
