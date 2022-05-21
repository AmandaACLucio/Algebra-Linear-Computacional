import json


def readTxtFile(path):
    with open(path, 'r') as f:
        content = f.readlines()
    return content


def readJsonFile(path):
    with open(path) as f:
        content = json.load(f)
    return content


def formatMatrix(matrix):
    newMatrix = []
    for i in matrix:
        newLine = i.replace('\n', '').split(' ')
        for j in range(len(newLine)):
            newLine[j] = float(newLine[j])
        newMatrix.append(newLine)
    print(matrix)
    return newMatrix


def writeOutputFile(content):
    with open('output.json', 'w') as outfile:
        json.dump(content, outfile, indent=4)


print(writeOutputFile({
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
