def factorial(num):
    f=1
    while(num>=1):
        f=f*num
        num-=1
    return f
        
num=int(input("enter a number="))
print(factorial(num))