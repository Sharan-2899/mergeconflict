# enumerate

x=[10,20,30,40]

print(list(enumerate(x)))

for i in enumerate (x):
    print(i)

# reversed sort

x=sorted([10,20,30,40,50],reverse=True)
print(x)  

# sorted lambda function

x=sorted({0:1,1:5,2:3}.items(),key= lambda x: x[1])
print(x)

# zip

x=list(zip([1,2],[3,4]))  
print(x)

#eval

x=eval("1 + 2")    
print(x)

