from src.task_5.item_2.utils.gauss_dict import dict_gauss_quadrature, select_quadrature
from src.utils.matrix_operations import function_task5

def gauss_legendre(count_points_integration, point_a, point_b):

    quadrature = select_quadrature(count_points_integration)
    L = point_b-point_a

    points = map(lambda point: 0.5*(point_a + point_b + point*L), quadrature.get('zpoints'))

    sum_weights = sum([function_task5(point) * weight for point, weight in zip(points, quadrature['weights'])])
    return (L/2)*sum_weights
