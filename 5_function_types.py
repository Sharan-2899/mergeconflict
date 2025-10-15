"""
# function without arg and without return
# function with arg and without return
# function without arg and with arg
# function with arg and with return
 
"""

# positional arg
'''These are arguments passed in the same order as the parameters in a function definition.'''
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Sharan", 20)


# keyword arguments
'''These are arguments passed with parameter names, so the order doesn’t matter.'''
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(name="Sharan", age=20)
student("Sharan", age=20)   # keyword args followed positional arguments

# default arguments
'''If you don’t provide a value for a parameter, Python will use its default value.'''
def greet(name, message="Good Morning"):
    print(f"Hello {name}, {message}!")

greet("Sharan")
greet("Riya", "Welcome!")

# Variable-length Arguments – *args
'''Used when you don’t know how many positional arguments you’ll get.'''
def add(*numbers):
    print(sum(numbers))

add(1, 2)
add(3, 4, 5, 6)

#Keyword Variable-length Arguments – **kwargs
'''Used when you don’t know how many keyword arguments you’ll get.'''
def info(**details):
    print(details)

info(name="Sharan", age=20, city="Bangalore")

# Mixing Argument Types
'''You can mix them, but order must be:  Positional → *args → Default → **kwargs  '''

def profile(name, *hobbies, age=18, **info):
    print(name, hobbies, age, info)

profile("Sharan", "Cricket", "Coding", age=20, city="Bangalore", college="MIT")





