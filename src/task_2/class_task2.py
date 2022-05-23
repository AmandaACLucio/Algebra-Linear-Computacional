from socket import fromfd
from src.task_2.metodo_jacobi import solver_jacobi
from src.utils.matrix_operations import laplace_determinant
from src.utils.files_operations import write_output_file

class task_2:

    def __init__(self, order, ICOD, IDET, matrix_a, TOL_m):

        self.order=order
        self.ICOD = ICOD
        self.IDET = IDET
        self.matrix_a = matrix_a
        self.TOL_m = TOL_m


    def run(self):

        content = {'eigen_values': [],
                'eigen_vectors': [],
                'useErrors': '',
                'determinant': 0,
                'convergenceInterationNumber': 0,
            }

        if(self.ICOD==1):
            print("Power Method")
            [eigen_values, eigen_vectors, steps] = [[],[], 0]
            content['eigen_values'] = eigen_values
            content['eigen_vectors'] = eigen_vectors
            content['convergenceInterationNumber'] = steps


        elif(self.ICOD==2):
            print("Jacobi Method")
            [eigen_values, eigen_vectors, steps] = solver_jacobi(self.matrix_a, self.TOL_m)
            content['eigen_values'] = eigen_values
            content['eigen_vectors'] = eigen_vectors
            content['convergenceInterationNumber'] = steps


        if(self.IDET>0):

            content["determinant"] = laplace_determinant(self.matrix_a)

        write_output_file(content)

        
