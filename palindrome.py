##PALINDRONE USING SLICING
number= str(input("enter a number"))
temp=number[::-1]
print(temp)
if(number==temp):
    print("palindrome")
else:
    print("not palindrome")


#HOW  TO FIND A PALINDRONE NUMBER
number=int(input("enter a num:"))

temp=number
a=0
while(number>0):
            last_digit=number%10
            #print(last_digit)
            a=a*10 + last_digit
            #print(a)  
            number=number//10    
            #print(number)
if(temp==a):
    print("this is a palindrome number")
else:
    print("not an palindrome number")
    


##USING FUNCTION
def palindrome(num):
    a=0
    while(num>0):
        #if(num!=0):
            last_digit=num%10
            #print("last_digit is",last_digit)
            a=a*10+last_digit
            #print(a)
            num=num//10
            #print(num)
    if(temp==a):
            return "number is palindrome"
    else:
        return "not a palindrome"

num = int(input("enter a number"))
temp=num
print(palindrome(num))