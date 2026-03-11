


def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return (num*factorial(num-1))
num=5
print(factorial(num))



def prime_number(num1):
    if num1<=1:
        return "invalid entry"

    elif(num1>=1):
        for i in range(2, num1+1):
            if num1%i==0:
                return "not a prime number"
        
               
            else:
                return "prime number"
            
num1=int(input("enter a number"))
print(prime_number(num1))
