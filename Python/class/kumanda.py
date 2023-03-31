import time
import random

print("""
Televizyon Uygulaması
1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Silme
6. Kanal Yeri Değiştirme
7. Kaynak Değiştirme
8. Kanal Sayısını Öğrenme
9. Rastgele Kanala Geçme
10. Televizyon Bilgileri
Çıkmak için 'q' ya basın.
""")

class Kumanda():
    def __init__(self,kanal = "TRT", tv_durum = "Kapalı",ses_duzeyi = 15,kanal_listesi = ["TRT","ATV"], kaynak = ["HDMI", "TV-Uydu", "CD/DVD", "USB"]):
        self.tv_durum = tv_durum
        self.ses_duzeyi = ses_duzeyi
        self.kanal_listesi = kanal_listesi
        self.kaynak = kaynak
        self.kanal = kanal

    def tv_durum1(self):
        if self.tv_durum == "Kapalı":
            self.tv_durum = "Açık"
            print ("TV Açılıyor")
        elif self.tv_durum == "Açık":
            self.tv_durum = "Kapalı"
            print("TV Kapatılıyor")
    def ses_ayari1(self):
        print(f"Ses Duzeyi= {self.ses_duzeyi}Ses Ayarlari min-1 max-30")
        while True:
            a = input("Sesi Arttirmak İcin +\nAzaltmak İcin -")
            if a == "+":
                if self.ses_duzeyi < 30:
                    print(f"Ses Arttırılıyor.. Duzey = {self.ses_duzeyi}")
                    time.sleep(1)
                    self.ses_duzeyi += 1
                else:
                    print("Ses Düzeyi Max 30 olabilir")

            elif a == "-":
                if self.ses_duzeyi > 1:
                    print(f"Ses Azaltılıyor.. Duzey = {self.ses_duzeyi}")
                    time.sleep(1)
                    self.ses_duzeyi += -1
                else:
                    print("Ses Düzeyi Min 1 olabilir")
                    time.sleep(1)
            else:
                print("Ses Ayarlarından Çıkılıyor...")
                break
    def kanal_ekle(self,eklenecek_kanal):
        self.kanal_listesi.append(eklenecek_kanal)
        time.sleep(1)
        print("Kanalınız Eklendi.. {}".format(eklenecek_kanal))
    def kanal_silme(self):
        onay = input("Mevcut kanal silinecek emin misiniz ? y/n")
        if onay == "y":
            self.kanal_listesi.remove(self.kanal)
            self.kanal = self.kanal_listesi[0]
            print("Kanalınız Silindi")
            print("Kanal = ", self.kanal)

        elif onay == "n":
            print("Silme İptal Edildi")
        else:
            print("Silme İptal Edildi")

    def kanal_yeri_degistirme(self):
        print("Mevcut kanalınızı hangi kanal ile değiştirmek istiyorsunuz ?")
        degisecekkanal = int(input("Sırasını Giriniz"))-1

        mevcut_kanal_sirasi = self.kanal_listesi.index(self.kanal)

        self.kanal_listesi[degisecekkanal] , self.kanal_listesi[mevcut_kanal_sirasi] = self.kanal_listesi[mevcut_kanal_sirasi] , self.kanal_listesi[degisecekkanal]

        print("Kanalınızın Yerleri Değiştirildi")
        print(self.kanal_listesi)

    def __len__(self):
        return len(self.kanal_listesi)

kumanda1 = Kumanda()


while True:
    memax = input("Yapmak istediğiniz işlemi seçiniz...")
    if memax == 'q':
        break
    if (memax == "1" or memax == "2"):
        kumanda1.tv_durum1()

    if (memax == "3"):
        kumanda1.ses_ayari1()
    if (memax == "4"):
        kanal_eklentileri = input("Kanal isimlerini ',' ile ayırarak girebilirsiniz...")
        kanal_listesi = kanal_eklentileri.split(",")
        for i in kanal_listesi:
            kumanda1.kanal_ekle(i)
            print(kumanda1.kanal_listesi)
    if (memax == "5"):
        kumanda1.kanal_silme()
    if (memax == "6"):
        kumanda1.kanal_yeri_degistirme()
    if memax == "7":
        print(kumanda1.__len__())
