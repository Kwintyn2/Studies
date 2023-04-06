# Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun.
# Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.
#
#                     coskun.m.murat@gmail.com
#                     example@xyz.com
#                     mustafa.com
#                     mustafa@gmail
#                     kerim@yahoo.com
#
#                            //
#                            //
#                            //
#
#
# *İpucu: Stringlerde bulunan endswith ve find metodlarını kullanabilirsiniz.*

def mail_mi(girdi):
    et_yer = girdi.find("@")
    et_sayi = girdi.count("@")
    nokta_yer = girdi.rfind(".")
    if et_yer != -1 and et_sayi != 0 and nokta_yer != -1 and et_yer < nokta_yer:
        return True
    else:
        return False


with open("mailler.txt", "r", encoding="utf-8") as file:
    mailler = file.readlines()
    with open ("mail_sonuclari.txt", "w", encoding="utf-8") as file2:
        for mail in mailler:
            if mail_mi(mail):
                file2.write(mail.strip() + "--- Mail Doğru\n")

            else:
                file2.write(mail.strip() + "--- Mail HATALI\n")







