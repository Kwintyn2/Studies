print("**LOGIN**")

s_username = "kedi"
s_pass = "kedi123"

for try_count in range(6):
    if try_count == 5:
        print("Deneme Hakkınız Kalmadı.\nProgram Sonlandırılıyor.....")
        break

    u_username = input("Kullanıcı Adınızı Giriniz: ")
    u_pass = input("Şifrenizi Giriniz: ")

    if u_username != s_username and u_pass != s_pass:
        try_count += 1
        print("Kullanıcı adı ve şifreniz Yanlış.. \nKalan Deneme Hakkınız: {}".format(5-try_count))
        continue
    if u_username == s_username and u_pass != s_pass:
        try_count += 1
        print("Şifreniz Yanlış.. \nKalan Deneme Hakkınız: {}".format(5-try_count))
        continue
    if u_username != s_username and u_pass == s_pass:
        try_count += 1
        print("Kullanıcı adı Yanlış.. \nKalan Deneme Hakkınız: {}".format(5-try_count))
        continue
    if u_username == s_username and u_pass == s_pass:
        print('***********************',
              "BAŞARI İLE GİRİŞ YAPILDI",
              "***********************",
              "WELCOME TO OUR JUNGLE",
              "***********************",
              sep = "\n")
        break