import math
from src.utils.matrix_operations import get_jacobian_matrix, inverse_matrix, multiply_matrix_vector, sum_vectors, norm_vector, get_vector_f

STEPS = 1000
TOL = 10**-4


def newton_method_nl(equations, x0):
    x = x0

    for _ in range(STEPS):
        jacobian_inverse = inverse_matrix(
            get_jacobian_matrix(equations, x))
        vector_f = get_vector_f(equations, x)

        if(jacobian_inverse == 0):
            print("Erro! A inversa do Jacobiano não pode ser nula")
            break

        delta_x = multiply_matrix_vector(jacobian_inverse, vector_f)
        delta_x = [x*(-1) for x in delta_x]
        x = sum_vectors(x, delta_x)

        residue = norm_vector(delta_x)/norm_vector(x)

        if (residue < TOL):
            print("Solução pelo método de Newton: " + str(x))
            return x

    print("A convergência não foi alcançada")
