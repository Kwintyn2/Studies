
a = input("1. Sayı: ")
b = input("2. Sayi: ")

a , b = int(a) , int(b)

bolen_a = list()
bolen_b = list()
ortak = list()

for i in range(1,a+1):
    if a % i == 0:
        bolen_a.append(i)

for i in range(1,b+1):
    if b % i == 0:
        bolen_b.append(i)

for i in bolen_a:
    for y in bolen_b:
        if i == y:
            ortak.append(y)


print(bolen_a)
print(bolen_b)
print(ortak)
print(ortak[len(ortak)-1])































