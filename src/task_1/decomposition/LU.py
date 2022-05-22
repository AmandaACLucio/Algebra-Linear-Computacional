import copy
from src.utils.matrix_operations import solve_linear_systems_with_lower_triangular,solve_linear_systems_with_upper_triangular

def decomposition_LU(matrix):

    columns = len(matrix[0])
    lines = len(matrix)
    matrix_LU = copy.deepcopy(matrix)

    if(lines != columns):
        print("Erro! Essa matriz não é quadrada. Tente com outros parâmetros!")
        return -1

    for k in range(lines):
        for i in range(k+1, lines):
            matrix_LU[i][k] = float(matrix_LU[i][k]/matrix_LU[k][k])

        for j in range(k+1, columns):
            for i in range(k+1, columns):
                matrix_LU[i][j] = float(matrix_LU[i][j]-matrix_LU[i][k]*matrix_LU[k][j])
    
    return matrix_LU

def solve_decomposition_LU(matrix, vector_b):

    #Temos LUx=b, chamamos Ux de y, então temos Ly=b, descobrimos y e depois fazemos Ux=y

    matrix_LU = decomposition_LU(matrix)
    
    Solve_Ly_b = solve_linear_systems_with_lower_triangular(matrix_LU, vector_b)

    Solve_Ux_y=solve_linear_systems_with_upper_triangular(matrix_LU, Solve_Ly_b)

    return(Solve_Ux_y)



print(solve_decomposition_LU([[2,3,-4,4],[-4,-7,11,-6],[6,11,-20,10],[-2,-7,22,-6]],[-1,5,-13,25]))
