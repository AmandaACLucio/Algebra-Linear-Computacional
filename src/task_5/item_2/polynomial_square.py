from src.task_5.item_2.utils.polynomial_dict import select_polynomial_quadrature
from src.utils.matrix_operations import function_task5


def polynomial_quadrature(consts, count_points_integration, point_a, point_b):

    polynomial_table = select_polynomial_quadrature(
        count_points_integration, point_a, point_b)

    [zpoint, weight] = polynomial_table[0][count_points_integration], polynomial_table[1][count_points_integration]

    
    return sum([function_task5(consts, zpoint[i])*weight[i] for i in range(count_points_integration)])
