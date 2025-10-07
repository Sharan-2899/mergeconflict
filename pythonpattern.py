n=5
for i in range(1,n+1):
    print("*"*i+"#"*(n-i),end="")
    print()

#Task

count=0
for i in range (5):
    count=count+1
    print("*"*count) 

#Task

n=5
for i in range(1,n+1):
    print("*"*i+"#"*(n-i))
print()

# Mirror for previous

n=5
for i in range(1,n+1):
    print("#"*(n-i)+"*"*i)
print()   


# diamond program
n=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i+"*"*(i-1))

for j in range(n-1, 0, -1):
    print(" "*(n-j)+"*"*j+"*"*(j-1))
print() 

# Hollow square
n = 5
for i in range(n):          
    for j in range(n):     
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
# 'N' shape stars
n = 5
for i in range(n):          
    for j in range(n):     
        if i == j or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# "M" shape stars
n = 5
for i in range(n):         
    for j in range(n):     
        if i == j  and i!=3 or j == 0 or j == n-1 or j==3 and i==1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# "Z" shape stars

n = 5
for i in range(n):          
    for j in range(n):     
        if i == 0 or i == n-1  or i == 1 and j == 3 or i == 2 and j == 2 or i == 3 and j == 1 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()