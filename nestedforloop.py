# nested for loop
for i in range(5):
    for j in range(2):
        print(i,j)

# nested for loop
week=0
for i in range(4):
    week=week+1
    day=0
    for j in range(7):
        day=day+1
        print(f"week:{week} --day:{day}")

# nested for loop
week=0
day=0

for i in range(4):
    week=week+1
    for j in range(7):
        day=day+1
        print(f"week:{week} -- day:{day}")  

# nested task1
for i in range(5):
    for j in range(1,6):
        print(j,end="," if j<5 else"")
    
    print()

# nested task1

for i in range(5):
    for j in range(1,6):
        print("*",end="")
    
    print()

# task 3
for i in range(6):
    for j in range(1,i+1):
        print("*",end="")
    
    print() 

# task 4
for i in range(5,0,-1):
    for j in range(i):
       print("*", end='')
    print() 

# task 6

for i in range(5,0,-1):
    for j in range(i):
       print("*", end='')
    print()  


# task 7
rows = 5

for i in range(1,rows+1):
   print(" "*(rows-i)+"*"*(2*i-1))

  
# task 8


      
c=0
for i in range(6):
    for j in range(1,i+1):
        c=c+1
        print(c,end=" ")
    
    print()     

#task 8
c=26
for i in range(5):
    for j in range(5):
        c=c-1
        print(c,end=" ")
    print()  

# Task 9      

x=[10,20,30,42,1,2,3]

y=len(x)

for i in range(y):
    for j in range(1,y-1):
        if x[j] > x[j+1]:
            x[j],x[j+1] = x[j+1],x[j]
print("ascending:",x) 


# task 
c=0
for i in range(6):
    for j in range(1,i+1):
        c=c+1
        print(c,end=" ")
    
    print()   

# task

x=[10,20,30,42,1,2,3]

y=len(x)

for i in range(y):
    for j in range(0,y-1):
        if x[j] > x[j+1]:
            x[j],x[j+1] = x[j+1],x[j]
print("ascending:",x) 

    
# task
for i in range(1,6):
    for j in range(i):
        print("$",end="")
    for j in range(i,6):
        print("*",end="")
    print()     

# task 

row=5

for i in range(1,row+1):
    print(" "*(row-i)+"*"*(2*i-1))
print()    

# task

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for k in range(i-1):
        print("*",end="")   
    print()  

# task
 

for i in range(1,6):
    for j in range(i):
        print(" ",end="")
    for j in range(i,5):
        print("*",end="")
    for k in range(i,6):
        print("*",end="")   
    print()  

# task    
for i in range(1,6):
    for j in range(i,6):
        print("*",end="")     




