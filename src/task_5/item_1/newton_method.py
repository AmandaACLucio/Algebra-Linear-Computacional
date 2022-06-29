from src.utils.matrix_operations import function_task5, get_derivative_task5
import math

STEPS = 1000


def newton_method(consts, x, TOL=0):

    for _ in range(STEPS):
        xi = x - function_task5(consts, x) / get_derivative_task5(consts, x)
        residue = math.fabs(xi - x)
        if(residue < TOL):
            print("Raiz: " + str(xi))
            return xi

        x = xi

    print("A função não convergiu")
