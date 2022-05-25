import copy
from src.utils.matrix_operations import solve_linear_systems_with_lower_triangular,solve_linear_systems_with_upper_triangular

def decomposition_LU(matrix):

    columns = len(matrix[0])
    lines = len(matrix)
    matrix_LU = copy.deepcopy(matrix)
    use_errors = []

    if(lines != columns):
        str_error = "Erro! Essa matriz não é quadrada. Tente com outros parâmetros!"
        use_errors.append(str_error)
        return [matrix_LU, use_errors]

    for k in range(lines):
        for i in range(k+1, lines):
            matrix_LU[i][k] = float(matrix_LU[i][k]/matrix_LU[k][k])

        for j in range(k+1, columns):
            for i in range(k+1, columns):
                matrix_LU[i][j] = float(matrix_LU[i][j]-matrix_LU[i][k]*matrix_LU[k][j])
    
    return [matrix_LU, use_errors]


def solve_decomposition_LU(matrix, vector_b):

    #Temos LUx=b, chamamos Ux de y, então temos Ly=b, descobrimos y e depois fazemos Ux=y

    [matrix_LU, use_errors] = decomposition_LU(matrix)

    if(len(use_errors)>0):
        return [matrix_LU, use_errors]
    
    [Solve_Ly_b, use_errors] = solve_linear_systems_with_lower_triangular(matrix_LU, vector_b)

    if(len(use_errors)>0):
        return [[], use_errors]

    [Solve_Ux_y, use_errors]=solve_linear_systems_with_upper_triangular(matrix_LU, Solve_Ly_b)

    return [Solve_Ux_y, use_errors]