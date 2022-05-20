import json

def readTxtFile(path):
    with open(path, 'r') as f:
        content = f.readlines()
    return content

def readJsonFile(path):
    with open(path) as f:
        content = json.load(f)
    return content

readTxtFile("C:/Algebra-Linear-Computacional/src/task 1/file.txt")