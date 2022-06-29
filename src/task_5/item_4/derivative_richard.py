from src.task_5.item_4.Richard_extrapolation import calculate_richard

def solve_derivative_richard(point, value_delta_x1, value_delta_x2, user_errors=[]):

    result = calculate_richard(point, value_delta_x1, value_delta_x2)

    return [result, user_errors]