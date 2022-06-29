import math
from src.utils.matrix_operations import calc_jacobiano, inverse_matrix, multiply_matrix_vector, add_vector_vector, multiply_vector_scalar, norm_vector, value_function

STEPS = 1000


def newton_method_nl(theta1, theta2, tol=0):
    x = [1, 0, 0]

    equations = value_function(x, theta1, theta2)

    for _ in range(STEPS):
        jacobian_inverse = inverse_matrix(
            calc_jacobiano(x))
        vector_f = value_function(x, theta1, theta2)
        if(jacobian_inverse == 0):
            print("Erro! A inversa do Jacobiano não pode ser nula")
            break

        delta_x = multiply_matrix_vector(jacobian_inverse[0], vector_f)
        delta_x = multiply_vector_scalar(delta_x[0], -1)
        x = add_vector_vector(x, delta_x)

        residue = norm_vector(delta_x)/norm_vector(x)

        if (residue < tol):
            print("Solução pelo método de Newton: " + str(x))
            return x

    print("A convergência não foi alcançada")
