print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8])))

# filter() fonksiyonu birinci parametre olarak mutlaka mantıksal değer dönen
# (True , False) bir fonksiyon alır ve liste gibi veritiplerinin her bir elemanına bu
# fonksiyonunu uygular. *filter* sadece True sonuç çıkaran değerleri alarak bir tane
# *filter* objesi döner.

def asal_sayi_mi(x):
    i = 2

    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        while i < x:
            if x % i == 0:
                return False
            i += 1
        return True

print(list(filter(asal_sayi_mi,range(1,102))))


