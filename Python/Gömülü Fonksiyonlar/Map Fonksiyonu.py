

# Pythonda gömülü bir fonksiyon olan *map()* fonksiyonunun yapısı şu şekildedir.
#
#                 map(fonksiyon,iterasyon yapılabilecek veritipi(liste,demet vb),....)
#
# *map()* fonksiyonu ilk parametre olarak bir tane fonksiyon objesi alır.
# (Fonksiyonlar da birer obje olduğu için başka bir fonksiyona gönderilebilir.)
# 2. parametre olarak da bir tane iterasyon yapılacak veritipi alarak ,
# gönderilen fonksiyonu her bir eleman üzerinde uygulayarak sonuçları bir *map* objesi olarak döner.




def double(x):
    return x * 2

list1 = list()
for i in range(1,20):
    list1.append(double(i))
print(list1)


print(list(map(double, [*range(1, 20)])))

print(list(map(lambda x: x * 2, (range(1, 20)))))

list1 = [1, 2, 3, 4, 5, 6]
list2 = [12, 22, 33, 66]
list3 = [15, 26, 13, 34, 25, 76, 11]

print(list(map(lambda x, y, z: x * y * z, list1, list2, list3)))


