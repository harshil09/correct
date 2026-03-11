class Animal:
    def sound(self):
        print("animal sound")

class Dog(Animal):
    def sound(self):
        print("bark")

class Cat(Animal):
    def sound(self):
        print("m")

for animal in [Dog(), Cat()]:
    print(animal.sound())



class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*2

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    
    def area(self):
        return 0.5*self.base*self.height


shapes=[Circle(5), Triangle(4,5)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: Area={shape.area()}")
