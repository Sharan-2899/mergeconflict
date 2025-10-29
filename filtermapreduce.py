from functools import reduce

numbers = [2, 4, 5, 6]
squared_filtered = list(filter(lambda x: x > 20, map(lambda n: n**2, numbers)))
print("Squares > 20:", squared_filtered)

nums = [1, 2, 3, 4, 5]
concatenated = reduce(lambda a, b: a + b, map(str, nums))
print("Concatenated string:", concatenated)

data = [10, 20, 30, 40, 50]
filtered = list(filter(lambda x: x > 25, data))
product = reduce(lambda a, b: a * b, filtered)
print("Numbers >25:", filtered)
print("Product of numbers >25:", product)

marks = [45, 78, 89, 32, 56, 90]
passed = list(filter(lambda m: m >= 50, marks))
grace_marks = list(map(lambda m: m + 5, passed))
print("Marks >= 50:", passed)
print("Marks after grace:", grace_marks)

nums_list = [1, 2, 3, 4, 5, 6, 8]
even_sum = reduce(lambda a, b: a + b, filter(lambda x: x % 2 == 0, nums_list))
print("Sum of even numbers:", even_sum)

words = ["apple", "is", "a", "tasty", "fruit"]
upper_filtered = list(filter(lambda w: len(w) > 4, map(lambda w: w.upper(), words)))
print("Uppercase words longer than 4 letters:", upper_filtered)
