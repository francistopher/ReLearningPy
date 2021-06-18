from random import randint

def get_2d_matrix(rows, columns):
    ''' rows=number of rows, columns= number of columns'''

    matrix = [[x for x in range(columns)] for y in range(rows)]
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            matrix[x][y] = randint(1, 100)
    return matrix

def transpose_2d_matrix(matrix):
    ''' transposes 2d matrix '''
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

