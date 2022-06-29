from src.task_5.item_2.utils.polynomial_dict import select_polynomial_quadrature
from src.utils.matrix_operations import value_function

def polynomial_quadrature(count_points_integration, point_a, point_b):
    points, weights = select_polynomial_quadrature(count_points_integration, point_a, point_b)
    return sum([value_function(point) * weight for point, weight in zip(points, weights)])