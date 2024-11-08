class Ders:
    def __init__(self, saat, konu):
        self.saat = saat
        self.konu = konu

    def get_info(self):
        return f"Saat: {self.saat}, Konu: {self.konu}"

class DersProgrami:
    def __init__(self, yas_grubu):
        self.yas_grubu = yas_grubu
        self.dersler = []

    def ders_ekle(self, saat, konu):
        yeni_ders = Ders(saat, konu)
        self.dersler.append(yeni_ders)

    def programi_goster(self):
        print(f"{self.yas_grubu} yaş grubu ders programı:")
        for ders in self.dersler:
            print(ders.get_info())

# 3 yaş grubu ders programı oluşturma
program_3_yas = DersProgrami("3")
program_3_yas.ders_ekle("08:00 - 09:00", "İngilizce")
program_3_yas.ders_ekle("09:00 - 10:00", "Boyama")
program_3_yas.ders_ekle("10:00 - 11:00", "Müzik")
program_3_yas.ders_ekle("11:00 - 11:30", "Jimlastik")
program_3_yas.ders_ekle("11:30 - 12:00", "Öğle Yemeği")


# 4 yaş grubu ders programı oluşturma
program_4_yas = DersProgrami("4")
program_4_yas.ders_ekle("09:00 - 10:00", "İngilizce")
program_4_yas.ders_ekle("10:00 - 11:00", "Boyama")
program_4_yas.ders_ekle("11:00 - 12:00", "Jimlastik")
program_4_yas.ders_ekle("12:00 - 13:00", "El Becerileri")
program_4_yas.ders_ekle("13.00 - 13:30", "Müzik")
program_4_yas.ders_ekle("13:30 - 13:30", "Öğle Yemeği")


# 5 yaş grubu ders programı oluşturma
program_5_yas = DersProgrami("5")
program_5_yas.ders_ekle("09:00 - 10:00", "İngilizce")
program_5_yas.ders_ekle("10:00 - 11:00", "Boyama")
program_5_yas.ders_ekle("11:00 - 12:00", "Jimlastik")
program_5_yas.ders_ekle("12:00 - 13:00", "El Becerileri")
program_5_yas.ders_ekle("13.00 - 13:30", "Müzik")
program_5_yas.ders_ekle("13:30 - 13:30", "Öğle Yemeği")

# 6 yaş grubu ders programı oluşturma
program_6_yas = DersProgrami("6")
program_6_yas.ders_ekle("09:00 - 10:00", "Dil Dersleri")
program_6_yas.ders_ekle("10:00 - 11:00", "El Becerileri")
program_6_yas.ders_ekle("11:00 - 12:00", "Müzik")
program_6_yas.ders_ekle("12:00 - 12:30", "Öğle Yemeği")
program_6_yas.ders_ekle("12.30 - 13:00", "Yazma Becerileri")
program_6_yas.ders_ekle("13:00 - 14:00", "Jimlastik")
program_6_yas.ders_ekle("14:00 - 15:00", "Boyama")



# Kullanıcıdan yaş grubunu alma ve ders programını gösterme 
def yas_grubu_sorgu(): 
    yas_grubu = input("Hangi yaş grubunun ders programını görmek istiyorsunuz? (3, 4, 5, 6): ") 
    if yas_grubu == "3": 
        program_3_yas.programi_goster() 
    elif yas_grubu == "4":
         program_4_yas.programi_goster() 
    elif yas_grubu == "5":
         program_5_yas.programi_goster()
    elif yas_grubu == "6":
         program_6_yas.programi_goster() 
    else: print("Geçersiz yaş grubu. Lütfen 3, 4, 5 veya 6 girin.") 
    
    
# Yaş grubu sorgusu
yas_grubu_sorgu()


# Ders ekleme ve çıkarma işlemleri
while True: 
    islem = input("Ders eklemek veya çıkarmak ister misiniz? (ekle/çıkar/hayır): ").lower()
    if islem == "ekle":
         yas_grubu = input("Hangi yaş grubuna ders eklemek istiyorsunuz? (3, 4, 5, 6): ")
         saat = input("Dersin saatini girin (HH:MM - HH:MM formatında): ") 
         konu = input("Dersin konusunu girin: ") 
         if yas_grubu == "3":
             program_3_yas.ders_ekle(saat, konu) 
         elif yas_grubu == "4":
             program_4_yas.ders_ekle(saat, konu) 
         elif yas_grubu == "5": 
            program_5_yas.ders_ekle(saat, konu)
         elif yas_grubu == "6":
             program_6_yas.ders_ekle(saat, konu) 
         else:
             print("Geçersiz yaş grubu.") 
    elif islem == "çıkar":
         yas_grubu = input("Hangi yaş grubundan ders çıkarmak istiyorsunuz? (3, 4, 5, 6): ") 
         saat = input("Çıkarmak istediğiniz dersin saatini girin (HH:MM - HH:MM formatında): ") 
         if yas_grubu == "3": 
            program_3_yas.ders_cikar(saat)
         elif yas_grubu == "4": 
            program_4_yas.ders_cikar(saat)
         elif yas_grubu == "5": 
            program_5_yas.ders_cikar(saat) 
         elif yas_grubu == "6": 
            program_6_yas.ders_cikar(saat) 
         else: 
             print("Geçersiz yaş grubu.") 

    elif islem == "hayır": 
        break 
    else: print("Geçersiz işlem. Lütfen 'ekle', 'çıkar' veya 'hayır' girin.") 
    
    
    
# Tüm ders programlarını gösterme
print("\nGüncellenmiş ders programları:") 
program_3_yas.programi_goster() 
print() 
program_4_yas.programi_goster() 
print() 
program_5_yas.programi_goster() 
print() 
program_6_yas.programi_goster()