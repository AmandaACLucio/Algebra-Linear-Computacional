import math
from src.utils.matrix_operations import check_lower_triangular, is_positive_definite, is_square_matrix, is_symmetric, solve_linear_systems_with_lower_triangular, solve_linear_systems_with_upper_triangular, transposed_matrix

def cholesky_decomposition(matrix):

    matrix_g = []
    use_errors = []

    # Verificando se a matriz é quadrada e se o nº de elementos por linha é o mesmo
    if (not is_square_matrix(matrix)):
        str_error = "Erro! Essa matriz não é quadrada. Tente com outros parâmetros!"
        return [matrix_g, use_errors.append(str_error)]

    [is_symmetric_bool, use_errors] = is_symmetric(matrix, use_errors)
    if (not is_symmetric_bool):
        str_error = "Não é possível utilizar esse método pois essa matriz não é simétrica"
        return [matrix_g, use_errors.append(str_error)]

    [is_positive_definite_bool, use_errors] = is_positive_definite(matrix, use_errors)
    if (not is_positive_definite_bool):
        str_error = "Não é possível utilizar esse método pois essa matriz não é positiva definida"
        return [matrix_g, use_errors.append(str_error)]
    
    # Criando matriz G com a mesma ordem da matriz A
    matrix_g = [[0] * len(matrix) for x in range(len(matrix))]
    
    for i in range(len(matrix)):
        total = 0
        for j in range(i+1):
            if (i==j):
                total = sum(matrix_g[i][k]**2 for k in range(i))
                matrix_g[i][i] = round(math.sqrt(matrix[i][i]-total), 2)
                continue
            
            total = sum(matrix_g[i][k]*matrix_g[j][k] for k in range(i))
            matrix_g[i][j] = round((matrix[i][j] - total)/matrix_g[j][j], 2)
    
    return [matrix_g, use_errors]

def solve_by_cholesky(matrix, vector):

    [matrix_g, use_errors] = cholesky_decomposition(matrix)
    
    if(len(use_errors)>0):
        return [matrix_g, use_errors]

    if (not check_lower_triangular(matrix_g)):
        str_error = "A matriz não é triangular inferior."
        return [matrix_g, use_errors.append(str_error)]

    matrix_y = solve_linear_systems_with_lower_triangular(matrix_g, vector, False)
    matrix_b = solve_linear_systems_with_upper_triangular(transposed_matrix(matrix_g), matrix_y)

    return [matrix_b, use_errors]
