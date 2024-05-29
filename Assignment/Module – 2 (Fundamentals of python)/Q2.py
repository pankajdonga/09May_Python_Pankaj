# Q2. Write a Python program to get the Factorial number of given number.

n=int(input("Enter any number: "))
i=0
j=1
while i<n:
    i+=1
    j=j*i
print(f"Factorial Value of {n}:", j)
