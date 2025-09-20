# intersection #it is inplace..which means u need not to open new variable to store updated data

a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
print(a)


#union

a = {1, 2}
b = {2, 3}
print(a.union(b))



#difference()

a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))


print(a | b)
print(a & b)











