age = int(input("Yaşınızı Giriniz: "))

if age < 18:
    print("Yaşınız tutmuyor, lütfen {} sene sonra tekrar geliniz".format(18-age))

else:
    print("Hoşgeldiniz ! ")