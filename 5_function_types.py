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