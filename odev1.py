print("""
#################################################
####   LÜTFEN BİLGİLERİ KÜÇÜK HARF           ####
####               VE                        ####
####   TÜRKÇE KARAKTER KULLANARAK GİRİNİZ....####
#################################################
""")

d_gun=input("Dogum Gununuzu Giriniz : ")
d_ay=input("Dogdugunuz Ayi Giriniz : ")

print(d_gun, d_ay)


if not d_gun or not d_ay:
    print("Dogum gununuzu ve dogum ayinizi yazmadan gecemezsiniz!!!!!")

##Koç Burcu (21 Mart- 20 Nisan)
elif 21 <= int(d_gun) <= 31 and d_ay == "mart" or 1 <= int(d_gun) <= 20 and d_ay == "nisan":
    print("KOÇ BURCUNDANSINIZ")

##Boğa Burcu (21 Nisan- 21 Mayıs)    
elif 21 <= int(d_gun) <=30 and d_ay == "nisan" or 1 <= int(d_gun) <=21 and d_ay == "mayıs":
    print("BOĞA BURCUNDANSINIZ")

##İkizler Burcu (22 Mayıs- 22 Haziran)
elif 22 <= int(d_gun) <=31 and d_ay == "mayıs" or 1<= int(d_gun) <=22 and d_ay == "haziran":
    print("İKİZLER BURCUNDANSINIZ")

##Yengeç Burcu (23 Haziran- 22 Temmuz)
elif 23 <= int(d_gun) <=30 and d_ay == "haziran" or 1<= int(d_gun) <=22 and d_ay == "temmuz":
    print("YENGEÇ BURCUNDANSINIZ")
    
##Aslan Burcu (23 Temmuz- 22 Ağustos)
elif 23 <= int(d_gun) <=31 and d_ay == "temmuz" or 1<= int(d_gun) <=22 and d_ay == "ağustos":
    print("ASLAN BURCUNDANSINIZ")

##Başak Burcu (23 Ağustos- 22 Eylül)
elif 23 <= int(d_gun) <=31 and d_ay == "ağustos" or 1<= int(d_gun) <=22 and d_ay == "eylül":
    print("BAŞAK BURCUNDANSINIZ")

##Terazi Burcu (23 Eylül- 22 Ekim)
elif 23 <= int(d_gun) <=30 and d_ay == "eylül" or 1<= int(d_gun) <=22 and d_ay == "ekim":
    print("TERAZİ BURCUNDANSINIZ")

##Akrep Burcu (23 Ekim- 21 Kasım)
elif 23 <= int(d_gun) <=31 and d_ay == "ekim" or 1<= int(d_gun) <=21 and d_ay == "kasım":
    print("AKREP BURCUNDANSINIZ")

##Yay Burcu (22 Kasım- 21 Aralık)
elif 23 <= int(d_gun) <=30 and d_ay == "kasım" or 1<= int(d_gun) <=21 and d_ay == "aralık":
    print("YAY BURCUNDANSINIZ")

##Oğlak Burcu (22 Aralık- 21 Ocak)
elif 22 <= int(d_gun) <=31 and d_ay == "aralık" or 1<= int(d_gun) <=21 and d_ay == "ocak":
    print("OĞLAK BURCUNDANSINIZ")

##Kova Burcu (22 Ocak- 19 Şubat)
elif 22 <= int(d_gun) <=31 and d_ay == "ocak" or 1<= int(d_gun) <=19 and d_ay == "şubat":
    print("KOVA BURCUNDANSINIZ")

##Balık Burcu (20 Şubat- 20 Mart)
elif 20 <= int(d_gun) <=29 and d_ay == "şubat" or 1<= int(d_gun) <=20 and d_ay == "mart":
    print("BALIK BURCUNDANSINIZ")

else:
    print("Lutfen bilgileri dogru giriniz!!!!")
