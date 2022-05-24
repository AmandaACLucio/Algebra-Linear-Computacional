from socket import fromfd
from src.task_1.decomposition.LU import solve_decomposition_LU
from src.task_1.decomposition.Cholesky import solve_by_cholesky
from src.task_1.iterative_procedure.Jacobi import jacobiano
#from src.task_1.iterative_procedure.Gauss_Seidel import
from src.utils.matrix_operations import laplace_determinant
from src.utils.files_operations import write_output_file

class task_1:

    def __init__(self, order, ICOD, IDET, matrix_a, vector_b, TOL_m):

        self.order=order
        self.ICOD = ICOD
        self.IDET = IDET
        self.matrix_a = matrix_a
        self.vector_b = vector_b
        self.TOL_m = TOL_m


    def run(self):

        content = {'solution': [],
                'useErrors': '',
                'determinant': 0,
                'convergenceInterationNumber': 0,
                'historical_residues': ''
            }

        if(self.ICOD==1):
            print("LU")
            soluction_LU = solve_decomposition_LU(self.matrix_a, self.vector_b)
            content['solution'] = soluction_LU

        elif(self.ICOD==2):
            print("Cholesky")
            soluction_Cholesky = solve_by_cholesky(self.matrix_a, self.vector_b)
            content['solution'] = soluction_Cholesky

        elif(self.ICOD==3):
            print("Jacobi")
            [soluction_Jacobi, historical_residues, step]= jacobiano(self.matrix_a, self.vector_b, self.TOL_m)
            content['solution'] = soluction_Jacobi
            content['convergenceInterationNumber'] = step
            content['historical_residues'] = historical_residues
        
        elif(self.ICOD==4):
            print("Gauss-Seidel")

        if(self.IDET>0):

            content["determinant"] = laplace_determinant(self.matrix_a)

        write_output_file(content)

        
