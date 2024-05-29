# Q3. Write a Python program to get the Fibonacci series of given range.

n=int(input("Enter Any number to get Fibonacci series: "))
j=0
k=1
l=0
for i in range(n):
    print(l, end=" ")
    j=k
    k=l
    l=k+j


    
