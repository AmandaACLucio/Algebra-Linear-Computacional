from src.task_5.item_1.bissection_method import bissection_method
from src.task_5.item_1.newton_method import newton_method
from src.task_5.item_2.integral_defined import solve_integral_defined
from src.task_5.item_4.Richard_extrapolation import solve_derivative_richard

from src.utils.files_operations import write_output_file


class task_5:

    def __init__(self, ICOD, c1, c2, c3, c4, TOL_m, count_points_integration, point_a, point_b,/ method_integral_defined, point_richard, value_delta_x1, value_delta_x2):

        self.ICOD = ICOD
        self.consts = [c1, c2, c3, c4]
        self.TOL_m = TOL_m
        self.point_a = point_a
        self.point_b = point_b
        self.method_integral_defined = method_integral_defined
        self.count_points_integration = count_points_integration
        self.point_richard = point_richard
        self.value_delta_x1 = value_delta_x1
        self.value_delta_x2 = value_delta_x2


    def run(self):

        content = {'solution': [],
                   'useErrors': ''
                   }
        if(not isinstance(self.ICOD, int)):
            content['useErrors'] = "Insira um ICOD inteiro no arquivo de configurações"

        else:
            if(self.ICOD == 1):
                [solution, use_errors] = [0, 0]
                print("Raiz")
                # Defina aqui os valores do intervalo a ser utilizado
                a = 1
                b = 10
                method = input(
                    'Escolha o método desejado: \n 1 - Bisseção,\n 2 - Newton \n')
                if(method == '1'):

                    [solution, use_errors] = [
                        bissection_method(self.consts, a, b, self.TOL_m), 0]
                elif(method == '2'):
                    [solution, use_errors] = [
                        newton_method(self.consts, x, self.TOL_m), 0]
                
                else:
                    print("Erro! Método inválido")

                content['solution'] = solution
                content['useErrors'] = use_errors
            
            elif(self.ICOD == 2):

                print("Integral Definida")

                [solution, use_errors] = solve_integral_defined(self.point_a, self.point_b, self.count_points_integration, self.method_integral_defined)

                content['solution'] = solution
                content['useErrors'] = use_errors

            elif(self.ICOD == 4):

                print("Derivada pelo método de Richard")

                [solution, use_errors] = solve_integral_defined(self.point_richard, self.value_delta_x1, self.value_delta_x2)

                content['solution'] = solution
                content['useErrors'] = use_errors
            elif(self.ICOD == 2):
                print("Integral")

            elif(self.ICOD == 3):
                print("Derivada DF")
            elif(self.ICOD == 4):
                print("Derivada RE")

            write_output_file(content)
