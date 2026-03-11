def prime_number(number):
    if number<=1:
        return "invalid entry"
    elif(number>=1):
        for i in range(2, number+1):
            if number%i == 0:
                return "not a prime number"
            else:
                return "prime number"

number=int(input("enter a number="))
print(prime_number(number))