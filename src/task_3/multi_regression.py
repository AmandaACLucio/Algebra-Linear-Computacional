from src.utils.matrix_operations import calculate_matrix_p_regressao, transposed_matrix, multiply_matrix_matrix, inverse_matrix, multiply_matrix_vector, value_function

def solver_multilinear_regression(values_x, values_y):
    
    matrix_p = calculate_matrix_p_regressao(values_x)
    matrix_p_transposed = transposed_matrix(matrix_p)

    matrix_a = multiply_matrix_matrix(matrix_p_transposed, matrix_p)
    matrix_c = multiply_matrix_vector(matrix_p_transposed, values_y)

    matrix_a_inverse = inverse_matrix(matrix_a)

    matrix_b = multiply_matrix_vector(matrix_a_inverse, matrix_c)

    return matrix_b

def find_value(values_x, values_y, xi):
    
    matrix_coeficients = solver_multilinear_regression(values_x, values_y)

    value_y_to_xi = value_function(xi, matrix_coeficients)

    return value_y_to_xi
