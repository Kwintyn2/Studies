def not_hesaplama(line):
    line = line.split(",")
    final_not = int((int(line[1]) * (3 / 10)) + (int(line[2]) * (3 / 10)) + (int(line[3]) * (4 / 10)))

    if final_not >= 90:
        harf_notu = "AA"
    elif final_not >= 85:
        harf_notu = "BA"
    elif final_not >= 80:
        harf_notu = "BB"
    elif final_not >= 75:
        harf_notu = "CB"
    elif final_not >= 70:
        harf_notu = "CC"
    elif final_not >= 65:
        harf_notu = "DC"
    elif final_not >= 60:
        harf_notu = "DD"
    elif final_not >= 55:
        harf_notu = "FD"
    else:
        harf_notu = "FF"

    return harf_notu


notlar = dict()

with open("not_hesaplama.txt", "r", encoding="utf-8") as file:
    for i in file:
        open("notlar.txt", "a", encoding="utf-8").write(f"{(i.split(','))[0]:20}=======>{not_hesaplama(i):>5}\n")

open("notlar.txt", "a", encoding="utf-8").close()


