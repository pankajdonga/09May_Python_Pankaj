 # Q10. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

x=int(input("Enter Value of X: "))
y=int(input("Enter Value of Y: "))

if x == y or x+y == 5 or x-y == 5:
    print("TRUE")
else:
    print("FALSE")