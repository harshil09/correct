prime_number = int(input("enter a number to find prime number:"))


for i in range(2, prime_number):
    if prime_number%i==0:
        print("not a prime number")    
        break
else:
    print("prime number")
           
        
'''while loop '''

num=int(input("enter a number to find prime number:"))

i=2
while(i<num):
    if num % i == 0:
        print("not a prime number")
        break
    i=i+1
else:
    print("prime")
        