'''class new:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def getage(self):
        return self.__age

n1=new("harshil", 20)
print(n1.name)
n1.getage()


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"hello my name is {self.name}")

p1=Person("nirali", 26)
p1.greet()'''


class Employee:
    def __init__(self,name,companyname):
        self.name=name
        self.companyname=companyname

    def show(self):
        print(self.name, self.companyname)

class Child(Employee):
    def __init__(self,name,companyname,language):
        super().__init__(name,companyname)
        self.language=language

    def show(self):
        super().show()
        print(self.language)

c=Child("harshil","hdfc","english")
c.show()
