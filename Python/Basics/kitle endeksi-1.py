while True:
    try:
        boy = float(input("Boyunuzu Metre Cinsinden Giriniz: "))
        kilo = float(input("Kilo Giriniz: "))
        break
    except ValueError:
        print("Hatalı girdi, Tekrar Deneyiniz:")


print(f"Beden Kitle Endeksiniz: {kilo/(boy ** 2):.2f}")
