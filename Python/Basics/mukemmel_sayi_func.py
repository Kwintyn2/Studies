def perfect(i):
    toplam = 0
    for j in range(1,i):
        if i % j == 0:
            toplam += j
    return toplam == i



for i in range(1,10000):
    if perfect(i):
        print("Mükemmel Sayı",i)
