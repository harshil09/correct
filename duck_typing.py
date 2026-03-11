class Dog:
    def sound(self):
        print("it barks")

class Cat:
    def sound(self):
        print("meow")


def same_method(animal):
    animal.sound()

same_method(Dog())
same_method(Cat())



"""class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"name is {self.name} and age is {self.age}")

class B(A):
    def __init__(self,name,age,language):
        super().__init__(name,age)
        self.language=language

    def show(self):
        super().show()
        print("language used is{self.language}")

b=B("harshil",23,"english")
b.show()
"""

"""class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"{self.name} and {self.age}")

class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks

    def display(self):
        super().display()
        print(f"{self.marks}")

c=Student("harshil",23,34)
c.display()
        """

####MULTILEVEL INHERITANCE
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printinfo(self):
        print(f"{self.name},{self.age}")

class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    
    def printinfo(self):
        super().printinfo()
        print(f"{self.salary}")

class Manager(Employee):
    def __init__(self,name,age,salary,department):
        super().__init__(name,age,salary)
        self.department=department
    
    def printinfo(self):
        super().printinfo()
        print(f"{self.department}")


m=Manager("harshil",22,2000,"claims")
m.printinfo()

    

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(B):
    def show(self):
        print("C")


c=C()
c.show()