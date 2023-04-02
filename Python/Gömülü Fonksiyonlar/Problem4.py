

isimler = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]

soyisimler = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

list2 = list(zip(isimler, soyisimler))

for i in range(len(list2)):
    print(f"{list2[i][0]:>10} {list2[i][1]:5} ")

