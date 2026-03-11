def log_decorator(func):
    def wrapper(*args,**kwargs):
        print(args)
        print(kwargs)
        return func(*args,**kwargs)
    return wrapper


@log_decorator
def students(name,age):
    print(f"name is {name} and age is {age}")

students("harshil",age =27)
