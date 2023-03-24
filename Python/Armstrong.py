

toplam = 0

while True:
    sayi = input("Bir Sayi Giriniz: ")
    basamak = len(sayi)

    for i in range(0, basamak):
        s = int(sayi[i])
        print("{}. Sayı= {}".format(i+1, s))
        toplam += s ** basamak

    if toplam == int(sayi):
        print("Armstrong Sayisi", "\nSayi:", sayi, "\nToplam:", toplam)
        toplam = 0

    else:
        print("Sayi:", sayi, "\nToplam= :", toplam, "\nArmstrong değil")
        toplam = 0










