# Q61. Write a Python program to calculate the area of a parallelogram.

def parallelogram(base,height):

    parallelogram=base*height

    print(f'Area of parallelogram: {parallelogram}')

base=int(input('Enter Value Of a Base: '))
height=int(input('Enter Value Of a Height: '))

parallelogram(base,height)

