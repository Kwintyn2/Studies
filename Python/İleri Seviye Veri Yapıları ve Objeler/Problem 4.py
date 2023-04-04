# Problem 4
# Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek ,
# ekrana isim ve soyisimleri *isimlere* göre sıralı bir şekilde yazdırmaya çalışın.
#
#         isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
#
#         soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]


isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

isim_soyisimler = list(zip(isimler,soyisimler))

print(isim_soyisimler)
isim_soyisimler.sort()
print(isim_soyisimler)

for i,j in isim_soyisimler:
    print(i,j)