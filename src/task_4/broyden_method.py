from src.task_2.metodo_jacobi import inverse_matrix
from src.utils.matrix_operations import multiply_matrix_scalar, add_vector_vector, multiply_vector_scalar, multiply_vector_vector, sub_vector_vector, norm_vector, multiply_matrix_vector, value_function, sub_matrix_matrix

def broyden_method(vector_x, phi_1, phi_2, max_tolerance=0, n_iterations=0):

    Bk_previous = []
    vector_x_previous=[]

    for i in range(1, n_iterations):
        matrix_J = Bk_previous
        vector_delta_x = multiply_matrix_scalar(multiply_matrix_vector( inverse_matrix(matrix_J),value_function(vector_x, phi_1, phi_2))[0] ,-1)

        vector_x = add_vector_vector(vector_x, vector_delta_x)

        vector_y = sub_vector_vector(value_function(vector_x, phi_1, phi_2), value_function(vector_x_previous, phi_1, phi_2))

        tolk = norm_vector(vector_delta_x)/norm_vector(vector_x)

        if(tolk<max_tolerance):

            return vector_x

        else:

            Bk_previous_x_vector_delta_x= multiply_matrix_vector(Bk_previous, vector_delta_x)[0] #P 

            Yk_sub_P = sub_matrix_matrix(vector_y, Bk_previous_x_vector_delta_x) #Q

            Q_mult_vector_delta_x = multiply_matrix_vector(Yk_sub_P, vector_delta_x)[0] #R

            R_div_vector_delta_x_2 = multiply_vector_scalar( Q_mult_vector_delta_x, 1/multiply_vector_vector( vector_delta_x, vector_delta_x)[0]) #S


            Bk_current = Bk_previous + R_div_vector_delta_x_2

    return -1