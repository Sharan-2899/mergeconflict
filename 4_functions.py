'''Function is a block of reusable code performs specific task'''
# reusability
# maintainability
# readability
# efficiency
# abstraction

''' Syntax
  def demo (parameter):
      print("hello")
  demo()    
'''
# armstrong number

def armstrong(num):

    num_str=str(num)

    digits=len(num_str)

    count=0

    for digit in num_str:
        count+=int(digit)**digits

    if num == count:
        print("armstrong number")
    else:
        print("not armstrong") 
armstrong(153)        

# function
def add():
    x=int(input())
    y=int(input())
    print(x+y)
def sub():
    x=int(input())
    y=int(input())
    print(x-y)
def mul():
    x=int(input())
    y=int(input())
    print(x*y)
def div():
    x=int(input())
    y=int(input())
    print(x/y)            

add()
sub()
mul()
div()



