from cgi import print_form
from re import T
import copy as c
import math

from matplotlib.style import use

def is_square_matrix(matrix):
    # Verificando se a matriz é quadrada e se tem o mesmo número de elementos em todas as linhas
    if any(len(i) != len(matrix) for i in matrix):
        return False
    return True

#transpor vetor
def transpose_vector(vector):
    return [[vector[i]] for i in range(len(vector))]

def multiply_vector_matrix(vector, matrix, use_errors=[]):
    columnsM = len(matrix[0])
    colunsV = len(vector)
    result = [0 for x in range(columnsM)]

    if(colunsV!=len(matrix)):
        str_error = "A matriz 1 precisa ter o mesmo número de colunas que a quantidade de linhas do vetor"
        use_errors.append(str_error)
        return [result, use_errors]

    for j in range(columnsM):
        sum = 0
        for i in range(colunsV):
            sum+=matrix[i][j]*vector[i]
        result[j]=sum

    return [result, use_errors]

def multiply_matrix_vector(matrix, vector, use_errors=[]):

    linesM = len(matrix)
    columnsM = len(matrix[0])
    linesV = len(vector)
    result = [0 for i in range(linesM)]

    if(linesV!=len(matrix[0])):
        str_error = "A matriz 1 precisa ter o mesmo número de colunas que a quantidade de linhas do vetor"
        use_errors.append(str_error)
        return [result, use_errors]

    for i in range(linesM):
        sum = 0
        for j in range(columnsM):
            sum+=matrix[i][j]*vector[j]
        result[i]=sum

    return [result, use_errors]


def sub_matrix_matrix(matrix1, matrix2):
    lines = len(matrix1)
    columns = len(matrix1[0])

    result = []
    for i in range(lines):
        line=[]
        for j in range(columns):
            line.append(matrix1[i][j]-matrix2[i][j])
        result.append(line)

    return result

def add_matrix_matrix(matrix1, matrix2):
    lines = len(matrix1)
    columns = len(matrix1[0])

    result = []
    for i in range(lines):
        line=[]
        for j in range(columns):
            line.append(matrix1[i][j]+matrix2[i][j])
        result.append(line)

    return result

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

def multiply_matrix_matrix(matrix1, matrix2, use_errors=[]):

    linesM1= len(matrix1)
    columnsM1 = len(matrix1[0])
    linesM2 = len(matrix2)
    columnsM2 = len(matrix2[0])

    result=[]


    if(columnsM1!=linesM2):
        str_error = "A matriz 1 precisa ter o mesmo número de colunas que a quantidade de linhas da matriz 2"
        use_errors.append(str_error)
        return [result, use_errors]

    result=[]
    for i in range(linesM1):
        line=[]
        for j in range(columnsM2):
            sum=0
            for k in range(linesM2):
                sum += matrix1[i][k] * matrix2[k][j]
            line.append(sum)
        result.append(line)
        
    return [result, use_errors]

def sub_vector_vector(vector1, vector2):

    vector_result = [vector1[linha]-vector2[linha] for linha in range(len(vector1))]

    return vector_result

def add_vector_vector(vector1, vector2):
    
    vector_result = [vector1[linha]+vector2[linha] for linha in range(len(vector1))]

    return vector_result


def multiply_vector_scalar(vector, scalar):
    
    vector_result = [vector[linha]*scalar for linha in range(len(vector))]

    return vector_result

def multiply_vector_vector(vector1, vector2):
    
    sum = 0
    for i in range(len(vector1)):
        sum+=vector1[i]*vector2[i]

    return sum

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

def solve_linear_systems_with_lower_triangular(matrix, vector_b, is_lu=True, use_errors=[]):
    
    lines = len(matrix)
    linesV = len(vector_b)

    if(linesV!=len(matrix[0])):
        str_error = "A matriz 1 precisa ter o mesmo número de colunas que a quantidade de linhas do vetor"
        use_errors.append(str_error)
        return [[], use_errors]

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

    return [result_x, use_errors]
    
def solve_linear_systems_with_upper_triangular(matrix, vector_b, use_errors=[]):
    lines = len(matrix)

    linesV = len(vector_b)

    if(linesV!=len(matrix[0])):
        str_error = "A matriz 1 precisa ter o mesmo número de colunas que a quantidade de linhas do vetor"
        use_errors.append(str_error)
        return [[], use_errors]

    result_x = [0 for i in range(lines)]

    result_x[lines-1] = vector_b[lines-1] /matrix[lines-1][lines-1]

    for i in range(lines-2, -1, -1):
        ax_sum = vector_b[i]
        for j in range(i+1, lines):
            ax_sum -= matrix[i][j]*result_x[j]

        result_x[i] = ax_sum/float(matrix[i][i])

    return [result_x, use_errors]

def get_submatrix(matrix, index):
    secondary = c.deepcopy(matrix)

    for row in range(len(secondary)):
        secondary[row] = secondary[row][1:]

    return secondary[:index] + secondary[index+1:]

def is_symmetric(matrix, use_errors=[]):
    
    if (not is_square_matrix(matrix)):
        str_error = "Erro! Essa matriz não é quadrada. Tente com outros parâmetros!"
        use_errors.append(str_error)
        return [False, use_errors]

    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != matrix[j][i]:
                return [False, use_errors]
    return [True, use_errors]

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

def laplace_determinant(matrix, use_errors=[]):
    if (not is_square_matrix(matrix)):
        str_error = "Erro! Essa matriz não é quadrada. Tente com outros parâmetros!"
        use_errors.append(str_error)
        return [False, use_errors]

    if (len(matrix) == 1):
        return [matrix[0][0], use_errors]

    if (len(matrix) == 2):
        return [matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0], use_errors]

    determinant = 0
    for i in range(len(matrix)):
        value_current_det = laplace_determinant(get_minor(matrix, i), use_errors)
        determinant += (-1)**i*matrix[0][i]*value_current_det[0]
    return [determinant, use_errors]

def sylvester_condition(matrix, use_errors=[]):
    for i in range(len(matrix)):
        aux_matrix = get_minor(matrix, i)
        det = laplace_determinant(aux_matrix)

        if(len(use_errors)>0):
            return [False, use_errors]

        if( det > 0):
            return [True, use_errors]
    return [False, use_errors]

def is_positive_definite(matrix, use_errors=[]):
    return [sylvester_condition(matrix), use_errors]

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


def calculate_matrix_p_jacobiano(matrix, index):
    
    lines = len(matrix)    
    value_phi = calculate_phi(matrix, index)

    matrix_p = [[float(i == j) for j in range(lines)] for i in range(lines)]


    matrix_p[index[0]][index[0]] = math.cos(value_phi)
    matrix_p[index[1]][index[1]] = math.cos(value_phi)
    matrix_p[index[0]][index[1]] = -math.sin(value_phi)
    matrix_p[index[1]][index[0]] = math.sin(value_phi)

    return matrix_p

def inverse_auxiliar_function(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

def inverse_matrix(matrix):
    
    cofactors = []
    use_errors = []
    determinant = laplace_determinant(matrix)[0]
    if(determinant == 0):
        return [0, use_errors]

    for r in range(len(matrix)):
        cofactorRow = []

        for c in range(len(matrix)):
            minor = inverse_auxiliar_function(matrix, r, c)
            cofactorRow.append(((-1)**(r+c))*laplace_determinant(minor)[0])

        cofactors.append(cofactorRow)

    cofactors = transposed_matrix(cofactors)


    for r in range(len(cofactors)):
        for c in range(len(cofactors)):

            cofactors[r][c] = cofactors[r][c]/determinant

    return [cofactors, use_errors]
'''

def inverse_matrix(matrix, use_errors=[]):
    if (not is_square_matrix(matrix)):
        str_error = "Erro! Essa matriz não é quadrada. Tente com outros parâmetros!"
        use_errors.append(str_error)
        return [False, use_errors]

    if (len(matrix) == 1):
        return [matrix[0][0], use_errors]

    if (len(matrix) == 2):
        return [matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0], use_errors]

    determinant = laplace_determinant(matrix)[0]

    if(determinant == 0):
        str_error = "Erro! O determinante da matriz é 0. Tente com outros parâmetros!"
        use_errors.append(str_error)
        return [-1, use_errors]

    inverse = [[float(0) for j in range(len(matrix))] for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            inverse[i][j] = (1/determinant)*(laplace_determinant(get_submatrix(matrix, j))*calculate_matrix_p_jacobiano(matrix, [i, j]))[0]

    return [inverse, use_errors]
'''

def calculate_matrix_p_regressao(values_x):

    matrix_p = []
    count_x = len(values_x)

    for i in range(count_x):
        matrix_p.append(fatores_function(values_x[i]))
    
    return matrix_p

def fatores_function(xi):

    "calculos feitos para cada"
    "ex: a+bx+c**2 -> [1, x, x**2]"

    #return [1, xi, xi**2]
    return [1/(math.e**xi), math.log(xi)]

''' def value_function(xi, coeficients):

    #a+bx+cx**2

    a=coeficients[0]
    b= coeficients[1]
    #c = coeficients[2]

    #return a+b*x+c*(x**2)
    return a*1/(math.e**xi)+b*math.log(xi) '''

def calc_jacobiano(value_x):

    [c2, c3, c4] = value_x

    dF1_dxn = [2*c2, 4*c3, 12*c4]
    
    dF2_dxn = [12*c3*c2 + 36*c3*c4, \
            24*c3**2 + 6*c2**2 + 36*c2*c4 + 108*c4**2, \
            36*c2*c3 + 2*108*c3*c4]
    
    dF3_dx1 = 2*60*(c3**2)*c2 + 576*(c3**2)*c4 + 2*252*(c4**2)*c2 + 1296*(c4**3) + 3*24*(c2**2)*c4 + 3
    dF3_dx2 = 4*60*c3**3 + 2*60*c3*c2**2 + 2*576*c2*c3*c4 + 2*2232*c3*c4**2
    dF3_dx3 = 576*c2*c3**2 + 2*2232*(c3**2)*c4 + 2*252*c4*c2**2 + 3*1296*(c4**2)*c2 + 4*3348*c4**3 + 24*(c2**3)

    dF3_dxn = [dF3_dx1, dF3_dx2, dF3_dx3]

    return [dF1_dxn, dF2_dxn, dF3_dxn]


def value_function(value_x, phi_1, phi_2):

    '''
    function_1 = 2*value_x[1]**2 + value_x[0]**2 + 6*value_x[2]**2 - 1

    function_2 = 8*value_x[1]**2 + 6*value_x[1]*value_x[0]**2 + 36*value_x[1]*value_x[0]*value_x[2] + 108*value_x[1]*value_x[2]**2 - phi_1
    
    function_3 = 60*value_x[1]**4 + 60*(value_x[1]**2)*(value_x[0]**2) + 576*(value_x[1]**2)*value_x[0]*value_x[2] + 2232*(value_x[1]**2)*(value_x[2]**2) + 252*(value_x[2]**2)*(value_x[0]**2) + 1296*(value_x[2]**3)*value_x[0] \
        + 3348*value_x[2]**4 + 24*(value_x[0]**3)*value_x[2] + 3*value_x[0] - phi_2
    
    return [function_1, function_2, function_3]'''

    x1= value_x[0]
    x2= value_x[1]
    return [x1+2*x2-2-phi_1, x1**2 + 4*(x2**2)-4-phi_2]	