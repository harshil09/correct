c=[1,2,3,4,5,6,7]

result= [i for i in c if range(i)]
print(result)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    @property
    def getsalary(self):
        return self.__salary

    @getsalary.setter
    def getsalary(self,value):
        if value>0:
            self.__salary=value
        else:
            return "invalid"

e= Employee("harshil",80000)
print(e.getsalary)
e.getsalary=90000
print(e.getsalary)
e.getsalary=-100
print(e.getsalary)

def funct(n):
    a=0
    temp
    while(n>0):
        lastdigit= n %10
        a=a*10+lastdigit
        n//=10

    if(temp==a):
        return "Its Palindrome number"
    else:
        return "Its not palindrome"



n=123 
temp=n
print(funct(n))

import threading

def task():
    print("this is a simple program")

t1=threading.Thread(target=task)
t1.start()
t1.join()

print("main program ends")