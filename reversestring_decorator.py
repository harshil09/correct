def decorator(func):
    
    def a(name):
        print(f"hello {name} this is before reversing")
        temp=name[::-1]
        print(f"hello {temp} this is after reversing")
        func(name)
        #
        #
        #print(f"hello {temp} this is after reversing")
    return a

@decorator
def calling_function(name):
    print("string already printed in reversed order")
name=str(input("enter a name="))
calling_function(name)