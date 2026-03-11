class hi:
  
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("hello my name is", self.name)

p1=hi("harshil",20)
p1.greet()


class mathh:
    def add(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b

m1=mathh()
print(m1.add(5,4))
print(m1.sub(6,5))


class details:
    def __init__(self, animal, group):
        self.animal=animal
        self.group=group

d=details("crab", "Crustaceans")
print(d.animal, "belong to the group of ", d.group)


class new:
    @classmethod
    def show(cls):
        print("hi this is a method")

n1=new()
