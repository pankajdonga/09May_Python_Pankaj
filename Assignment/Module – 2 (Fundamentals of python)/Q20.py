# Q20. Write a Python function that takes a list of words and returns the length of the longest one.

city=["rajkot", "surat", "pune", "faridabad", "prayagraj"]

length=len(city[0])

for i in city:
    all_length = len(i)
    
    if all_length > length:
        longest_length = all_length

if len(i) == longest_length:
    print(f"Longest word in list is {i} with {longest_length} Characters") 






