import math
pi = math.pi

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = radius*2
        else:
            self.diameter = diameter
            self.radius = diameter/2

    def area(self):
        return pi*self.radius**2

    def perimeter(self):
        return 2*pi*self.radius

    def display(self):
        print(f"The value of your circle is {self.area()} and the value of your perimeter is {self.perimeter()}")

choice = input("Enter 1 to calculate using radius and 2 using diameter:")

if choice == "1":
    Radius = float(input("Enter the value of the radius:"))
    circle = Circle(radius=Radius)
elif choice == "2":
    Diameter = float(input("Enter the value of the diameter:"))
    circle = Circle(diameter=Diameter)
else:
    print("Invalid input.")

circle.display()

import math
pi = math.pi

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = radius*2
        else:
            self.diameter = diameter
            self.radius = diameter/2

    def area(self):
        return pi*self.radius**2

    def perimeter(self):
        return 2*pi*self.radius

    def display(self):
        print(f"The value of your circle is {self.area()} and the value of your perimeter is {self.perimeter()}")

choice = input("Enter 1 to calculate using radius and 2 using diameter:")

if choice == "1":
    Radius = float(input("Enter the value of the radius:"))
    circle = Circle(radius=Radius)
elif choice == "2":
    Diameter = float(input("Enter the value of the diameter:"))
    circle = Circle(diameter=Diameter)
else:
    print("Invalid input.")

circle.display()

