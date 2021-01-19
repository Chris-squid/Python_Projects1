#create the Parent class to pass data onto the child class
class Fruit:
  def __init__(self):
    self.name = "Fruit"
#Child classes where data is passed onto
class Hard(Fruit):
  def __init__(self):
    self.name = "Apple"
    self.color = "Red"
    self.taste = "Sweet"


class Soft(Fruit):
  def __intit__(self):
    self.name = "Banana"
    self.smell = "Fragrant"
    self.genus = "Musaceae"
#output of data from both classes
