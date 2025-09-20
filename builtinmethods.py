# name="Harry potter"

# print(name.find("potter"))
# print(name.index("o"))
# print(name.replace("p","P"))
# print(name.count("t"),name.count("r"),sep=",")

# fruitshop="apple banana cherry".split()
# print(fruitshop)
# print("-".join(fruitshop))

# padded_strip="  hello  "
# print(padded_strip.strip())
# print(padded_strip.lstrip())
# print(padded_strip.rstrip())
# name="Hi sarath"
# print(name[::-1])
# name="hello world"
# print(name[-1:-12:-1])
# print(name[0:-1])

# x="hello python"
# print(x[0:12:2])
# print(x[1:8:6])
# print(x[-4:-12:-7])
# print(x[-2:-12:-3])
# print(x[-1:-7:-1])
# print(x[-1:-12:-5])
# print(x[8:10])
# print(x[-10:-13:-1])
# print(x[2:5])



# content="my name is {} and my age is {}"

# print(content.format("sarath",25))


# name="sarath"
# age=25

# print(f"my name is {name} and my age is {age}")


# name="sarath is my friend"
# print(name.split())


name="abcdefghijklmnopqratuvwxyz"
print(name.upper())
print(name)
name2=name.upper()
print(name2)
print(name2)

print(name2.lower())
print(name.title())
print(name.capitalize())
print("HellO I'm Harry Potter".swapcase())
print("HellO I'm Harry Potter".title())
print("hello,im,harry,potter".split(","))
print("")
print("".join(['hello','im','harry']))

x="Hello im harry Hello im ron Hello im hermoine"
print(x.replace("Hello","Hi",3))

x="Hello I'm Harry potter Welcome to Hogwarts"
print(x.find("H",1,12))
print(x.index("potter"))

#right index
print(x.rfind("e"))

print(x.isupper())
print(x.islower())

x="Hello I'm Harry potter Welcome to Hogwarts"
print(x.find("H",1,12))
print(x.index("potter"))

print(x.isupper())
print(x.islower())
print(x.isalpha())
print(x.isalnum())
print(x.istitle())
print(x.count("e"))


myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)
