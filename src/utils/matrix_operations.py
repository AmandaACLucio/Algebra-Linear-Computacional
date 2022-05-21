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

def multiply_matrix_scalar(scalar, matrix):
    
    result = []
    for i in range(len(matrix)):
        line=[]
        for j in range(len(matrix[0])):
            line.append(scalar*matrix[i][j])
        result.append(line)

    return result

def multiply_matrix_matrix(matrix1, matrix2):

    if(len(matrix1[0])!=len(matrix2)):
        return -1

    result=[]
    for i in range(len(matrix1)):
        line=[]
        for j in range(len(matrix2[0])):
            sum=0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            line.append(sum)
        result.append(line)
    return result