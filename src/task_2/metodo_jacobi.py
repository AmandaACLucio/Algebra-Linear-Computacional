from src.utils.matrix_operations import is_symmetric, get_big_value, calculate_matrix_p_jacobiano, transposed_matrix, multiply_matrix_matrix

def solver_jacobi(matrix, max_tolerance=0):
    
    if (not is_symmetric(matrix)):
        print("Não é possível utilizar esse método pois essa matriz não é simétrica")
        return -1

    lines=len(matrix)

    
    [big_element_value, big_element_index] = get_big_value(matrix)
    matrix_x = [[float(i == j) for j in range(lines)] for i in range(lines)]

    steps=0


    while(big_element_value>max_tolerance):

        matrix_p = calculate_matrix_p_jacobiano(matrix, big_element_index)
        matrix_p_transposed = transposed_matrix(matrix_p)

        matrix = multiply_matrix_matrix(matrix_p_transposed,multiply_matrix_matrix(matrix, matrix_p))
        matrix_x = multiply_matrix_matrix(matrix_x, matrix_p)

        [big_element_value, big_element_index] = get_big_value(matrix)
        
        steps+=1


    eigen_values = [matrix[i][j] for i in range(lines) for j in range(lines) if i==j]

    eigen_vectors =  transposed_matrix(matrix_x)

    return [eigen_values, eigen_vectors, steps]