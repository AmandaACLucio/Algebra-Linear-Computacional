

from src.task_5.item_2.gauss_square import gauss_legendre
from src.task_5.item_2.polynomial_square import polynomial_quadrature


def solve_integral_defined(point_a, point_b, count_points_integration, method, user_errors=[]):

    result=[]

    if method == 1:
        result = gauss_legendre(count_points_integration, point_a, point_b)
    elif method == 2:
        result = polynomial_quadrature(count_points_integration, point_a, point_b)
    else:
        user_errors.append('Método inválido, escolha entre 1 - Gauss-Legendre e 2 - Polinomial')
        result=-1

    return [result, user_errors]