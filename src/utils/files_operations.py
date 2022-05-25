import json
import os

def read_txt_file(path):
    with open(path, 'r') as f:
        content = f.readlines()
    return content


def read_json_file(path):
    
    path = os.path.join(os.path.dirname(__file__), path)

    with open(path, encoding='utf-8-sig') as f:
        content = json.load(f)
    return content


def format_matrix(matrix):
    newMatrix = []
    for i in matrix:
        newLine = i.replace('\n', '').split(' ')
        for j in range(len(newLine)):
            newLine[j] = float(newLine[j])
        newMatrix.append(newLine)
    print(matrix)
    return newMatrix

def write_output_file(content):

    path = "..\\..\\files\\outputs\\output.json"
    path = os.path.join(os.path.dirname(__file__), path)

    with open(path, 'w') as outfile:
        print(content)
        json.dump(content, outfile, indent=4)

def read_matrix_file(path):
    
    path = os.path.join(os.path.dirname(__file__), path)


    with open(path, 'r',  encoding='utf-8-sig') as f:
        content = f.readlines()
    
    matrix = []
    for line in content:
        matrix.append([float(n) for n in line.split()])
    print(matrix)

    return matrix

def read_vector_file(path):
    
    path = os.path.join(os.path.dirname(__file__), path)


    with open(path, 'r',  encoding='utf-8-sig') as f:
        content = f.readlines()
    
    matrix = []
    for line in content:
        matrix.append(float(line.split()[0]))
    return matrix

def read_pairs_file(path):
    
    path = os.path.join(os.path.dirname(__file__), path)


    with open(path, 'r', encoding='utf-8-sig') as f:
        content = f.readlines()
    
    values_x = []
    values_y = []
    for line in content:
        [x, y] = line.split()
        values_x.append(float(x))
        values_y.append(float(y))

    return [values_x, values_y]
