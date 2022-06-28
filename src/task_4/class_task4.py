from hashlib import new
from src.task_4.newton_method import newton_method_nl
# from src.task_4.broyden_method import
from src.utils.files_operations import write_output_file


def get_equations(self, x):
    e1 = 2*x[1]**2 + x[0]**2 + 6*x[2]**2 - 1
    e2 = 8*x[1]**2 + 6*x[1]*x[0]**2 + 36*x[1] * \
        x[0]*x[2] + 108*x[1]*x[2]**2 - self.t1
    e3 = 60*x[1]**4 + 60*(x[1]**2)*(x[0]**2) + 576*(x[1]**2)*x[0]*x[2] + 2232*(x[1]**2)*(x[2]**2) + 252*(
        x[2]**2)*(x[0]**2) + 1296*(x[2]**3)*x[0] + 3348*x[2]**4 + 24*(x[0]**3)*x[2] + 3*x[0] - self.t2

    return [e1, e2, e3]


class task_4:

    def __init__(self, ICOD, t1, t2, TOL_m):

        self.ICOD = ICOD
        self.t1 = t1
        self.t2 = t2
        self.TOL_m = TOL_m

    def run(self):

        x0 = [1, 0, 0]
        content = {'read data': [],
                   'solution': [],
                   'useErrors': [],
                   }
        content['read data'] = [x0, self.t1, self.t2]

        if(not isinstance(self.ICOD, int) or (self.ICOD != 1 and self.ICOD != 2)):
            content['useErrors'] = "Insira um ICOD inteiro no arquivo de configurações"

        else:

            if(self.ICOD == 1):
                print("Newton")
                equations = get_equations(x0)
                [newton, use_errors] = newton_method_nl(
                    equations, x0)
                content['solution'] = newton
                content['useErrors'] = use_errors

            elif(self.ICOD == 2):
                print("Broyden")
                # [broyden, use_errors] = broyden_method(
                #     self.matrix_a, self.vector_b)
                # content['solution'] = broyden_method
                # content['useErrors'] = use_errors

            elif(not isinstance(self.TOL_m, float)):
                content['useErrors'] = "Insira uma valor de tolerância float no arquivo de configurações"

            write_output_file(content)
