# Author   : David Bowser
# Email    : dbowser@umass.edu
# Spire ID : 34781213

'''
Linear Algebra Calculator
Final Project - CICS 110

'''


def matrix(rows, columns):
    matrix = []
    one_row = []
    for i in range(columns):
        one_row.append('X')
    for i in range(rows):
        matrix.append(one_row)
    return(matrix)

# Produces empty matrix with dimensions that are input. 
# Parameters are number of rows and number of columns
# Returns list of lists (empty matrix)

def print_matrix(matrix):
    for elem in matrix:
        print(elem)
    return(None)

# Prints matrix 
# Parameter is matrix
# Returns nothing

def input_matrix(element, row, column, matrix):
    matrix[row][column] = element
    return(matrix)

# Inserts some element into a given coordinate.
# Parameters are element, row, column, matrix. 
# Returns new matrix

def make_matrix():
    i = int(input("How many rows?:"))
    j = int(input("How many columns?:"))
    A = matrix(i,j)
    print_matrix(A)
    for m in range(i):
        for n in range(j):
            a = input("What element would you like in row "+str(m+1)+" column "+str(n+1)+"?:")
            input_matrix(a, m, n, A)
    return(A)

# Makes matrix with elements in each entry
# No parameters
# Returns matrix A

A = matrix(3, 4)
print_matrix(A)
A = input_matrix(1, 2, 2, A)
print_matrix(A)