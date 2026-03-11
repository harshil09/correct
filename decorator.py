def my_decorator(func):
    def wrapper(name):
        print("hello world")
        func(name)
        print("hi")
    return wrapper

@my_decorator
def hello(name):
    print("hello "+ name)
hello("harshil")


def my_name(name1):
    def greeting(name):
        print(f"hello {name}")
        name1(name)
        print("hi")
    return greeting

@my_name
def hi(name):
    print("hi"+ name)
hi("nirali")    

