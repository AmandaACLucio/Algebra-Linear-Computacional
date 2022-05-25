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

        if(self.ICOD==1):
            print("Interpolation")
            value_y_to_xi = solver_interpolation(self.values_x, self.values_y, self.xi)
            content['value_y_to_xi'] = value_y_to_xi


        elif(self.ICOD==2):
            print("Regression Multilinear")
            value_y_to_xi = find_value(self.values_x, self.values_y, self.xi)
            content['value_y_to_xi'] = value_y_to_xi


        write_output_file(content)

        
