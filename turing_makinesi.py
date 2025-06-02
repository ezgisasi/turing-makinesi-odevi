class TuringMakinesi:
    def __init__(self, bant_verisi):
        self.bant = list(bant_verisi)  # Bantı karakter listesine çevirdim
        self.kafa = 1  # İlk karakterden sonra okumaya başlasın
        self.durum = "q0"  # Başlangıç durumu

    def bant_yazdir(self):
        bant_str = "".join(self.bant)  # Listeyi stringe çevirdim
        isaretci = " " * self.kafa + "^"  # Okuma kafasının yerini gösteren işaretçi
        print(bant_str)
        print(isaretci)
        print("Durum:", self.durum)
        print()

    def hareket_et(self, yon):
        if yon == "R":  # Sağa git
            self.kafa += 1
            if self.kafa >= len(self.bant):  # Sona geldiyse boş hücre ekle
                self.bant.append("_")
        elif yon == "L":  # Sola git
            self.kafa -= 1
            if self.kafa < 0:  # Başın altına düşerse öne boş hücre koy
                self.bant.insert(0, "_")
                self.kafa = 0

    def dogrula(self):
        self.durum = "q1"  # Bir sonraki durum
        self.bant_yazdir()

        # Sistem PIN’inin başladığı yeri bul
        try:
            self.sistem_baslangic = self.bant.index("#", self.kafa) + 1
        except ValueError:
            self.durum = "qH"  # Eğer # yoksa hata
            return False

        while self.bant[self.kafa] != "#": # Kullanıcı PIN’ini kontrol etmeye başla
            self.bant_yazdir()

            # Eğer sistem PIN biterse ya da hata varsa dur
            if self.sistem_baslangic >= len(self.bant) or self.bant[self.kafa] == "#":
                self.durum = "qH"
                return False

            if self.bant[self.kafa] == self.bant[self.sistem_baslangic]:
                self.bant[self.kafa] = "X"  # Kullanıcı PIN’indeki karakter işaretlendi
                self.bant[self.sistem_baslangic] = "Y"  # Sistem PIN’indeki karakter de işaretlendi

                self.durum = f"q{int(self.durum[1:]) + 1}"  # Durumu sırayla güncelledim
                self.hareket_et("R")  # Kullanıcı PIN’inde bir sağa geç
                self.sistem_baslangic += 1  # Sistem PIN’inde de bir ileri git
            else:
                self.durum = "qH"  # Karakterler eşleşmediyse dur
                self.bant_yazdir()
                return False

        if self.sistem_baslangic < len(self.bant) and self.bant[self.sistem_baslangic] == "#":
            self.durum = "kabul"  # Başarılı eşleşme
            self.bant_yazdir()
            return True
        else:
            self.durum = "qH"  # Eşleşme tam değilse hata
            self.bant_yazdir()
            return False
