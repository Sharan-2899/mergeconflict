# a while loop is a control flow statement . used to repeat to a code as long as a condition is true ( infinite loop )

# while loop

i=1
while 10 == 10:
    print("hello world")
    if i == 3:
        break
    i+=1

# while loop

n=5
while True:
    print(n)
    if n == 50:
        break
    n+=5 
print()      

# while loop(increment)

n=0
while n<50 :
    n+=5 
    print(n)
print()

# while loop (decrement)    

n=100
while n>0:
    n-=1
    if n%3==0 and n%5==0:
        print(n)
        n-=1
   
# reverse a string using while loop

name="Harry"

rev=" "

i=len(name)-1

while i>=0:
    rev = rev + name[i]
    i-=1
print(rev)  

# check panlindrome:

name="Harry"

rev=" "

i=len(name)-1

while i>=0:
    rev = rev + name[i]
    i-=1
if name == rev:
    print("it's palindrome")
else:
    print("not palindrome")    


# check palindrome  # method 2

name= input()
f=0
l=len(name)-1

while f < l:
    if name[f] != name[l]:
        print('not palindrome')
        break
    f+=1
    l-=1
else:
    print("palindrome")    

# check palindrome  # method 2

name= input()
f=0
l=len(name)-1

while f < l:
    if name[f] != name[l]:
        print('not palindrome')
        break
    f+=1
    l-=1
else:
    print("palindrome")       

# check palindrome in list
        
words = ["madam", "hello", "level", "world", "noon"]

i = 0
while i < len(words):        
    word = words[i]
    rev = ""
    j = len(word) - 1         
    
    while j >= 0:
        rev = rev + word[j]
        j -= 1

   
    if word == rev:
        print(word, "→ Palindrome")
    else:
        print(word, "→ Not Palindrome")

    i += 1

