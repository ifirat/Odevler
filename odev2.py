mesafe = input("Mesafeyi KM cinsinden giriniz : ")

#girilecek mesafe bilgisinin tam sayi olmama ihtimali icin FLOAT olarak ayarladik
kara_mil = float(mesafe) / 1.609344     

print("SONUC :", kara_mil, "Kara Milidir.")
