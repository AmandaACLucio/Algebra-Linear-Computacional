import numpy as np

def multiply_matrix_vector(vector, matrix):

    if(len(vector)!=len(matrix[0])):
        return -1

    result = np.zeros(range(matrix))
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[0])):
            sum+=matrix[i][j]*vector[j]
        result[i]=sum

    return result

def multiply_matrix_vector(vector, matrix):
    
    if(len(vector)!=len(matrix[0])):
        return -1

    result = np.zeros(range(matrix))
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[0])):
            sum+=matrix[i][j]*vector[j]
        result[i]=sum

    return result

