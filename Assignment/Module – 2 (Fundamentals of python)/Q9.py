# Q9. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

x=int(input("Enter Valur for X: "))
y=int(input("Enter Valur for Y: "))
z=int(input("Enter Valur for Z: "))

if x == y or x == z or y == z:
    print("Sum of X + Y + Z= 0")
else:
    print("Sum of X + Y + Z= ", x+y+z)