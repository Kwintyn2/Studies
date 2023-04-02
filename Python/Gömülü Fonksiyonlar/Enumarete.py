
#Yani aslında burada herbir elemanı indekslerle numaralandırıyor ve demet çiftleri oluşturuyoruz.
# *for döngüsü* yazarken bazen hem elemanları hem de indeksleri almak isteyebiliriz.
# Böyle bir durumda numaralandırma işlemi yapan *enumerate* fonksiyonunu kullanabiliriz.

liste = ["Elma", "Armut", "Muz", "Kiraz"]

# sonucu [(0,'Elma'),(1,'Armut'),(2,'Muz'),(3,'Kiraz')] yapmak istiyoruz.

sonuç = list()

i = 0

for a in liste:
    sonuç.append((i, a))
    i += 1
print(sonuç)







