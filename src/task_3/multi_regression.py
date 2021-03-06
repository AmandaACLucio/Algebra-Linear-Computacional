from src.utils.matrix_operations import calculate_matrix_p_regressao, transposed_matrix, multiply_matrix_matrix, multiply_matrix_vector, value_function

from src.task_2.metodo_jacobi import inverse_matrix

def solver_multilinear_regression(values_x, values_y):

    use_errors = []
    matrix_b = []

    if(len(values_x)!=len(values_y)):
        str_error = "A quantidade de parâmetros x deve ser igual a de parâmetro y"
        use_errors.append(str_error)
        return [matrix_b, use_errors]

    matrix_p = calculate_matrix_p_regressao(values_x)
    matrix_p_transposed = transposed_matrix(matrix_p)

    [matrix_a, use_errors] = multiply_matrix_matrix(matrix_p_transposed, matrix_p)
    [matrix_c, use_errors] = multiply_matrix_vector(matrix_p_transposed, values_y)

    [matrix_a_inverse, use_errors] = inverse_matrix(matrix_a, use_errors)

    [matrix_b, use_errors] = multiply_matrix_vector(matrix_a_inverse, matrix_c)

    return [matrix_b, use_errors]

def find_value(values_x, values_y, xi, use_errors=[]):
    
    [matrix_coeficients, use_errors] = solver_multilinear_regression(values_x, values_y)

    if(len(use_errors)>0):
        return ["undefined", use_errors]

    value_y_to_xi = value_function(xi, matrix_coeficients)

    return [value_y_to_xi, use_errors]
