from functools import reduce

list1 = [1,2,3,4,5,6,7,8,9,10]


print(reduce(lambda x, y: x + y, list(filter(lambda x: x % 2 == 0, list1))))

#veya
list2 = list(filter(lambda x: x % 2 == 0, list1))

print(reduce(lambda x, y: x + y, list2))