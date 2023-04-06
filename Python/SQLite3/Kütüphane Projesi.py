from Kütüphane_Projesi_moduller import *

print("""**********************

Kütüphane Programına Hoşgeldiniz

işlemler;
1. Kitapları Göster
2. Kitap Sorgulama
3. Kitap Ekle
4. Kitap Sil
5. Baskı Yükselt

Çıkmak İçin 'Q' tuşuna basınız..
**********************""")

kütüphane = Kütüphane()


while True:
    işlem = input("Yapacağınız işlemi seçiniz: ")

    if (işlem == "q"):
        print("Program Sonlandırılıyor...")
        time.sleep(2)
        print("Program Sonlandı :P")
        break
    elif (işlem == "1"):
        kütüphane.kitaplari_goster()
    elif (işlem == "2"):
        isim = input("Hangi Kitabı İstiyorsunuz")
        print("Kitap Sorgulanıyor .... ")
        time.sleep(2)

        kütüphane.kitap_sorgula(isim)

    elif (işlem == "3"):
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayinevi = input("Yayınevi: ")
        tur = input("Tür: ")
        baski = int(input("Baski: "))

        yeni_kitap = Kitap(isim, yazar, yayinevi, tur, baski)

        print("Kitap ekleniyor...")
        kütüphane.kitap_ekle(yeni_kitap)
        time.sleep(1)
        print("Kitap Eklendi :D")

    elif (işlem == "4"):
        isim = input("Hangi Kitabi Silmek İstiyorsunuz ?")
        cevap = input ("Emin misiniz ? (E/H)")
        if cevap == "E":
            print("Kitap Siliniyor...")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap Silindi...")

    elif işlem == "5":
        isim = input("Hangi kitabin baskisini yükseltmek istiyorsunuz ? ")
        print("Baskı yükseltiliyor...")
        time.sleep(2)

        kütüphane.baski_yukselt(isim)

        print("Baskı Yükseltildi...")
    else:
        print("Geçersiz Girdi :@")







