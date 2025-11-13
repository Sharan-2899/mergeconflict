# 1.	Create a list of squares for numbers 1 to 15 using list comprehension.
squares=[i*i for i in range(1,16)]
print(squares)

# 2.	Write a lambda function to check whether a number is even or odd.
o_or_e=lambda n: "Even" if n%2==0 else "odd"
print(o_or_e(7))
print(o_or_e(10))

# 3.	Use map() to convert all names in a list to uppercase.
names=['sharan','rubin','bala','ravi']
upper_names=list(map(str.upper,names))
print(upper_names)

# 4.	Use filter() to find all numbers divisible by both 3 and 5 in a list.
num=list(range(1,101))
divisible=list(filter(lambda x: x%3 ==0 and x%5==0,num))
print(divisible)

# 5.	Use reduce() to calculate the product of all elements in a list.
from functools import reduce
nums=[1,2,3,4,5]
sum=reduce(lambda a,b:a+b,nums)
print(sum)

# 6.	Write a Python function that takes a list and returns a new list with only unique elements.
def unique_elements(lst):
    return list(set(lst))
numbers = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(numbers)
print(result)

# 7.	Print all elements of a tuple using a for loop.
tuple1=(10,20,30,40,50)
for i in tuple1:
    print(i)

# 8.	Write a function to count how many even numbers are present in a tuple.  
def count_even_numbers(cen):
    count = 0
    for num in cen:
        if num % 2 == 0:
            count += 1
    return count
numbers = (1, 2, 3, 4, 5, 6, 8)
result = count_even_numbers(numbers)
print("Number of even numbers:", result)

# 9.	Use filter() with lambda to find names that start with the letter “A”.
names=['Archie','Betty','Veronica','Jughead','Ambrose','Agito','Max','andrea pirlo','andrew']
new_names=list(filter(lambda n: n.startswith('A') or n.startswith('a'),names))
print(new_names)

# 10.	Write a for loop to reverse a given string without using slicing.
def reverse_string(s):
    rev=" "
    for ch in s:
        rev = ch + rev
    return rev
print(reverse_string("Harry Potter")) 

# 11.	Write code to show the difference between shallow copy and deep copy on nested lists.
import copy

stable=[[1,2],[3,4]]
shallow=copy.copy(stable)
deep=copy.deepcopy(stable)

stable[0][1]=3
print('stable',stable)
print('shallow',shallow)
print('deep',deep)

# 12.	Write a function to find the factorial of a number using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

result=factorial(5)
print("factorial of 5 is",result)

# 13.	Demonstrate that two variables pointing to the same list share the same memory address.
a = [1,2,3]
b = a
print(id(a) , id(b))
print(a is b)

# 14.	Convert a list of temperatures in Celsius to Fahrenheit using map() and lambda.
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

# 15.	Use filter() and lambda to remove all negative numbers from a list.
nums=[-2,3,-4,5,-6,7,-8]
not_negative=list(filter(lambda x: x>=0 , nums))
print(not_negative)



