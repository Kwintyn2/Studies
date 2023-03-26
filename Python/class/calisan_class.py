
class calisan ():

    def __init__(self,isim,maas,depart):
        print("calisan sinifinin init fonksiyonu")

        self.isim = isim
        self.maas = maas
        self.depart = depart

    def bilgilerigoster(self):
        print("Calisan Bilgileri")

        print(f"İsim: {self.isim}\nMaas: {self.maas}\nDepartman: {self.depart}")

    def departmandegistir(self,depart):
        print("Departman Değiştirme")
        self.depart = depart

calisan1 = calisan("Ali",1500,"IT")

calisan1.bilgilerigoster()

calisan1.departmandegistir("İnsan Kaynakları")

calisan1.bilgilerigoster()

print("_________________________")

class yönetici(calisan):
    def zam_yap(self,zammiktari):
        self.maas += zammiktari

yönetici1 = yönetici("Mehmet Müdür", 1500 , "Yönetici")

yönetici1.bilgilerigoster()

yönetici1.zam_yap(1500)

yönetici1.bilgilerigoster()















