a = input("Birinci sayı: ")
b = input("İkinci sayı: ")

print("Değiştirilmeden önce a = ", a, " ve b = ", b)
input("Devam etmek için bir tuşa basın...")

a, b = b, a

print("Değiştirildikten sonra a = ", a, " ve b = ", b)