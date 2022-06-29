from src.utils.matrix_operations import function_task5


def forward_step(consts, x, delta_x):
    result = (function_task5(consts, x + delta_x) -
              function_task5(consts, x)) / delta_x
    print('Derivada: ', str(result))
    return result


def backward_step(consts, x, delta_x):
    result = (function_task5(consts, x) -
              function_task5(consts, x - delta_x)) / delta_x
    print('Derivada: ', str(result))
    return result


def central_difference(consts, x, delta_x):
    result = (function_task5(consts, x + delta_x) -
              function_task5(consts, x - delta_x)) / (2 * delta_x)
    print('Derivada: ', str(result))
    return result
