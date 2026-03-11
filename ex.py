from module import *

num1 = int(input("enter a num1:"))
num2 = int(input("enter a num2:"))

print("addition: ", add(num1,num2))
print("mul: ", mul(num1,num2))
print("sub: ", sub(num1,num2))
print("div: ", div(num1,num2))


###MODULE USING ALIAS
import math as m

print("square root of 5 is ", m.sqrt(5))
print("2 to the power 4 is:", m.pow(2,4))


from operator import mod
import math
lis=dir(math)
print(lis)
