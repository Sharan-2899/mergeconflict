x=0
while x < 5:
    print(x)
    y=10
    while y < 15:
        print(y)
        y=y+1
    x=x+1 

# Multiplication Tables

i=1
while i<=10:
    j=1
    while j<=10:
        print(f"{i} x {j} = {i*j}",end="\t")  
        j=j+1
        print()
    i=i+1    

# square
i=1
while i<=5:
    j=1
    while j<=5:
        print("*",end=" ")
        j=j+1
    print()    
    i=i+1      

# left angle triangle  
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

# inverted triangle
i=5
while i>=1:
    j=1
    while j <= i:
        print("*",end=" ")
        j=j+1
    print()
    i-=1              

# right angled triangle

i = 1
while i <= 5:
    j = 1
    while j <= 5 - i:
        print(" ",end=" ")
        j = j + 1
    k = 1
    while k <= i:
        print("*",end=" ")
        k = k + 1
    print()
    i = i + 1  

# centered triangle

i = 1
while i <= 5:
   
    j = 1
    while j <= 5 - i:
        print(" ", end=" ")
        j = j + 1
    k = 1
    while k <= (2 * i - 1):
        print("*", end=" ")
        k = k + 1
    print()
    i = i + 1

# reverse a string

x="hello"
rev =''
l=len(x)-1
while 0 <= l:
    rev=rev+x[l]
    l=l-1
print(rev)

# find the sum of pair of numbers for the given input in the list

# using while loop 

list=[1,2,3,4,5,6,7,8,9,10]
n=int(input("Enter the Number:"))
l=len(list)-1
i=0
while l>=0:
    j=0
    while j<=l:
        if list[i]+list[j]==n:
            print(list[i],list[j])
        j=j+1
    i=i+1
    l=l-1

# using for loop

arr = [1,2,3,4,5,6,7,8,9] 
x = int(input("enter a number: "))

new_arr=[]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==x:
            new_arr=new_arr+[(arr[i],arr[j]),]
print(new_arr)            




    




   
   
 


