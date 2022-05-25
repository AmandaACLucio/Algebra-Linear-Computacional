import math

from numpy import einsum
from src.utils.matrix_operations import multiply_matrix_vector


def power_method(matrix, tolerance=10**(-5)):
    rows = len(matrix)
    columns = len(matrix[0])

    eigenvector = [1.0 for i in range(columns)]
    eigenvalue = 1.0
    initial_eigenvalue = 1.0
    use_errors = []

    [Y, use_errors] = multiply_matrix_vector(matrix, eigenvector)
    eigenvalue = Y[0]
    steps = 1

    if(len(use_errors>0)):
        return [[], [], 0, use_errors]

    for i in range(len(Y)):
        Y[i] /= eigenvalue

    eigenvector = Y
    residue = math.fabs(eigenvalue - initial_eigenvalue)/eigenvalue
    while (residue >= tolerance):
        initial_eigenvalue = eigenvalue
        Y = multiply_matrix_vector(matrix, eigenvector)

        if( Y == -1):
            return Y

        eigenvalue = Y[0]
        
        for i in range(len(Y)):
            Y[i] /= eigenvalue
        eigenvector = Y

        residue = math.fabs(eigenvalue - initial_eigenvalue)/eigenvalue
        steps += 1

    return [eigenvalue, eigenvector, steps, use_errors]
