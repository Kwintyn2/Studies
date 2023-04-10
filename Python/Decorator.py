def mukemmel_sayi(func):
    def wrapper(*args):
        for x in args:
            total = 0
            for y in range(1, x):
                if x % y == 0:
                    total += y
            if total == x:
                print(x, "Mükemmel sayi")
        func(*args)
    return wrapper


@mukemmel_sayi
def asal_sayi(*args):
    for x in args:
        sayi = 2

        if x == 1:
            print(x, "asal degil")
            continue
        elif x == 2:
            print(x, "asal")
            continue
        else:
            while sayi < x:
                if x % sayi == 0:
                    print(x, "Asal değil")
                    break
                sayi += 1
            if sayi == x:
               print(x, "Asal")


asal_sayi(*range(1, 10001))








