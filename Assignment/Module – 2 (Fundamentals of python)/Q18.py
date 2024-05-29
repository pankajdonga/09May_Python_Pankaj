"""Q18. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is 
less than 3, leave it unchanged."""

test=input("Enter an any word(minimum 3 latter required): ")

length=len(test)

if length < 3:
    print(test)
elif length >= 3:
    print(test + "ing")
elif test[-3:] == "ing":
    print(test.replace("ing", "ly"))



