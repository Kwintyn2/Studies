def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True


# Bütün değerler True ise True en az birisi False ise False döndürmek istiyoruz.
liste = [True, False, True, False, True]

liste = [1,2,3,4,5] # Daha önceden biliyoruz. 0' haricinde bütün sayılar True sayılmaktadır.

hepsi(liste) # Hepsi True ==== all(liste)
all(liste)

# /---------------------------------------------------------
def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False
# Herhangi bir değer True ise True, Hepsi False ise False döndürmek istiyoruz.

liste = [True,False,True,False,True]
herhangi(liste)
any(liste)











