from hashlib import new
from src.task_4.newton_method import newton_method_nl
from src.task_4.broyden_method import broyden_method
from src.utils.files_operations import write_output_file
from src.utils.matrix_operations import value_function


class task_4:

    def __init__(self, ICOD, theta1, theta2, TOL_m):

        self.ICOD = ICOD
        self.theta1 = theta1
        self.theta2 = theta2
        self.TOL_m = TOL_m

    def run(self):

        content = {'values_c': [],
                   'useErrors': ''
                   }
        if(not isinstance(self.ICOD, int)):
            content['useErrors'] = "Insira um ICOD inteiro no arquivo de configurações"

        else:
            if(self.ICOD == 1):
                print("Newton Method")
                [values_c, use_errors] = [
                    newton_method_nl(self.theta1, self.theta2, self.TOL_m), 0]
                content['values_c'] = values_c
                content['useErrors'] = use_errors

            elif(self.ICOD == 2):
                print("Broyden Method")
                [values_c, use_errors] = broyden_method(
                    self.theta1, self.theta2, self.TOL_m)
                content['values_c'] = values_c
                content['useErrors'] = use_errors

            write_output_file(content)
