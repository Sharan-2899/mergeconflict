# Python String Built-in Methods with Examples

s = "hello world"
t = "Python123"
u = "   spaced text   "
v = "ABC"
w = "123"
x = "hello\nworld"

def show(num, desc, result):
    print(f"{num}. {desc} -> {result}")
    print("-" * 50)

show(1, "capitalize()", s.capitalize())
show(2, "casefold()", "HELLO".casefold())
show(3, "center(20, '-')", s.center(20, "-"))
show(4, "count('l')", s.count("l"))
show(5, "encode()", s.encode())
show(6, "endswith('world')", s.endswith("world"))
show(7, "expandtabs(4)", "a\tb\tc".expandtabs(4))
show(8, "find('world')", s.find("world"))
show(9, "format()", "My name is {}".format("Sharan"))
data = {"name": "Sharan", "age": 21}
show(10, "format_map(data)", "My name is {name}, age {age}".format_map(data))
show(11, "index('world')", s.index("world"))
show(12, "isalnum()", ("Python123".isalnum(), "Python 123".isalnum()))
show(13, "isalpha()", "Python".isalpha())
show(14, "isascii()", "abc123".isascii())
show(15, "isdecimal()", "123".isdecimal())
show(16, "isdigit()", "123".isdigit())
show(17, "isidentifier()", ("name1".isidentifier(), "1name".isidentifier()))
show(18, "islower()", s.islower())
show(19, "isnumeric()", "123".isnumeric())
show(20, "isprintable()", ("hello".isprintable(), "hello\n".isprintable()))
show(21, "isspace()", "   ".isspace())
show(22, "istitle()", "Hello World".istitle())
show(23, "isupper()", "HELLO".isupper())
show(24, "join()", ",".join(["a", "b", "c"]))
show(25, "ljust(15, '-')", s.ljust(15, "-"))
show(26, "lower()", v.lower())
show(27, "lstrip()", u.lstrip())
table = str.maketrans("aeiou", "12345")
show(28, "translate(maketrans())", "hello".translate(table))
show(29, "partition(' ')", s.partition(" "))
show(30, "removeprefix('Python')", "Python3".removeprefix("Python"))
show(31, "removesuffix('.py')", "hello.py".removesuffix(".py"))
show(32, "replace('world', 'Python')", s.replace("world", "Python"))
show(33, "rfind('l')", s.rfind("l"))
show(34, "rindex('l')", s.rindex("l"))
show(35, "rjust(15, '-')", s.rjust(15, "-"))
show(36, "rpartition(' ')", s.rpartition(" "))
show(37, "rsplit(' ', 1)", s.rsplit(" ", 1))
show(38, "rstrip()", u.rstrip())
show(39, "split(' ')", s.split(" "))
show(40, "splitlines()", x.splitlines())
show(41, "startswith('hello')", s.startswith("hello"))
show(42, "strip()", u.strip())
show(43, "swapcase()", "Hello".swapcase())
show(44, "title()", s.title())
show(45, "upper()", s.upper())
show(46, "zfill(5)", "42".zfill(5))
