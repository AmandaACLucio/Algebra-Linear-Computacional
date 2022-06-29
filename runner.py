from src.task_1.class_task1 import task_1
from src.task_2.class_task2 import task_2
from src.task_3.class_task3 import task_3
from src.task_4.class_task4 import task_4
from src.task_5.class_task5 import task_5

from src.utils.files_operations import read_matrix_file, read_vector_file, read_json_file, read_pairs_file


def main(task):

    load_config = read_json_file("../../files/inputs/config.json")

    if(task == 1):

        matrix_a = read_matrix_file(load_config["Path_Matrix_A"])
        vector_b = read_vector_file(load_config["Path_Vector_B"])

        task_object = task_1(load_config["OrdemN"], load_config["ICOD"],
                             load_config["IDET"], matrix_a, vector_b, load_config["TOLm"])

        task_object.run()

    elif(task == 2):

        matrix_a = read_matrix_file(load_config["Path_Matrix_A"])

        task_object = task_2(load_config["OrdemN"], load_config["ICOD"],
                             load_config["IDET"], matrix_a, load_config["TOLm"])

        task_object.run()

    elif(task == 3):

        [values_x, values_y] = read_pairs_file(load_config["Path_Pairs"])

        task_object = task_3(
            load_config["ICOD"], load_config["Number_pairs_points"], load_config["xi"], values_x, values_y)

        task_object.run()

    elif(task == 4):

        task_object = task_4(
            load_config["ICOD"], load_config["theta1"], load_config["theta2"], load_config["TOLm"])

        task_object.run()

    elif(task == 5):

        task_object = task_5(
            load_config["ICOD"], load_config["c1"], load_config["c2"], load_config["c3"], load_config["c4"], load_config["TOLm"])

        task_object.run()


task = input("Escolha a task desejada ")
main(int(task))
