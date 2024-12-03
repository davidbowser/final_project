# Author   : David Bowser
# Email    : dbowser@umass.edu
# Spire ID : 34781213

'''
Linear Algebra Calculator
Final Project - CICS 110

'''
import numpy as np

def matrix(rows, columns):
    A = np.round(np.empty((rows, columns)))
    for i in range(rows):
        for j in range(columns):
            A[i][j] = float(input(f'Input element for row {i+1}, column {j+1}:'))
            print()
            print("============================================")
            print()
            print_matrix(A)
            print()
            print("============================================")
            print()
    return A
       

# Produces matrix (with elements) with dimensions that are input. 
# Parameters are number of rows and number of columns
# Returns array representing matrix (list of lists)

def print_matrix(matrix):
    for elem in matrix:
        print(elem)
    return(None)

# Prints matrix, row by row
# Parameter is matrix array
# Returns nothing

def dot():
    rows = int(input('Please give the dimensions of your matrices. # of rows?:'))
    print()
    columns = int(input('# of columns?:'))
    print()
    print('Please give entries for matrix A:')
    print()
    A = matrix(rows, columns)
    print()
    print('Please give entries for matrix B:')
    print()
    B = matrix(rows, columns)
    print()
    print_matrix(np.dot(np.transpose(A), B))
    return(np.dot(np.transpose(A), B))

def scalar_m():
    rows = int(input('Please give the dimensions of your matrices. # of rows?:'))
    print()
    columns = int(input('# of columns?:'))
    print()
    print('Please give entries for matrix A:')
    print()
    A = matrix(rows, columns)
    print()
    c = int(input('Please input your scalar you would like to multiply by:'))
    print_matrix(c * A)
    return(c * A)

def multiply():
    rows = int(input('Please give the dimensions of your matrices. # of rows for matrix A?:'))
    print()
    col_rows = int(input('# of columns for matrix A / rows for matrix B?:'))
    print()
    columns = int(input('# of columns for matrix B?:'))
    print()
    print('Please give entries for matrix A:')
    print()
    A = matrix(rows, col_rows)
    print()
    print('Please give entries for matrix B:')
    print()
    B = matrix(col_rows, columns)
    print()
    print_matrix(np.dot(A, B))
    return(np.dot(A, B))

def addition():
    rows = int(input('Please give the dimensions of your matrices. # of rows?:'))
    print()
    columns = int(input('# of columns?:'))
    print()
    print('Please give entries for matrix A:')
    print()
    A = matrix(rows, columns)
    print()
    print('Please give entries for matrix B:')
    print()
    B = matrix(rows, columns)
    print()
    print_matrix(np.add(A, B))
    return(np.add(A, B))