# EKOK (EN KUCUK ORTAK KAT)
def find_ekok(a, b):
    sayi = max(a, b)
    while True:
        if sayi % a == 0 and sayi % b == 0:
            return sayi
        sayi += 1

while True:
    a = input("Ekok Bulmak istediğiniz 1. sayı: ")
    if a == 'q':
        exit("Program Bittiğğ")
    b = input("Ekok Bulmak istediğiniz 2. sayı: ")
    if a == 'q':
        exit("Program Bittiğğ")
    else:
        a, b = int(a), int(b)
    print("EKOK: ",find_ekok(a,b))


