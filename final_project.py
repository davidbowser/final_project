# Author   : David Bowser
# Email    : dbowser@umass.edu
# Spire ID : 34781213

'''
Linear Algebra Calculator
Final Project - CICS 110

'''
import numpy as np
from sympy import Matrix

def new_matrix(rows, columns):
    A = np.round(np.empty((rows, columns)))
    for i in range(rows):
        for j in range(columns):
            counter = 0
            while counter == 0:
                try:
                    A[i][j] = float(input(f'Input element for row {i+1}, column {j+1}:'))
                    print()
                    counter += 1
                except:
                    print('Invalid matrix entry, please try something else\n')
            print("============================================", end = '\n\n')
            print_matrix(A)
            print("============================================", end = '\n\n')
    return A

# Produces matrix (with elements) with dimensions that are input. 
# Parameters are number of rows and number of columns
# Returns array representing matrix (list of lists)

def print_matrix(matrx):
    for elem in matrx:
        print(elem)
    print()

# Prints matrix, row by row
# Parameter is matrix array A
# Returns nothing

def dot(a = '', b = ''):
    if isinstance(a, np.ndarray):
        if len(a[0]) > 1:
            print('Sorry, this is an invalid matrix to dot product. Dot product is only defined for vectors.\n')
            return(a)
        rows = len(a)
    else:
        rows = input('Please give the dimensions of your vectors. # of rows?:')
        while not rows.isnumeric():
            print('Invalid row input')
            rows = input('# of rows?:')
        rows = int(rows)
        print()
        print('Please give entries for vector a:', end = '\n\n')
        a = new_matrix(rows, 1)
    print('Please give entries for vector b:', end = '\n\n')
    b = new_matrix(rows, 1)
    print(np.dot(np.transpose(a), b)[0][0])
    return('')

# Dots two vectors
# Parameters are vector arrays a and b
# Returns an empty string

def scalar_m(A = ''):
    if not isinstance(A, np.ndarray):
        rows = input('Please give the dimensions of your matrices. # of rows?:\n')
        while not rows.isnumeric():
            print('Invalid row input')
            rows = input('# of rows?:')
        rows = int(rows)
        columns = input('# of columns?:\n')
        while not columns.isnumeric():
            print('Invalid column input')
            columns = input('# of columns?:')
        columns = int(columns)
        print('Please give entries for matrix A:\n')
        A = new_matrix(rows, columns)
        print()
    counter = 0
    while counter == 0:
        try:
            c = float(input('Please input your scalar you would like to multiply by:\n'))
            print()
            counter += 1
        except:
            print('Invalid scalar multiple, please try something else\n')
    print_matrix(c * A)
    return(c * A)

# Multiplies a matrix array by a scalar
# Parameter is matrix array A
# Returns scaled matrix

def multiply(A = '', B = ''):
    if not isinstance(A, np.ndarray):
        rows = input('Please give the dimensions of your matrices. # of rows for matrix A?:\n')
        while not rows.isnumeric():
            print('Invalid row input')
            rows = input('# of rows?:\n')
        rows = int(rows)
    print()
    if (not isinstance(A, np.ndarray)) and (not isinstance(B, np.ndarray)):
        col_rows = input('# of columns for matrix A / rows for matrix B?:\n')
        while not col_rows.isnumeric():
            print('Invalid input')
            col_rows = input('# of columns for matrix A / rows for matrix B?:\n')
        col_rows = int(col_rows)
    elif isinstance(A, np.ndarray):
        col_rows = len(A)
    elif isinstance(B, np.ndarray):
        col_rows = len(B[0])
    print()
    if not isinstance(B, np.ndarray):
        columns = input('# of columns for matrix B?:\n')
        while not columns.isnumeric():
            print('invalid column input')
            columns = input('# of columns for matrix B?:\n')
        columns = int(columns)
    print()
    if not isinstance(A, np.ndarray):
        print('Please give entries for matrix A:\n')
        A = new_matrix(rows, col_rows)
        print()
    if not isinstance(B, np.ndarray):
        print('Please give entries for matrix B:\n')
        B = new_matrix(col_rows, columns)
        print()
    print_matrix(np.dot(A, B))
    return(np.dot(A, B))

# Multiplies two matrices
# Parameters are two matrix arrays A and B
# Returns matrix product

def addition(A = '', B = ''):
    if not isinstance(A, np.ndarray):
        rows = input('Please give the dimensions of your matrices. # of rows?:\n')
        while not rows.isnumeric():
            print('Invalid row input')
            rows = input('# of rows?:')
        rows = int(rows)
        columns = input('# of columns?:\n')
        while not columns.isnumeric():
            print('Invalid column input')
            columns = input('# of columns?:')
        columns = int(columns)
        print('Please give entries for matrix A:')
        print()
        A = new_matrix(rows, columns)
        print()
    else:
        rows = len(A)
        columns = len(A[0])
    print('Please give entries for matrix B:')
    print()
    B = new_matrix(rows, columns)
    print()
    print_matrix(np.add(A, B))
    return(np.add(A, B))

# Adds two matrices
# Parameters are matrix arrays A and B
# Returns sum of two matrices

def solve(A = ''):
    if not isinstance(A, np.ndarray):
        rows = input('Please give the dimensions of your matrices. # of rows?:\n')
        while not rows.isnumeric():
            print('Invalid row input')
            rows = input('# of rows?:')
        rows = int(rows)
        columns = input('# of columns?:\n')
        while not columns.isnumeric():
            print('Invalid column input')
            columns = input('# of rows?:')
        columns = int(columns)
        print('Please give entries for matrix A:\n')
        A = new_matrix(rows, columns)
        print()
    A = Matrix(A)
    A = A.rref()[0]
    A = np.array(A).astype(np.float64)
    print_matrix(A)
    return A

# Solves linear system represented by the matrix
# Parameter is matrix array A
# Returns reduced row echelon form of matrix

def start():
    print('\nHello! Welcome to the David Bowser linear algebra calculator!\nPlease see the following for a list of commands, then type your command')
    A = ''
    while True:
        print(' - dot: dot product two vectors\n - multiply: multiply two matrices\n - add: add two matrices\n - scale: multiply a matrix by a scalar\n - solve: reduce the matrix to reduced echelon form\n - newmatrix - make a new matrix\n - exit: exit the matrix calculator')
        i = input()
        if i in ['dot', 'multiply', 'add', 'scale', 'exit', 'solve', 'newmatrix']:
            if i == 'dot':
                A = dot(A)
            if i == 'multiply':
                if not isinstance(A, np.ndarray):
                    A = multiply(A)
                else:
                    j = input("Type 'left' to left multiply or 'right' to right multipy your existing matrix\n")
                    if j in ['left', 'right']:
                        if j == 'right':
                            A = multiply(A)
                        if j == 'left':
                            A = multiply('',A)
            if i == 'scale':
                A = scalar_m(A)
            if i == 'add':
                A = addition(A)
            if i == 'solve':
                A = solve(A)
            if i == 'newmatrix':
                rows = input('Please give the dimensions of your matrices. # of rows?:\n')
                while not rows.isnumeric():
                    print('Invalid row input')
                    rows = input('# of rows?:')
                rows = int(rows)
                columns = input('# of columns?:\n')
                while not columns.isnumeric():
                    print('Invalid column input')
                    columns = input('# of columns?:')
                columns = int(columns)
                print('Please give entries for matrix A:\n')
                A = new_matrix(rows, columns)
            if i == 'exit':
                print('Thank you for using the David Bowser linear algebra calculator, and have a nice day!')
                exit()
            print('Are there any other functions you would like to do to this matrix?')
        else:
            print('Sorry, that is an invalid command. Please try something else')
            
# Runs interface to navigate calculator
# No parameters
# Returns nothing

start()