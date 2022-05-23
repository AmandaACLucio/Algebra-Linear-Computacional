from re import T
import numpy as np
import copy as c
import math

def is_square_matrix(matrix):
    # Verificando se a matriz é quadrada e se tem o mesmo número de elementos em todas as linhas
    if any(len(i) != len(matrix) for i in matrix):
        return False
    return True

def multiply_matrix_vector(matrix, vector):

    linesM = len(matrix)
    columnsM = len(matrix[0])
    linesV = len(vector)

    if(linesV!=len(matrix[0])):
        print("A matriz 1 precisa ter o mesmo número de colunas que a quantidade de linhas do vetor")
        return -1

    try:
        result = [0 for i in range(linesM)]
        for i in range(linesM):
            sum = 0
            for j in range(columnsM):
                sum+=matrix[i][j]*vector[j]
            result[i]=sum

        return result

    except Exception as e:
        print("Não foi possível realizar a operação", e)


def multiply_matrix_scalar(matrix,scalar):

    lines = len(matrix)
    columns = len(matrix[0])

    result = []
    for i in range(lines):
        line=[]
        for j in range(columns):
            line.append(scalar*matrix[i][j])
        result.append(line)

    return result

def multiply_matrix_matrix(matrix1, matrix2):

    linesM1= len(matrix1)
    columnsM1 = len(matrix1[0])
    linesM2 = len(matrix2)
    columnsM2 = len(matrix2[0])


    if(columnsM1!=linesM2):
        print("A matriz 1 precisa ter o mesmo número de colunas que a quantidade de linhas da matriz 2")
        return -1

    result=[]
    for i in range(linesM1):
        line=[]
        for j in range(columnsM2):
            sum=0
            for k in range(linesM2):
                sum += matrix1[i][k] * matrix2[k][j]
            line.append(sum)
        result.append(line)
    return result

def sub_vector_vector(vector1, vector2):

    vector_result = [vector1[linha]-vector2[linha] for linha in range(len(vector1))]

    return vector_result

def add_vector_vector(vector1, vector2):
    
    vector_result = [vector1[linha]+vector2[linha] for linha in range(len(vector1))]

    return vector_result


def mult_vector_scalar(vector, scalar):
    
    vector_result = [vector[linha]*scalar for linha in range(len(vector))]

    return vector_result


def check_upper_triangular(matrix):
    
    lines = len(matrix)
    columns = len(matrix[0])

    if(not is_square_matrix(matrix)):
        print("A matriz precisa ser quadrada para realizar essa operação")
        return -1

    for i in range(lines):
        for j in range(0, i):
            if matrix[i][j] != 0:
                return False
    
    return True

def check_lower_triangular(matrix):
    
    lines = len(matrix)
    columns = len(matrix[0])

    if(not is_square_matrix(matrix)):
        print("A matriz precisa ser quadrada para realizar essa operação")
        return -1

    for i in range(lines):
        for j in range(i+1, columns):
            if matrix[i][j] != 0:
                return False
    
    return True

def solve_linear_systems_with_lower_triangular(matrix, vector_b, is_lu=True):
    lines = len(matrix)
    
    result_x = [0 for i in range(lines)]
    
    if(is_lu):
        result_x[0] = vector_b[0]
    else:
        result_x[0] = vector_b[0]/matrix[0][0]

    for i in range(1, lines):
        ax_sum = vector_b[i]
        for j in range(i):
            ax_sum -= matrix[i][j]*result_x[j]

        if(is_lu):
            result_x[i] = ax_sum
        else:
            result_x[i]= ax_sum/matrix[i][i]

    return result_x
    
def solve_linear_systems_with_upper_triangular(matrix, vector_b):
    lines = len(matrix)

    result_x = [0 for i in range(lines)]

    result_x[lines-1] = vector_b[lines-1] /matrix[lines-1][lines-1]

    for i in range(lines-2, -1, -1):
        ax_sum = vector_b[i]
        for j in range(i+1, lines):
            ax_sum -= matrix[i][j]*result_x[j]

        result_x[i] = ax_sum/float(matrix[i][i])

    return result_x

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

    lines = len(matrix)
    columns = len(matrix[0])

    if(not is_square_matrix(matrix)):
        print("Erro! Essa matriz não é quadrada. Tente com outros parâmetros!")
        return -1

    if (columns == 1):
        det = matrix[0][0]
    else:
        for k in range(lines):
            det += matrix[k][0]*((-1)**k) * laplace_determinant(get_submatrix(matrix, k))
    return det

def is_symmetric(matrix):
    if (not is_square_matrix(matrix)):
        print("Essa matriz não é quadrada, tente com outro parâmetro")
        return -1
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def get_minor(matrix, order):

    if (order > (len(matrix) - 1)):
        print ("A ordem da menor principal não pode ser maior que a ordem da matriz.")
        return False

    column = []
    for i in range(order+1):
        row = []
        for j in range(order+1):
            row.append(matrix[i][j])
        column.append(row)

    return column

def sylvester_condition(matrix):
    for i in range(len(matrix)):
        aux_matrix = get_minor(matrix, i)
        if(laplace_determinant(aux_matrix) > 0):
            return True
    return False

def is_positive_definite(matrix):
    return sylvester_condition(matrix)

def transposed_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

def norm_vector(vector):

    norma=0

    for i in range(len(vector)):
        norma+=vector[i]**2
    
    norma=norma**0.5
    return norma

def value_residue(vector_after, vector_before):

    return norm_vector(sub_vector_vector(vector_after,vector_before))/norm_vector(vector_after)

def converges(matrix):

    lines = len(matrix)
    columns = len(matrix[0])

    if(not is_square_matrix(matrix)):
        print("A matriz precisa ser quadrada para realizar essa operação")
        return -1

    for l in range(lines):
        
        sum_line = 0        
        sum_column = 0  

        for c in range(columns):

            if(l != c):

                sum_line += math.fabs(matrix[l][c])
                sum_column += math.fabs(matrix[c][l])

        if(sum_column>matrix[l][l] or sum_line>matrix[l][l]):
            return False                

    return True

def get_big_value(matrix):

    lines = len(matrix)
    columns = len(matrix[0])
    the_big = -math.inf

    index=[]

    for i in range(lines):
        for j in range(columns):

            if(math.fabs(matrix[i][j])>the_big and i!=j):
                the_big=matrix[i][j]
                index=[i, j]
    return [the_big, index]


def calculate_phi(matrix, index):

    i= index[0]
    j= index[1]

    a_ii = matrix[i][i]
    a_jj = matrix[j][j]
    a_ij = matrix[i][j]
    
    if(a_ii!=a_jj):
        
        value = 0.5*math.atan((2*a_ij)/(a_ii-a_jj))
        return value
    
    return math.pi/4


def calculate_matrix_p(matrix, index):
    
    lines = len(matrix)    
    value_phi = calculate_phi(matrix, index)

    matrix_p = [[float(i == j) for j in range(lines)] for i in range(lines)]


    matrix_p[index[0]][index[0]] = math.cos(value_phi)
    matrix_p[index[1]][index[1]] = math.cos(value_phi)
    matrix_p[index[0]][index[1]] = -math.sin(value_phi)
    matrix_p[index[1]][index[0]] = math.sin(value_phi)

    return matrix_p


