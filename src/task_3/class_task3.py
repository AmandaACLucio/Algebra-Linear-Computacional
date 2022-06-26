from src.task_3.multi_regression import find_value
from src.task_3.interpolation import solver_interpolation
from src.utils.files_operations import write_output_file


class task_3:

    def __init__(self, ICOD, N, xi, values_x, values_y):

        self.ICOD = ICOD
        self.N = N
        self.xi = xi
        self.values_x = values_x
        self.values_y = values_y


    def run(self):

        content = {'value_y_to_xi': [],
                'useErrors': ''
            }
        if(not isinstance(self.ICOD, int)):
            content['useErrors'] = "Insira um ICOD inteiro no arquivo de configurações"
        
        else:
            if(self.ICOD==1):
                print("Interpoletion")
                [value_y_to_xi, use_errors]  = solver_interpolation(self.values_x, self.values_y, self.xi)
                content['value_y_to_xi'] = value_y_to_xi
                content['useErrors'] = use_errors

            elif(self.ICOD==2):
                print("Regression Multilinear")
                [value_y_to_xi, use_errors] = find_value(self.values_x, self.values_y, self.xi)
                content['value_y_to_xi'] = value_y_to_xi
                content['useErrors'] = use_errors


            write_output_file(content)

        
