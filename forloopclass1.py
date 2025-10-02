# task1

for i in range(len("hello")):
    for j in range(len("hi")):
        print(i,j)

# task2

x=['1','2','hi','hello','12','ddhe','ss','sss','w22','ss']
y=0

for i in x:
    y=y+1
    if y%2==0:
        print(y)


# task2

x={'1','2','hi','hello','12','ddhe','ss','sss','w22','ss'}
y=0

for i in x:
    y=y+1
    if y%2==0:
        print(y)


# task3


x={"hell0","hi","python","html"} 

for i in x:
    print(i)

# task 4   

person = {"name": "Alice", "age": 25, "city": "Delhi"}

for key in person:
    print(key, ":", person[key])

# task 5


person = {"name": "Alice", "age": 25, "city": "Delhi"}
print(person.items())

for key in person.items():
    print(person)  



# enumerate  

x=['harry','hermoine','ron','ginny','hagrid']  

for index,i in enumerate(x,start=1):
    print(index,i)


# pattern basics

for i in range(3):
    for j in range (4):
       print("*",end=" ")
    print()  

# task

x=0
for i in range(0,101):
    x+=1
    if x%3==0 and x%7==0:
       print(i,"the num is divisible by 3 and 7")
    else:
        print(i,"not divisible by 3 and 7")   

# task


for i in range(1, 101):  
    if i % 3 == 0 and i % 7 == 0:
        print(i, "is divisible by 3 and 7")


# task

for i in range(50,0,-1):
    if i%2 != 0:
        print(i,"is odd number")  

# task


odd_numbers=[]
for i in range(50,0,-1):
    if i%2 != 0:
        odd_numbers.append(i)
print(odd_numbers,"is odd number")        


# task


enter = int(input("enter a number: "))
print(f"****{enter} Tables*****")
for i in range(1, 11):
   print(enter, "x", i, "=", enter * i)


# task

x=[1,2,3,4,5,6,7,8,9,10]
sum=0

for i in x:
    sum=sum+i
print(sum)

# task

numbers = [4, 17, 2, 89, 33]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)


# task
numbers = [12, 45, 2, 34, 67, 89, 34]

largest = second_largest = float('-inf')  # start with very small numbers

for num in numbers:
    if num > largest:
        second_largest = largest  # previous largest becomes 2nd largest
        largest = num             # update largest
    elif num > second_largest and num != largest:
        second_largest = num      # update 2nd largest if num is in between

print("Second largest number is:", second_largest)

# task
x=[10,20,30,40,50,33,22,66,11,77]
first=float('-inf')
second=float('-inf')


for i in x:
    if i > first:
        second = first
        first = i
    elif first > i > second:
        second = i  

print("second largest is :",second)  
  

    


 


   