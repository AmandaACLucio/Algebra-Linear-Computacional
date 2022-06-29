from src.task_5.item_1.bissection_method import bissection_method
from src.task_5.item_1.newton_method import newton_method

from src.utils.files_operations import write_output_file


class task_5:

    def __init__(self, ICOD, c1, c2, c3, c4, TOL_m):

        self.ICOD = ICOD
        self.consts = [c1, c2, c3, c4]
        self.TOL_m = TOL_m

    def run(self):

        content = {'solution': [],
                   'useErrors': ''
                   }
        if(not isinstance(self.ICOD, int)):
            content['useErrors'] = "Insira um ICOD inteiro no arquivo de configurações"

        else:
            if(self.ICOD == 1):
                [values_c, use_errors] = [0, 0]
                print("Raiz")
                # Defina aqui os valores do intervalo a ser utilizado
                a = 1
                b = 10
                method = input(
                    'Escolha o método desejado: \n 1 - Bisseção,\n 2 - Newton \n')
                if(method == '1'):

                    [values_c, use_errors] = [
                        bissection_method(self.consts, a, b, self.TOL_m), 0]
                elif(method == '2'):
                    x = a+b/2.0
                    [values_c, use_errors] = [
                        newton_method(self.consts, x, self.TOL_m), 0]
                else:
                    print("Erro! Método inválido")

                content['solution'] = values_c
                content['useErrors'] = use_errors
            elif(self.ICOD == 2):
                print("Integral")

            elif(self.ICOD == 3):
                print("Derivada DF")
            elif(self.ICOD == 4):
                print("Derivada RE")

            write_output_file(content)
