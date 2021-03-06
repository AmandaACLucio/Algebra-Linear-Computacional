from src.utils.matrix_operations import multiply_vector_vector

def solver_interpolation(values_x, values_y, xi):
    
    use_errors = []

    if(len(values_x)!=len(values_y)):
        str_error = "A quantidade de parâmetros x deve ser igual a de parâmetro y"
        use_errors.append(str_error)
        return ["undefined", use_errors]

    count_x = len(values_x)

    phis = []

    for i in range(count_x):

        product_numerator = 1
        product_denominator = 1
        for j in range(count_x):

            if i != j:
                
                product_numerator *=(xi-values_x[j])
                product_denominator *=(values_x[i]-values_x[j])
        
        phis.append(product_numerator/product_denominator)

    value_y_to_xi = multiply_vector_vector(phis, values_y)

    return [value_y_to_xi, use_errors]
