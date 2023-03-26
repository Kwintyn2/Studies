print("""*******************

TOPLAMA MAKİNASI

*******************

Toplamı Görmek İçin 'q''ya Basınız


*******************

Toplamak İstediğiniz Sayıları Giriniz 

*******************
""")
toplam = 0

for i in range(999):
    try:
        sayi = input(f"Sayi {i}: ")
        if sayi == 'q':
            print("Sayılarinizin Toplami: {}".format(toplam))
            break
        toplam += int(sayi)
    except ValueError:
        print("O sayı mı AAA")