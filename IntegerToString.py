a=int(input("enter a integer value = "))
b=str(a)
print(b)
try:
    c=a+b
    print(c)
except TypeError:
    print("Cannot add String and integer")