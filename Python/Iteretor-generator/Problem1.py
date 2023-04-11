class kare_al():
    def __init__(self, max):
        self.max = max
        self.deger = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.max > self.deger:
            sonuc = self.deger ** 2
            self.deger += 1
            return sonuc

        else:
            self.deger = 0
            raise StopIteration


for i in kare_al(16):
    print(i)








