from src.utils.matrix_operations import is_symmetric, get_big_value, calculate_matrix_p_jacobiano, transposed_matrix, multiply_matrix_matrix

def solver_jacobi(matrix, max_tolerance=0, use_errors=[]):
    

    steps=0
    eigen_values=[]
    eigen_vectors=[]
    use_errors = []

    [is_symmetric_bool, use_errors] = is_symmetric(matrix, use_errors)
    if (not is_symmetric_bool):
        str_error = "Não é possível utilizar esse método pois essa matriz não é simétrica"
        use_errors.append(str_error)
        return [eigen_values, eigen_vectors, steps, use_errors]
    
    lines=len(matrix)

    
    [big_element_value, big_element_index] = get_big_value(matrix)
    matrix_x = [[float(i == j) for j in range(lines)] for i in range(lines)]

    while(big_element_value>max_tolerance):

        matrix_p = calculate_matrix_p_jacobiano(matrix, big_element_index)
        matrix_p_transposed = transposed_matrix(matrix_p)

        [matrix_A_P, use_errors] =  multiply_matrix_matrix(matrix, matrix_p, use_errors)
        [matrix, use_errors] = multiply_matrix_matrix(matrix_p_transposed, matrix_A_P, use_errors)

        [matrix_x, use_errors] = multiply_matrix_matrix(matrix_x, matrix_p, use_errors)

        [big_element_value, big_element_index] = get_big_value(matrix)
        
        steps+=1

    lines = len(matrix)
    eigen_values = [matrix[i][j] for i in range(lines) for j in range(lines) if i==j]

    eigen_vectors =  transposed_matrix(matrix_x)
    determinant = 1

    for i in eigen_values:
        determinant*=i


    return [eigen_values, eigen_vectors, steps, determinant, use_errors]


def inverse_auxiliar_function(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]


def inverse_matrix(matrix, use_errors=[]):
    
    matrix_cofactors = []
    
    value_determinant = solver_jacobi(matrix, 0.00001)[3]

    if(len(use_errors)>0):

        return [0, use_errors]

    if(value_determinant == 0):
        return [0, use_errors]

    for i in range(len(matrix)):

        line_cofactor = []

        for j in range(len(matrix)):
            minor = inverse_auxiliar_function(matrix, i, j)
            determinant = solver_jacobi(minor, 0.00001)[3]
            line_cofactor.append(((-1)**(i+j)) * determinant)

        matrix_cofactors.append(line_cofactor)

    matrix_cofactors = transposed_matrix(matrix_cofactors)

    for i in range(len(matrix_cofactors)):
        for j in range(len(matrix_cofactors)):

            matrix_cofactors[i][j] = matrix_cofactors[i][j]/value_determinant

    return [matrix_cofactors, use_errors]


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

def sylvester_condition(matrix, use_errors=[]):
    for i in range(len(matrix)):
        aux_matrix = get_minor(matrix, i)
        det = solver_jacobi(aux_matrix, 0.00001)[3]

        if(len(use_errors)>0):
            return [False, use_errors]

        if( det > 0):
            return [True, use_errors]
    return [False, use_errors]

def is_positive_definite(matrix, use_errors=[]):
    return [sylvester_condition(matrix), use_errors]