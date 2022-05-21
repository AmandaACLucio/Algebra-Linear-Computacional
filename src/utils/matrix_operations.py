import numpy as np
import copy as c


def multiply_matrix_vector(vector, matrix):

    if(len(vector) != len(matrix[0])):
        return -1

    result = np.zeros(range(matrix))
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[0])):
            sum += matrix[i][j]*vector[j]
        result[i] = sum

    return result


def multiply_matrix_scalar(scalar, matrix):

    result = []
    for i in range(len(matrix)):
        line = []
        for j in range(len(matrix[0])):
            line.append(scalar*matrix[i][j])
        result.append(line)

    return result


def multiply_matrix_matrix(matrix1, matrix2):

    if(len(matrix1[0]) != len(matrix2)):
        return -1

    result = []
    for i in range(len(matrix1)):
        line = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            line.append(sum)
        result.append(line)
    return result


def get_submatrix(matrix, index):
    sub_matrix = c.deepcopy(matrix)

    # Removendo primeira coluna
    for i in range(len(sub_matrix)):
        sub_matrix[i] = sub_matrix[i][1:]

    # Removendo linha selecionada
    sub_matrix = sub_matrix[:index] + sub_matrix[index+1:]

    return sub_matrix

def laplace_determinant(matrix):
    det = 0

    num_columns = len(matrix[0])
    num_rows = len(matrix)

    if(num_rows != num_columns):
        return "Erro! Essa matriz não é quadrada. Tente com outros parâmetros!"

    if (num_columns == 1):
        det = matrix[0][0]
    else:
        for k in range(num_rows):
            det += matrix[k][0]*((-1)**k) * laplace_determinant(get_submatrix(matrix, k))
    return det
    
print(laplace_determinant([
    [4,7,3], 
    [1,2,3],
    [2,3,5]
]))