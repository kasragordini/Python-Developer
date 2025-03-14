# a simple 5 x 5 matrix using nested list comprehension
matrix = [[col for col in range(0,5)] for row in range(0,5)]

for row in matrix:
    print(row)
