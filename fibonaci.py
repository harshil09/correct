num=int(input("enter a no:"))
a=0
b=1
n=0
for i in range(1,num+1):
    print(a)  #0
    n = (a+b)  #0+1=1
    a=b #a=1
    b=n #b=1


'''while loop'''

n1=int(input("enter a no:"))
num1=0
num2=1
i=1
n=0
while(i<=n1):
   
    print(num1)
    n = (num1+num2) 
    num1=num2
    num2=n
    i+=1
    