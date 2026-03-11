n=int(input("enter a number"))
if n <=0:
    print("invalid entry!!reenter")
else:

    factorial=1
    for i in range(1, n+1):
        factorial = factorial *i;
    print(factorial)



'''while loop'''
num=int(input("enter a number"))
factorial1=1
while(num>1):
    factorial1 = factorial1*num
    num=num-1
print(factorial1)