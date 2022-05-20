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

print(formatMatrix(readTxtFile("C:/Algebra-Linear-Computacional/src/task 1/file.txt")))