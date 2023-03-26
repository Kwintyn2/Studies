print("Merhaba")

while True:
    try:
        sekil = int(input("Üçgen için 3\nDörtgen için 4'e Basınız"))
        if sekil == 3 or sekil == 4:
            if sekil == 3:
                kenar1 = float(input("1. Kenarı Giriniz: "))
                kenar2 = float(input("2. Kenarı Giriniz: "))
                kenar3 = float(input("3. Kenarı Giriniz: "))
                input("Üçgeninizin Tipini Görmek İçin Enter'a Basınız")

                if kenar1 + kenar2 > kenar3 and kenar1 + kenar3 > kenar2 and kenar2 + kenar3 > kenar1:

                    if kenar1 == kenar2 == kenar3:
                        print("Eşkenar Üçgen")

                    if kenar1 == kenar2 != kenar3 or kenar1 != kenar2 == kenar3 or kenar1 == kenar3 != kenar2:
                        print("İkizkenar Üçgen")
                    elif kenar1 != kenar2 != kenar3:
                        print("Düz Üçgen")
                else:
                    print("Üçgen Değilsin sen")
            kenarlar = []
            if sekil == 4:
                for i in range(4):
                    kenar = float(input("{}. Kenarı Giriniz: ".format(i + 1)))
                    kenarlar.append(kenar)
                if len(set(kenarlar)) == 1:
                    print("Kare veya Eşkenar bir dörtgen")

                elif    kenarlar[0] == kenarlar[1] and kenarlar[2] == kenarlar[3] or\
                        kenarlar[0] == kenarlar[2] and kenarlar[1] == kenarlar[3] or\
                        kenarlar[0] == kenarlar[3] and kenarlar[1] == kenarlar[2]:
                    print("Dik bir dörtgen")

                else:
                    print("Bozuk bir dörtgen")
        else:
            print("3 veya 4 yaz!!!!!!!")
    except:
        print("Hatalı VERİ Başa döndün!")
