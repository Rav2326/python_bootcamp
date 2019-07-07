x = [[1, 12], [2, 1], [80, 100], [0, 45]]


def second(x):
    return x[1]

def xxx(x, y):             # to jest to samo co:
    return x + y


lll = second
print(lll([20, 30]))

xxx = lambda x, y: x + y   # to

print(xxx(10, 24))

print(sorted(x, key=lambda x: x[1]))
