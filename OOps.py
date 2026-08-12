# n=int(input("enter number:"))
# if n<10 and n>5:
#     raise ValueError("enter corect value")
#     print(n)

# class details:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def info(self):
#         print(f"{self.name} is {self.age} years old.")

# det1=details("sai", 20)
# det1.name="nanni"

# det2=details("nani",25)
# det2.age=30

# det1.info()
# det2.info()

# def greet(fx):
#     print("hello")
#     fx()

# @greet
# def hello():
#     print("hello world")

# hello()

import logging 
def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} returned {result}")
        return result
    return decorated

# @log_function_call
def add(a, b):
    return a + b

log_function_call(add)(5, 3)
