from re import A
from src.task_5.item_1.bissection_method import bissection_method
from src.task_5.item_1.newton_method import newton_method
from src.task_5.item_3.derivative import backward_step, central_difference, forward_step
from src.task_5.item_2.integral_defined import solve_integral_defined
from src.task_5.item_4.derivative_richard import solve_derivative_richard

from src.utils.files_operations import write_output_file


class task_5:

    def __init__(self, ICOD, c1, c2, c3, c4, a, b, delta_x, TOL_m, count_points_integration, point_a, point_b, method_integral_defined, point_richard, value_delta_x1, value_delta_x2):

        self.ICOD = ICOD
        self.consts = [c1, c2, c3, c4]
        self.a = a
        self.b = b
        self.delta_x = delta_x
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
                method = input(
                    'Escolha o método desejado: \n 1 - Bisseção,\n 2 - Newton \n')
                if(method == '1'):
                    print('Método da Bisseção')
                    [values_c, use_errors] = [
                        bissection_method(self.consts, self.a, self.b, self.TOL_m), 0]
                elif(method == '2'):
                    print('Método de Newton')

                    x = self.a+self.b/2.0
                    [values_c, use_errors] = [
                        newton_method(self.consts, x, self.TOL_m), 0]

                else:
                    print("Erro! Método inválido")

                content['solution'] = solution
                content['useErrors'] = use_errors

            elif(self.ICOD == 2):

                print("Integral Definida")

                [solution, use_errors] = solve_integral_defined(
                    self.point_a, self.point_b, self.count_points_integration, self.method_integral_defined)

                content['solution'] = solution
                content['useErrors'] = use_errors

            elif(self.ICOD == 3):
                print("Derivada DF")
                method = input(
                    'Escolha o método de diferença finita desejado: \n 1 - Passo a frente \n 2 - Passo atrás \n 3 - Central \n')
                if(method == '1'):
                    print("Diferença finita passo a frente")
                    [values_c, use_errors] = [forward_step(
                        self.consts, self.a, self.delta_x), 0]

                if(method == '2'):
                    print("Diferença finita passo atrás")
                    [values_c, use_errors] = [backward_step(
                        self.consts, self.a, self.delta_x), 0]

                if(method == '3'):
                    print("Diferença finita central")
                    [values_c, use_errors] = [central_difference(
                        self.consts, self.a, self.delta_x), 0]

                content['solution'] = values_c
                content['useErrors'] = use_errors


            elif(self.ICOD == 4):

                print("Derivada pelo método de Richard")

                [solution, use_errors] = solve_derivative_richard(
                    self.point_richard, self.value_delta_x1, self.value_delta_x2)

                content['solution'] = solution
                content['useErrors'] = use_errors

            write_output_file(content)
