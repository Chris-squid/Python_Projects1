#Parent Class Car, to pass on attributes and methods to Child classes
#Polymorphism example of structure in abstract class, implementaion in other classes
class Car:
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement abstract method")

#1st Child class with 2 attributes     
class Sportscar(Car):
    def drive(self):
        return 'Sportscar driving!'

    def stop(self):
        return 'Sportscar braking!'
#2nd child class
    
class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'

    def stop(self):
        return 'Truck braking!'

cars = [Truck('Bananatruck'),
Truck('Orangetruck'),
Sportscar('Z3')]

for car in cars:
    print (car.name + ': ' + car.drive())
