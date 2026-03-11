def addd(num1,num2):
    return num1+num2
    
lambda_function=lambda num1,num2:num1+num2

print(addd(2,5))
print(lambda_function(3,5))


def palindrome(num):
    a=0
    while(num>0):
        #if(num!=0):
            last_digit=num%10
            print("last_digit is",last_digit)
            a=a*10+last_digit
            print(a)
            num=num//10
            print(num)
    if(temp==a):
            return "number is palindrome"
    else:
        return "not a palindrome"

num = int(input("enter a number"))
temp=num
print(palindrome(num))


