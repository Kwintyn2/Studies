class calisan ():

    def __init__(self, isim = "None",maas ="None",depart = "None"):
        print("1. fonksiyon")
        self.isim = isim
        self.maas = maas
        self.depart = depart

    def bilgilerigoster(self):
        print("Calisan Bilgileri")

        print(f"İsim: {self.isim}\nMaas: {self.maas}\nDepartman: {self.depart}")

    def departmandegistir(self,depart):
        print("Departman Değiştirme")
        self.depart = depart

class yonetici(calisan):
    def __init__(self,isim = "None",maas ="None",depart = "None",rutbe = "None"):
        super().__init__(isim,maas,depart)
        print("2. Fonksiyon")
        self.rutbe = rutbe

class ust_yonetici(yonetici):
    def __init__(self,isim = "None",maas ="None",depart = "None",rutbe = "None",sene ="None"):
        super().__init__(isim,maas,depart,rutbe)
        self.sene = sene
    def bilgilerigoster(self):
        super().bilgilerigoster()
        print(f"Rutbe: {self.rutbe}")
        print(f"Sene {self.sene}")


ust_yonetici1 = ust_yonetici("Adnan",39_000,"GENEL","CEO" , 35)

ust_yonetici1.bilgilerigoster()


