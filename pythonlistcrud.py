# ===============================
# Python List Methods Examples
# ===============================

print("\n1. append()")
x = [10, 20]
x.append(30)
print(x)   # [10, 20, 30]

print("\n2. extend()")
x = [1, 2]
x.extend([3, 4, 5])
print(x)   # [1, 2, 3, 4, 5]

print("\n3. insert()")
x = [10, 20, 30]
x.insert(1, 99)
print(x)   # [10, 99, 20, 30]

print("\n4. remove()")
x = [1, 2, 3, 2]
x.remove(2)
print(x)   # [1, 3, 2]

print("\n5. pop()")
x = [10, 20, 30, 40]
print(x.pop())    # 40
print(x.pop(1))   # 20
print(x)          # [10, 30]

print("\n6. clear()")
x = [1, 2, 3]
x.clear()
print(x)   # []

print("\n7. index()")
x = [10, 20, 30, 20]
print(x.index(20))   # 1

print("\n8. count()")
x = [1, 2, 2, 3, 2]
print(x.count(2))   # 3

print("\n9. sort()")
x = [3, 1, 4, 2]
x.sort()
print(x)   # [1, 2, 3, 4]
x.sort(reverse=True)
print(x)   # [4, 3, 2, 1]

print("\n10. reverse()")
x = [1, 2, 3]
x.reverse()
print(x)   # [3, 2, 1]

print("\n11. copy()")
x = [10, 20, 30]
y = x.copy()
y.append(40)
print("x:", x)   # [10, 20, 30]
print("y:", y)   # [10, 20, 30, 40]

# ===============================
# pop() vs remove()
# ===============================

print("\n=== Difference between pop() and remove() ===")
x = [10, 20, 30, 40]
print("Before pop:", x)
print("Popped element:", x.pop())   # removes last
print("After pop:", x)

x = [10, 20, 30, 20]
print("\nBefore remove:", x)
x.remove(20)   # removes first occurrence of 20
print("After remove:", x)
