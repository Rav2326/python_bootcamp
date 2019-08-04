a = [[10, 20], [30, 40]]
b = [[11, 22], [33, 44, 10]]


def add(*args):

    sizes = set()


    result = []
    for i in range(len(args[0])):
        row = []
        for j in range(len(args[0][i])):
            x = 0
            for m in args:
                x += m[i][j]
            row.append(x)
        result.append(row)
    return result

print(add(a, b))