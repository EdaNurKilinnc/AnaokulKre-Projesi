class Öğretmen:
    # Özellikler
    def __init__(self, isim, soyisim, telno, yas, sinifadi):
        self.isim = isim
        self.soyisim = soyisim
        self.telno = telno
        self.yas = yas
        self.sinifadi = sinifadi

    # Metotlar
    def get_info(self):
        return f"Öğretmen: {self.isim} {self.soyisim}, Tel: {self.telno}, Yaş: {self.yas}, Sınıf: {self.sinifadi}"

# Öğretmen örnekleri oluşturma
öğretmenler = [
    Öğretmen("Egemen", "Yalçın", "05454678986", 26, "Kelebek"),
    Öğretmen("Jale", "Kale", "05693425170", 34, "Aslan"),
    Öğretmen("Emir", "Yanıt", "05438752309", 31, "Sincap"),
    Öğretmen("Hilal", "Ekin", "05439215656", 28, "Balık"),
    Öğretmen("Mustafa", "Akın", "05497240232", 32, "Panda"),
    Öğretmen("Nuray", "Demir", "05234153867", 38, "Zürafa"),
    Öğretmen("Danla", "Kılçık", "05382831748", 25, "Ceylan")
]

# Kullanıcıdan öğretmen adını alma ve bilgileri gösterme
def ogretmen_bilgisi_bul(isim):
    for öğretmen in öğretmenler:
        if öğretmen.isim == isim:
            return öğretmen.get_info()
    return "Öğretmen bulunamadı."

# Kullanıcıdan isim alma
kullanici_girdisi = input("Bilgilerini öğrenmek istediğiniz öğretmenin adını girin: ")
print(ogretmen_bilgisi_bul(kullanici_girdisi))


# Yeni öğretmen ekleme fonksiyonu
def yeni_ogretmen_ekle(): 
    isim = input("Öğretmenin ismini girin: ") 
    soyisim = input("Öğretmenin soyismini girin: ") 
    telno = input("Öğretmenin telefon numarasını girin: ") 
    yas = int(input("Öğretmenin yaşını girin: ")) 
    sinifadi = input("Öğretmenin sınıf adını girin: ") 
    yeni_ogretmen = Öğretmen(isim, soyisim, telno, yas, sinifadi) 
    öğretmenler.append(yeni_ogretmen)
    print(f"{isim} {soyisim} başarıyla eklendi.") 



def yeni_ogretmen_ekle_sorgu():
    while True:
        cevap = input("Yeni bir öğretmen eklemek ister misiniz? (evet/hayır): ").lower() 
        if cevap == "evet": 
            yeni_ogretmen_ekle() 
        elif cevap == "hayır":
           print("Yeni öğretmen eklenmedi.") 
        else: 
            print("Geçersiz cevap. Lütfen 'evet' veya 'hayır' girin.")
            continue
        break
    

# Öğretmen bilgilerini sorgulama fonksiyonu 
def ogretmen_bilgisi_sorgu(): 
    isim = input("Bilgilerini öğrenmek istediğiniz öğretmenin adını girin: ") 
    print(ogretmen_bilgisi_bul(isim))
    
    
 # Öğretmen bilgilerini bulma fonksiyonu 
def ogretmen_bilgisi_bul(isim):
    for öğretmen in öğretmenler: 
        if öğretmen.isim == isim:
             return öğretmen.get_info() 
        return "Öğretmen bulunamadı." 
    

# Öğretmen silme fonksiyonu 
def ogretmen_sil(isim):
    for öğretmen in öğretmenler: 
        if öğretmen.isim == isim: 
            öğretmenler.remove(öğretmen) 
            return f"{isim} başarıyla silindi." 
        return "Öğretmen bulunamadı."
    
    
# Ana döngü 
while True: 
    yeni_ogretmen_ekle_sorgu() 
    ogretmen_bilgisi_sorgu() 
    devam = input("Başka bir işlem yapmak ister misiniz? (evet/hayır): ").lower() 
    if devam == "hayır":
        break 
    
    
# Tüm öğretmenlerin bilgilerini görüntüleme 
for öğretmen in öğretmenler: 
    print(öğretmen.get_info())