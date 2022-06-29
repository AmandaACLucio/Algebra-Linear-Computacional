from src.utils.matrix_operations import function_task5

def previous_step(point, value_delta_x):

    derivative = (function_task5(point) - function_task5(point - value_delta_x)) / value_delta_x
    return derivative


def next_step(point, delta_x):

    derivative = (function_task5(point + delta_x) - function_task5(point)) / delta_x
    return derivative

def calculate_richard(point, value_delta_x1, value_delta_x2):
    value_p = 1
    value_q = value_delta_x1/value_delta_x2

    derivative1 = next_step(point, value_delta_x1)
    derivative2 = next_step(point, value_delta_x2)

    result = derivative1 + (derivative1-derivative2)/(value_q**(-value_p) - 1)

    return result