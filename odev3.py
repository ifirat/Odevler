ad_soyad   = input ("Ad ve Soyadınızı giriniz           : ")
vize_notu  = input ("Vize notunuzu giriniz              : ")
final_notu = input ("Final notunuzu giriniz             : ")
ders_sayisi= input ("Katıldığınız ders sayısını giriniz : ")

##- Vize Notu ( 30%)
##- Final Notu (50%)
##- Ders takip (20%)

vize_yuzde  = int(vize_notu) * 0.3
final_yuzde = int(final_notu) * 0.5
ders_yuzde  = (100-((20 - int(ders_sayisi)) * 5))*0.2

## yil sonu puani hesabi
ders_notu = vize_yuzde + final_yuzde + ders_yuzde


print('"' +  ad_soyad + '"', ' yıl sonu ders punanınız : ' , ders_notu)

dosya = open ("ogrenciNotHesaplama.txt", "w")
print ("isim Soyisim           : " , ad_soyad, "\n",
       "Vize Notu              : " , vize_notu, "\n",
       "Final Notu             : " , final_notu, "\n",
      "Girilen Ders Sayisi    : " , ders_sayisi, "\n",
       "\n",
       "-"*50, "\n",
      "Yil Sonu Ders Puaniniz : ", ders_notu, file=dosya, sep="")

dosya.close()
