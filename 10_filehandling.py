file=open('filehandling.txt','w')
file.write("hello i'm gusion")
file.close()

file=open('filehandling.txt','r')
print(file.read())
file.close()


file2=open('12_filehandling.txt','w')
file2.write("i'm a gusion player....and he is my favourite")
file2.close()

file2=open('12_filehandling.txt','w')
file2.write("Hi im gusion")
file2.close()

file2=open('12_filehandling.txt','a')
file2.write('\ni managed to grind hard with gusion and mastered how to use the hero')
file2.close()

file2=open('12_filehandling.txt','r')
print(file2.readlines())
file2.close()

with open('12_filehandling.txt','r') as file2:
    print(file2.read())


with open('12_filehandling.txt','w') as file2:
    print(file2.write('...........'))    

with open('12_filehandling.txt','a') as file2:
    file2.write("\nnow i can use gusion even as a roam hero...and carry the team")

file2=open('12_filehandling.txt','a')
x=["\ngusion","\tfanny","\tclaude","\tyi sun shin"]
file2.writelines(x)
file2.close()

# read
file2=open('12_filehandling.txt','r')
print(file2.read())
file2.close()

# readline
file2=open('12_filehandling.txt','r')
print(file2.readline())
file2.close()

# readlines
file2=open('12_filehandling.txt','r')
print(file2.readlines())
file2.close()

# u can also give how many characters u wanna read by giving numbers 
file2=open('12_filehandling.txt','r')
print(file2.readline(13))
file2.close()

#tell & seek
file2 = open('12_filehandling.txt', 'r')
data = file2.readline(13)
print("Data read:", data)
print("Current position (using tell):", file2.tell())
file2.seek(0)
print("Pointer moved back to:", file2.tell())
print("Reading again after seek:", file2.readline())
file2.close()

#r+

file3 = open('12_filehandling.txt', 'r+')
data = file3.readline(13)
print("Data read:", data)
print("Current position:", file3.tell())

file3.seek(0, 2)  
file3.write("\nAdded using r+ mode")
file3.seek(0)
print("Reading file after writing with r+:")
print(file3.read())

file3.close()

#w+

file3 = open('12_filehandling.txt', 'r')
data = file3.read()
file3.close()

file3 = open('12_filehandling.txt', 'w+')
file3.write(data) 
file3.write("\nAdded using w+ mode")
file3.seek(0)
print("Reading file after writing with w+:")
print(file3.read())

file3.close()





