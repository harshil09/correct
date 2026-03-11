class operator:
    def __init__(self,marks):
        self.marks=marks

    def __gt__(self,a):
        return self.marks>a.marks

n1=operator(89)
n2=operator(98)
print(n1>n2)


##__str__method

class Car:
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return f"{self.name}"

c=Car("a")
print(c)


class a:
    def ss(self):
        print(a)

class b(a):
    def ss(self):
        print(b)

class c(a):
    def ss(self):
        print(c)

def methodf(sound):
    sound.ss()

methodf(b())
methodf(c())