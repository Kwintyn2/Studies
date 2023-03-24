

bolumliste = list()
zero = 0
while True:
    sayi = input("Bir sayi giriniz: ")
    if sayi == "q":
        print("Çıkış")
        break
    else:
        sayi = int(sayi)

    for i in range(1, sayi):
        if sayi % i == 0:
            zero += i
    if zero == sayi:
        print("Mükemmel")
        zero = 0
    else:
        print("Mükemmel değil")
        zero = 0





