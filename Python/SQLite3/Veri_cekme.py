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

def veri_al():
    imlec.execute("Select * From kitaplik")
    liste = imlec.fetchall()

    for i in liste:
        print(i)


def veri_al2():
    imlec.execute("Select isim,yazar from kitaplik")
    liste = imlec.fetchall()
    for i in liste:
        print(i)


def veri_al3(yayinevi):
    imlec.execute("Select * from kitaplik where Yayınevi = ?", (yayinevi,))
    liste = imlec.fetchall()
    for i in liste:
        print(i)


veri_al3("Everest")
sq_baglanti.close()
