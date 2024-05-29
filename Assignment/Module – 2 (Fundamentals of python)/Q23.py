 # Q23. Write a Python function to insert a string in the middle of a string.

test=input("Enter a String: ")

add_str=input("Enter a string to add string in middle of origional string: ")

x=test.find(" ")

new_str=test[:x] + " " + add_str + " " + test[x+1: ]

print(new_str)