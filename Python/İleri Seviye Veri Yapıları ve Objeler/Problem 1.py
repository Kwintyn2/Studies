# Problem 1
# Elinizde uzunca bir string olsun.
#
#             "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
#
#
# Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.

str1 = "ProgramlamaÖdeviileriSeviyeVeriYapılarıveObjeleripynb".lower()
set1 = set(str1)

dict1 = dict()

for i in set1:
    dict1[i] = str1.count(i)
for harf , sayi in dict1.items():
    print(f"'{harf}' harfi {sayi} defa geçiyor")


