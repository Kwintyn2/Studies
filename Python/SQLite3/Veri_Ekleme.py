import sqlite3

sq_baglanti = sqlite3.connect("Kütüphane.db")

imlec = sq_baglanti.cursor()

def tablo_olustur():
    imlec.execute("CREATE TABLE IF NOT EXISTS kitaplik (isim TEXT, yazar TEXT, Yayınevi TEXT, Sayfa_sayısı INT)")
    sq_baglanti.commit()
tablo_olustur()

def veri_ekle():
    imlec.execute("Insert into kitaplik Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    sq_baglanti.commit()
# veri_ekle()

def veri_ekle2(isim,yazar,yayinevi,sayfa):
    imlec.execute(f"Insert into kitaplik Values('{isim}','{yazar}','{yayinevi}',{sayfa})")
    sq_baglanti.commit()

isim = input("Kitap İsmini Giriniz: ")
yazar = input("Yazar İsmini Giriniz: ")
yayinevi = input("Yayınevi İsmini Giriniz: ")
sayfa = int(input("Sayfa Sayısını Giriniz: "))

if input("Girdiğiniz bilgileri eklemek istiyor musunuz ?\n(y \ n) ") == "y":
    veri_ekle2(isim, yazar, yayinevi, sayfa)
    print("Bilgiler Eklendi")
else:
    print("Ekleme Yapılmadı")

sq_baglanti.close()
