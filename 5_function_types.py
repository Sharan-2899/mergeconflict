"""
# function without arg and without return
# function with arg and without return
# function without arg and with return
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

# order of arguments

def student_info(name, *subjects, age=18, **details):
    print("Name:", name)
    print("Subjects:", subjects)
    print("Age:", age)
    print("Other Details:", details)

# Calling the function
student_info(
    "Sharan", 
    "Math", "Science", "English",     # *args
    age=20,                           # default argument overridden
    city="Bangalore", college="MIT"   # **kwargs
)



"""  ### function as variable """
def bodhidharma():
    return "vanakam da mapla....china la irunthu"
x=bodhidharma

print(bodhidharma())
print(x())

''' ### function of argument '''
def square(x):
    return x * x

def cube(x):
    return x * x * x

def apply_function(func, value):
    result = func(value)  # call the function passed as argument
    print("Result:", result)

apply_function(square, 5)  # Result: 25
apply_function(cube, 3)    # Result: 27

# function returning another function
def demo():
    return 'hi'

def main():
    print(demo())
    return "hello"

print(main())

#uppercase function call...
def touppercase(func):
    result=func()
    return result.upper()

def greet():
    return "hello world"

result1=touppercase(greet)
print(result1)

# nested function

def outer():
    def inner():
      return "i am inner"
    print(inner())
    return 'i am outer'  
print(outer())  

# nested function

def greet(name):
    def message():
        return "Hello " + name.upper()
    return message()

print(greet("Sharan"))

#################
def outer_function(name):
    def inner_function():
        return f"Hello {name.upper()}"
    return inner_function  # returning the function itself

greet = outer_function("Sharan")  # outer_function returns inner_function
print(greet())  # calling the inner function

##############
def outer(a):
    def inner():
        return a
    return inner()

print(outer("hi"))

####################
def outer(a):
    def inner():
        return a
    return inner

x=print(outer("hi"))
print(x)

####################
def outer(a):
    def inner():
        return a
    return inner



x=outer("hi")
del outer
print(x())

