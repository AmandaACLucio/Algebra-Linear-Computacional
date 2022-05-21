import json

def read_txt_file(path):
    with open(path, 'r') as f:
        content = f.readlines()
    return content


def read_json_file(path):
    with open(path) as f:
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
    with open('output.json', 'w') as outfile:
        json.dump(content, outfile, indent=4)


print(write_output_file({
    'solution': {
        'x': 1,
        'y': 1,
        'z': 1
    },
    'useErrors': '',
    'det': 0,
    'convergenceInterationNumber': 0,
    'tol': ''
}))
