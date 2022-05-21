import numpy as np

def multiply_matrix_vector(vector, matrix):

    linesM = len(matrix)
    columnsM = len(matrix[0])
    linesV = len(vector)

    if(linesV!=len(matrix[0])):
        print("A matriz 1 precisa ter o mesmo número de colunas que a quantidade de linhas do vetor")
        return -1

    try:
        result = np.zeros(linesM)
        for i in range(linesM):
            sum = 0
            for j in range(columnsM):
                sum+=matrix[i][j]*vector[j]
            result[i]=sum

        return result

    except Exception as e:
        print("Não foi possível realizar a operação", e)




def multiply_matrix_scalar(scalar, matrix):

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

def check_upper_triangular(matrix):
    
    lines = len(matrix)
    columns = len(matrix[0])

    if(lines!=columns):
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

    if(lines!=columns):
        print("A matriz precisa ser quadrada para realizar essa operação")
        return -1

    for i in range(lines):
        for j in range(i+1, columns):
            if matrix[i][j] != 0:
                return False
    
    return True

def solve_linear_systems_with_lower_triangular(matrix, b):
    #Ax = b

    lines = len(matrix)
    columns = len(matrix[0])

    if(lines!=columns):
        print("A matriz precisa ser quadrada para realizar essa operação")
        return -1

    '''if(matriz  invertível):
        print("A matriz precisa ser quadrada para realizar essa operação")
    return -1'''

    result_x = []

    for i in range(0, lines):


        value_x = b[i]
        ax_sum = 0
        a_ii = matrix[i][i]

        for j in range(0, i):
            
            ax_sum+=matrix[i][j]*result_x[j]

        value_x-=ax_sum
        value_x=value_x/a_ii

        result_x.append(value_x)
    
    return result_x

def solve_linear_systems_with_upper_triangular(matrix, b):

    lines = len(matrix)
    columns = len(matrix[0])

    if(lines!=columns):
        print("A matriz precisa ser quadrada para realizar essa operação")
        return -1

    '''if(matriz  invertível):
        print("A matriz precisa ser quadrada para realizar essa operação")
    return -1'''

    result_x = np.zeros(columns)

    for i in range(lines-1, -1, -1):


        value_x = b[i]
        ax_sum = 0
        a_ii = matrix[i][i]

        for j in range(i+1, lines):
            
            ax_sum+=matrix[i][j]*result_x[j]

        value_x-=ax_sum
        value_x=value_x/a_ii

        result_x[i]=value_x
    
    return result_x

