a=[1,2,3,4,5]
n=1
rotate=a[n:]+a[:n]
print(rotate)


b=[1,2,3,4,5]
x=2
shift=b[-x:]+b[:-x]
print(shift)


arr=[1,2,3,4,5]
n=2
for i in range(2):
    cut=arr.pop()
    arr.insert(0,cut)
print(arr)

a=[1,2,3,4,5]
len=len(a)
i=int(input("Enter the number of rotations: "))
for i in range(i):
    temp=a[0]
    for j in range(len-1):
        a[j]=a[j+1]
    a[len-1]=temp
print(a)