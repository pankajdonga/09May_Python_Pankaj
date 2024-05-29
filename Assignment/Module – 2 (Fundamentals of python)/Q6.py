# Q6.  Write python program that swap two number with temp variable and without temp variable.

print("=== Swaping Number With using temp variable ===\n")
a=10
b=20
print("Value of A Before Swap: ", a)
print("Value of B Before Swap: ", b)

c=a
a=b
b=c
print("\n==========================\n")
print("Value of A After Swap: ", a)
print("Value of B After Swap: ", b)


print("\n=== Swaping Number Without using temp variable ===\n")
x=50
y=60

print("Value of X Before Swap: ", x)
print("Value of Y Before Swap: ", y)

x,y=y,x

print("\n==========================\n")
print("Value of X After Swap: ", x)
print("Value of Y After Swap: ", y)

