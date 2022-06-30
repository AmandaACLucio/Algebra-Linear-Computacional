from src.task_5.item_2.utils.polynomial_dict import select_polynomial_quadrature
from src.utils.matrix_operations import function_task5


def polynomial_quadrature(consts, count_points_integration, point_a, point_b):

    zpoints, weights = select_polynomial_quadrature(
        count_points_integration, point_a, point_b)
    return sum([function_task5(consts, zpoints[i])*weights[i] for i in range(count_points_integration)])
