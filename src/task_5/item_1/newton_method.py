from src.utils.matrix_operations import function_task5, get_derivative_task5
import math

STEPS = 1000


def bissection_method(consts, a, b, TOL=0):

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


def newton_method(consts, x, TOL=0):

    for _ in range(STEPS):
        xi = x - function_task5(consts, x) / get_derivative_task5(consts, x)
        residue = math.fabs(xi - x)

        if(residue < TOL):
            print("Raiz: " + str(xi))
            return xi

        x = xi

    print("A função não convergiu")
