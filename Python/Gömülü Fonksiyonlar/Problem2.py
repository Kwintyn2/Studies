
def ucgen_mi(x):
    if x[0] + x[1] > x[2] and x[0] + x[2] > x[1] and x[1] + x[2] > x[0]:
        return True
    else:
        return False


list1 = [(3,4,5),(6,8,10),(3,10,7)]


print(list(filter(ucgen_mi, list1)))

