# method 1
def demo():
    x=[10,20,30,40,50,60,70,80,90,100]
    for i in x:
        yield i
print(next(demo()))   
print(next(demo())) 


# method 2
def demo():
    x=[10,20,30,40,50,60,70,80,90,100]
    for i in x:
        yield i
gen=demo()        
print(next(gen))   
print(next(gen)) 

# fibonacci

def fibonacci(n):
    a, b = 0, 1           
    for _ in range(n):
        yield a           
        a, b = b, a + b   

gen = fibonacci(10)
for num in gen:
    print(num)
