import math
from src.utils.matrix_operations import check_lower_triangular, is_positive_definite, is_square_matrix, is_symmetric, solve_linear_systems_with_lower_triangular, solve_linear_systems_with_upper_triangular, transposed_matrix

def cholesky_decomposition(matrix):
    # Verificando se a matriz é quadrada e se o nº de elementos por linha é o mesmo
    if (not is_square_matrix(matrix)):
        print("Erro! Essa matriz não é quadrada. Tente com outros parâmetros!")
        return -1
    if (not is_symmetric(matrix)):
        print("Não é possível utilizar esse método pois essa matriz não é simétrica")
        return -1

    if (not is_positive_definite(matrix)):
        print("Não é possível utilizar esse método pois essa matriz não é positiva definida")
        return -1
    
    # Criando matriz G com a mesma ordem da matriz A
    g = [[0] * len(matrix) for x in range(len(matrix))]
    
    for i in range(len(matrix)):
        total = 0
        for j in range(i+1):
            if (i==j):
                total = sum(g[i][k]**2 for k in range(i))
                g[i][i] = round(math.sqrt(matrix[i][i]-total), 2)
                continue
            
            total = sum(g[i][k]*g[j][k] for k in range(i))
            g[i][j] = round((matrix[i][j] - total)/g[j][j], 2)
    
    return g

def solve_by_cholesky(matrix, vector):
    g = cholesky_decomposition(matrix)

    if(g == -1):
        return g
    
    if (not check_lower_triangular(g)):
        print("A matriz não é triangular inferior.")
        return -1

    y = solve_linear_systems_with_lower_triangular(g, vector, False)

    return solve_linear_systems_with_upper_triangular(transposed_matrix(g), y)