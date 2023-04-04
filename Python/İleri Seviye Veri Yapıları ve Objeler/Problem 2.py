
# siir.txt dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek
# bir string oluşturun ve bu string'i ekrana yazdırın.

temiz_satirlar = list()

with open("siir.txt", "r", encoding= "utf-8") as file:
    satirlar = file.readlines()


for i in satirlar:
    i = i.strip()
    if i != "":
        temiz_satirlar.append(i)

bas_harfler = str()
for i in range(len(temiz_satirlar)):
    bas_harfler += temiz_satirlar[i][0]

print(bas_harfler)





