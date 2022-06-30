import os
import matplotlib.pyplot as plt
import pandas as pd
from src.utils.matrix_operations import function_task6, derivative_function_task6

def solve_runge_kutta_nystron(integration_step, integration_time, value_m, value_c, value_k, list_a, list_w):

    use_errors = []

    try:
        total_steps = int(integration_time / integration_step)+1
    
    except:

        use_errors.append("Insira um valor de tempo de integração diferente de 0")

        return (-1, use_errors)
    
    size_step = integration_step
    half_size_step = size_step/2

    value_displacement = value_velocity = value_time_current = 0

    value_aceleration = derivative_function_task6(value_time_current, value_displacement, value_velocity,  value_c, value_m, value_k, list_a, list_w)

    list_define_moment_dict = []

    moment_dict = {'time': value_time_current, 'displacement': value_displacement, 'velocity': value_velocity, 'acceleration': value_aceleration}

    list_define_moment_dict.append(moment_dict)

    path_csv_file = os.path.join(os.path.dirname(__file__),"../../files/outputs/Teste_6/runge_kutta_nystron.csv")
    path_graph = os.path.join(os.path.dirname(__file__),"../../files/outputs/Teste_6/moments.png")

    for k in range(1, total_steps):

        K1 = half_size_step*derivative_function_task6(value_time_current, value_displacement, value_velocity, value_c, value_m, value_k, list_a, list_w)

        value_Q = half_size_step*(value_velocity+0.5*K1)

        K2 = half_size_step*derivative_function_task6(value_time_current+half_size_step, value_displacement+value_Q, value_velocity+K1,  value_c, value_m, value_k, list_a, list_w)

        K3 = half_size_step*derivative_function_task6(value_time_current+half_size_step, value_displacement+value_Q, value_velocity+K2,  value_c, value_m, value_k, list_a, list_w)

        value_L = size_step*(value_velocity+K3)

        K4 = half_size_step*derivative_function_task6(value_time_current+size_step, value_displacement+value_L, value_velocity+2*K3,  value_c, value_m, value_k, list_a, list_w)

        value_time_current = k*size_step

        value_displacement = value_displacement + size_step*(value_velocity+(K1+K2+K3)/3)

        value_velocity = value_velocity+(K1+2*K2+2*K3+K4)/3
        
        value_aceleration = derivative_function_task6(value_time_current,value_displacement, value_velocity,  value_c, value_m, value_k, list_a, list_w)

        moment_dict = {'time': value_time_current, 'displacement': value_displacement, 'velocity': value_velocity, 'acceleration': value_aceleration}

        list_define_moment_dict.append(moment_dict)

    dataframe = pd.DataFrame.from_dict(list_define_moment_dict)

    if os.path.exists(path_csv_file):
        os.remove(path_csv_file)

    dataframe.to_csv(path_csv_file, index=False)
    dataframe.plot(x='time', y=['displacement','velocity','acceleration'])

    plt.show()

    plt.savefig(path_graph)


    return [list_define_moment_dict, use_errors]