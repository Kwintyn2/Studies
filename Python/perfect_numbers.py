

bolumliste = list()
zero = 0

for sayi in range(1, 1000):
    for i in range(1, sayi):
        if sayi % i == 0:
            zero += i
    if zero == sayi:
        bolumliste.append(sayi)
        zero = 0
    else:
        zero = 0

print(bolumliste)
