from src.utils.matrix_operations import function_task5
import math


def bissection_method(consts, a, b, TOL=0):
    if function_task5(consts, a)*function_task5(consts, b) > 0:
        print("Erro! Não é possível afirmar se o intervalo contém raiz")
        return

    c = a
    while(math.fabs(b - a) >= TOL):

        c = (a+b)/2.0
        function_i = function_task5(consts, c)
        if(function_i == 0):
            break

        if (function_i*function_task5(consts, a) < 0):
            b = c
        else:
            a = c

    print("Raiz: " + str(c))
    return c
