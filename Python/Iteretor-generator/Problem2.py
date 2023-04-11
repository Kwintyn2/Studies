
def asal_sayi():
    for i in range(2, 101):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i



generator = asal_sayi()

print(type(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

for i in generator:
    print(i)













