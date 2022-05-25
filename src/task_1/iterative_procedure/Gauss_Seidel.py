from src.utils.matrix_operations import converges, is_square_matrix, value_residue


def gauss_seidel(matrix, vector_b, max_tolerance):

    lines = len(matrix)

    if(not is_square_matrix(matrix)):
        print("A matriz precisa ser quadrada para realizar essa operação")
        return -1

    if(not converges(matrix)):
        print("A matriz não converge para o método jacobiano")
        return -1

    vector_old = [1 for x in range(lines)]
    vector_new = [0 for x in range(lines)]
    residue = 1
    residue_historic = [1]
    step = 0

    while(residue >= max_tolerance):
        for i in range(lines):
            vector_new[i] = vector_b[i]

            for j in range(lines):

                if(i > j):
                    vector_new[i] -= matrix[i][j]*vector_new[j]
                
                if(i < j):
                    vector_new[i] -= matrix[i][j]*vector_old[j]

            vector_new[i] /= matrix[i][i]

        residue = value_residue(vector_new, vector_old)
        residue_historic.append(residue)

        for i in range(lines):
            vector_old[i] = vector_new[i]

        step += 1

    return [vector_new, residue_historic, step]