'''
def logger(func):
    def wrap():
        print("before a function runs")
        func()
        print("after a function runs")
    return wrap

@logger
def greet():
    print("hello python")
greet()
'''

from textwrap import wrap


def generic(func):
    def wrap(*args,**kwargs):
        print(f"{args} and {kwargs}")
        func(*args, **kwargs)
    return wrap

def add(a,b,name):
    print(f"a is {a} b is {b} and name is {name}")

add(2,3, name="harshil")


###FUNCTION USING ARGS
def using_args(func):
    def wrapp(*args):
        print(f"{args}")
        func(*args)
    return wrap

def passing_values(a,b,c,d,e,f,g):
    print(f"values are {a}, {b}, {c}, {d}, {e}, {f}, {g}")
passing_values(12,23,43,45,56,67,68)

