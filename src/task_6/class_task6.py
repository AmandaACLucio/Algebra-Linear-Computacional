from src.task_6.runge_kutta_nystron import solve_runge_kutta_nystron
from src.utils.files_operations import write_output_file


class task_6:

    def __init__(self, integration_step, integration_time, value_m, value_c, value_k, list_a, list_w):

        self.integration_step = integration_step
        self.integration_time = integration_time
        self.value_m = value_m
        self.value_c = value_c
        self.value_k = value_k
        self.list_a = list_a
        self.list_w = list_w

    def run(self):

        content = {'solution': [],
                   'useErrors': ''
                   }

        print("Integral Definida")

        [solution, use_errors] = solve_runge_kutta_nystron(self.integration_step, self.integration_time, self.value_m, self.value_c, self.value_k, self.list_a, self.list_w)

        content['path_solution_csv'] = solution
        content['useErrors'] = use_errors

        write_output_file(content)
