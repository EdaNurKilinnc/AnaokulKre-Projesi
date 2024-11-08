class Öğrenci:
    def __init__(self, adi, soyadi, yasi, sinifi, velitelno, öğretmeni):
        self.adi = adi
        self.soyadi = soyadi
        self.yasi = yasi
        self.sinifi = sinifi
        self.velitelno = velitelno
        self.öğretmeni = öğretmeni

    def get_info(self):
        return f"Öğrenci: {self.adi} {self.soyadi}, Yaş: {self.yasi}, Sınıf: {self.sinifi}, Veli Tel: {self.velitelno}, Öğretmen: {self.öğretmeni}"

Öğrenciler = [
    Öğrenci("Arda", "Beniz", 3, "Kelebek", "05245961875", "Egemen Yalçın"),
    Öğrenci("Ekrem", "Bilim", 3, "Kelebek", "05425631548", "Egemen Yalçın"),
    Öğrenci("Ceren", "Aksoy", 3, "Kelebek", "05472853695", "Egemen Yalçın"),
    Öğrenci("Ayşe", "Ensar", 4, "Aslan", "0574261549", "Jale Kale"),
    Öğrenci("Ayşegül", "Ümit", 4, "Aslan", "05418536941", "Jale Kale"),
    Öğrenci("Emirhan", "İlim", 4, "Aslan", "05782499657", "Jale Kale"),
    Öğrenci("Enes", "Yiğit", 4, "Aslan", "05371980382", "Jale Kale"),
    Öğrenci("Nilay", "Kök", 4, "Sincap", "0546280482", "Emir Yanıt"),
    Öğrenci("Suna", "Bayram", 4, "Sincap", "05374828123", "Emir Yanıt"),
    Öğrenci("Halil", "Ker", 4, "Sincap", "05468279475", "Emir Yanıt"),
    Öğrenci("Can", "Dinç", 5, "Balık", "0546286474", "Hilal Ekin"),
    Öğrenci("Kerem", "Kısım", 5, "Balık", "0534858933", "Hilal Ekin"),
    Öğrenci("Emin", "Tunç", 5, "Balık", "05472475824", "Hilal Ekin"),
    Öğrenci("Emine", "Tunç", 5, "Balık", "05364789254", "Hilal Ekin"),
    Öğrenci("Nil", "Umut", 5, "Panda", "053894320345", "Mustafa Akın"),
    Öğrenci("Emre", "Alptek", 5, "Panda", "05345665432", "Mustafa Akın"),
    Öğrenci("İpek", "Esin", 5, "Panda", "05422309873", "Mustafa Akın"),
    Öğrenci("Yunus", "Zen", 6, "Zürafa", "05436284647", "Nuray Demir"),
    Öğrenci("Erva", "Zen", 6, "Zürafa", "05345627367", "Nuray Demir"),
    Öğrenci("Eda", "Akın", 6, "Zürafa", "0546374583", "Nuray Demir"),
    Öğrenci("Ahmet", "Aysü", 6, "Zürafa", "05345634873", "Nuray Demir"),
    Öğrenci("Naz", "Keman", 6, "Zürafa", "05463744842", "Danla Kılçık"),
    Öğrenci("Zeynep", "Anka", 6, "Ceylan", "05364738823", "Danla Kılçık"),
    Öğrenci("Naz", "Parla", 6, "Ceylan", "053452678338", "Danla Kılçık"),
    Öğrenci("Merve", "İclal", 6, "Ceylan", "05345672446", "Danla Kılçık")
]

# Kullanıcıdan öğrenci adını alma ve bilgileri gösterme
def ogrenci_bilgisi_bul(adi):
    for öğrenci in Öğrenciler:
        if öğrenci.adi == adi:
            return öğrenci.get_info()
    return "Öğrenci bulunamadı."

# Öğrenci bilgilerini sorgulama
kullanici_girdisi = input("Bilgilerini öğrenmek istediğiniz öğrencinin adını girin: ")
print(ogrenci_bilgisi_bul(kullanici_girdisi))




# Yeni öğrenci ekleme fonksiyonu
def yeni_ogrenci_ekle():
    isim = input("Öğrencinin ismini girin: ") 
    soyisim = input("Öğrencinin soyismini girin: ") 
    telno = input("Velinin telefon numarasını girin: ") 
    yas = int(input("Öğrencinin yaşını girin: ")) 
    sinifadi = input("Öğrencinin sınıf adını girin: ") 
    öğretmeni = input("Öğretmeninin ismini giriniz ")
    yeni_ogrenci = Öğrenci(isim, soyisim, telno, yas, sinifadi,öğretmeni) 
    Öğrenciler.append(yeni_ogrenci)
    print(f"{isim} {soyisim} başarıyla eklendi.") 




def yeni_ogrenci_ekle_sorgu():
    while True:
        cevap = input("Yeni bir öğrenci eklemek ister misiniz? (evet/hayır): ").lower() 
        if cevap == "evet": 
            yeni_ogrenci_ekle() 
        elif cevap == "hayır":
           print("Yeni öğrenci eklenmedi.") 
        else: 
            print("Geçersiz cevap. Lütfen 'evet' veya 'hayır' girin.")
            continue
        break



# Öğrenci bilgilerini sorgulama fonksiyonu
def ogrenci_bilgisi_sorgu():
     adi = input("Bilgilerini öğrenmek istediğiniz öğrencinin adını girin: ") 
     print(ogrenci_bilgisi_bul(adi)) 
     
     

# Öğrenci bilgilerini bulma fonksiyonu 
def ogrenci_bilgisi_bul(adi): 
    for öğrenci in Öğrenciler: 
        if öğrenci.adi == adi: 
            return öğrenci.get_info()
        return "Öğrenci bulunamadı."
    


# Öğrenci silme fonksiyonu 
def ogrenci_sil(isim):
    for öğrenci in öğrenciler: 
        if öğrenci.isim == isim: 
            Öğrenciler.remove(öğrenci) 
            return f"{isim} başarıyla silindi." 
        return "Öğrenci bulunamadı."
    


# Ana döngü 
while True: 
    yeni_ogrenci_ekle_sorgu() 
    ogrenci_bilgisi_sorgu() 
    devam = input("Başka bir işlem yapmak ister misiniz? (evet/hayır): ").lower() 
    if devam == "hayır":
        break 
    

# Tüm öğretmenlerin bilgilerini görüntüleme 
for öğrenci in Öğrenciler: 
    print(öğrenci.get_info())