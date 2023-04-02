from functools import reduce

def toplama(x, y):
    return x + y


print(reduce(toplama, [1, 2, 3, 4, 5]))  # 1+2=3 / 3+3=6 / 6+4=10 / 10+5=15

