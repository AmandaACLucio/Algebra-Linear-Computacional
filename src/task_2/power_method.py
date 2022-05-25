import math

from numpy import einsum
from src.utils.matrix_operations import multiply_matrix_vector


def power_method(matrix, tolerance=10**(-5)):
    rows = len(matrix)
    columns = len(matrix[0])

    eigenvector = [1.0]*columns
    eigenvalue = 1.0
    initial_eigenvalue = 1.0

    Y = multiply_matrix_vector(matrix, eigenvector)
    eigenvalue = Y[0]
    steps = 1

    if( Y == -1):
        return Y

    for i in range(len(Y)):
        Y[i] /= eigenvalue

    eigenvector = Y
    residue = math.fabs(eigenvalue - initial_eigenvalue)/eigenvalue
    while (residue >= tolerance):
        print(residue)
        initial_eigenvalue = eigenvalue
        print(initial_eigenvalue, '-', eigenvalue)
        Y = multiply_matrix_vector(matrix, eigenvector)

        if( Y == -1):
            return Y

        eigenvalue = Y[0]
        print(initial_eigenvalue, '-', eigenvalue)

        
        for i in range(len(Y)):
            Y[i] /= eigenvalue
        eigenvector = Y

        residue = math.fabs(eigenvalue - initial_eigenvalue)/eigenvalue
        print(eigenvalue - initial_eigenvalue)
        print(residue)
        steps += 1

    return eigenvalue, eigenvector, steps

print(power_method([
    [1, 0.2, 0],
    [0.2, 1, 0.5],
    [0, 0.5, 1]
], 10**(-3)))
