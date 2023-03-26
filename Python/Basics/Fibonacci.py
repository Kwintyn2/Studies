


a = 1
b = 1
fibonaccis = list()
fibonaccis.append(a)
fibonaccis.append(b)

for i in range(20):
    a += b
    fibonaccis.append(a)
    b += a
    fibonaccis.append(b)

print(fibonaccis)

