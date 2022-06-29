#from src.task_2.metodo_jacobi import inverse_matrix

from logging import exception
from src.utils.matrix_operations import  add_vector_vector, multiply_matrix_scalar, multiply_vector_scalar, multiply_vector_vector, multiply_vector_matrix, multiply_matrix_matrix, sub_vector_vector, norm_vector, multiply_matrix_vector, value_function, inverse_matrix, transpose_vector, add_matrix_matrix

def broyden_method(phi_1, phi_2, max_tolerance=0, n_iterations=1000):

    Bk_previous = [[int(i==j) for i in range(3)] for j in range(3)]
    #Bk_previous = [[1, 2], [4, 24]]

    use_errors = []
    vector_x = [1, 0, 0]
    value_function_vector=[]

    for i in range(1, n_iterations):
        matrix_J = Bk_previous

        try:

            J_inverse = inverse_matrix(matrix_J)[0]

            value_function_vector =value_function(vector_x, phi_1, phi_2)
            J_inv_x_F = multiply_matrix_vector(J_inverse, value_function_vector)[0]

            vector_delta_x = multiply_vector_scalar(J_inv_x_F,-1)

            print("vector_delta_x: ", vector_delta_x)

        except Exception as e:

            use_errors.append("The matrix B generated was a Sigunlar matrix")
            return [-1, use_errors]

        vector_x = add_vector_vector(vector_x, vector_delta_x)

        vector_y = sub_vector_vector(value_function(vector_x, phi_1, phi_2), value_function_vector)

        tolk = norm_vector(vector_delta_x)/norm_vector(vector_x)

        print(tolk)

        if(tolk<max_tolerance):

            return [vector_x, use_errors]

        else:

            Bk_previous_mult_vector_delta_x = multiply_vector_scalar(multiply_matrix_vector(Bk_previous, vector_delta_x)[0], -1) #P

            Yk_sub_P = add_vector_vector(vector_y, Bk_previous_mult_vector_delta_x) #Q

            Yk_sub_P = transpose_vector(Yk_sub_P)

            Yk_sub_P_x_transposed = multiply_matrix_matrix (Yk_sub_P, [vector_delta_x])[0] #R

            delta_x_2 = multiply_vector_vector( vector_delta_x, vector_delta_x)

            R_div_vector_delta_x_2 = multiply_matrix_scalar ( Yk_sub_P_x_transposed, 1/delta_x_2)


            Bk_previous = add_matrix_matrix(Bk_previous,R_div_vector_delta_x_2)

            print("vector_x: ", vector_x)

            n_iterations-=1

    return [-1, use_errors]