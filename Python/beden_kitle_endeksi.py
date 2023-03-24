print("""-------------
Beden Kitle Endeksi
-------------""")

def bti():
    while True:
        try:
            boy = float(input("Boyunuzu metre cinsinden giriniz: "))
            if boy <= 0:
                print("Sıfırdan küçük veya eşit bir değer girdiniz!")
                continue
            break
        except ValueError:
            print("Geçersiz Değer")

    while True:
        try:
            kilo = int(input("Kilonuzu kg cinsinden giriniz: "))
            break
        except ValueError:
            print("Hatalı Veri Lütfen Doğru Giriniz,\nÖrnek;80")

    input("Kitle endeksiniz için Enter'a basınız: ")

    indeks = kilo / (boy * 2)
    if indeks < 18.5:
        print(f"BTI = {indeks:.2f}\nDurum: Zayıf")

    elif 18.5 < indeks < 25:
        print(f"BTI = {indeks:.2f}\nDurum: Normal")

    elif 25 < indeks < 30:
        print(f"BTI = {indeks:.2f}\nDurum: Kilolu")

    elif indeks > 30:
        print(f"BTI = {indeks:.2f}\nDurum: Obez")



bti()

