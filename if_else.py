num = int(input("enter a num: "))

if num%2==0:
    print("the num is even")
else:
    print("the num is odd")    

# if else (task 1)

if num%2==1:
    print("the num is odd")
else:
    print("the num is even")

# if else (task2)

if num>20 and num<=25:
    print("the num is greater than 20")
elif num>0 and num<=20:
    print("the given number is in range")
else:
    print("out of range! still a valid number")    

# if else (task 3)

#question 1 

number=int(input("enter a number: "))    
if number%5==0:
    print("the num is divisible by 5")
else:
    print("the number is not divisible 5")  

#question 2

age=int(input("enter a age: "))

if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")   

# question 3

num1=int(input("enter a num: "))  

if  num1%3==0:
    print("the num is multiple by 3")  
else:
    print("the num is not multiple by 3")

# question 4

input1=str(input("enter a alphabet: "))

if input1 in ['a','e','i','o','u']:
    print("the entered alphabet is vowel")
else:
    print('the entered alphabet is consonant')

# question 5

enterpassword=input("enter a password: ")
password="1234@google"

if enterpassword==password:
    print("entered password id correct")
else:
    print("invalid password")    

# question 6

age=int(input("enter your age: "))  

if age>=18:
    print("your'e an adult")

elif age<0:
    print("invalid age")

else:
    print("your'e an kid")

# question 7

totalclass=int(input("enter a num: "))  
attendedclass=int(input("enter a num: "))

attendance=(attendedclass/totalclass)*100

if attendance>=75:
    print("your'e allowed to sit in exam hall")
else:
    print("your'e not allowed to sit in exam hall")    

# question 8
look=str(input("watch for the signal and respond and move according: "))  

if look=="red":
  print("stop! and wait")

elif look=="yellow":
    print("get ready!")

elif look=="green":
    print("Go!")

else:
    print("************************************************************")
    print("Watch carefully ! your'e not paying attention to the signal!")  
    print("************************************************************")  

