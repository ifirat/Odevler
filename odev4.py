print ("### SAYI TAHMIN OYUNU ###")

deger = 10  # Bulunmasi gereken sayi degeri

deneme_sayisi = 1

while deneme_sayisi <= 5 :
    tahmin = input ("1 ile 10 arasinda bir sayi giriniz :") #kullanicinin tahmini aliniyor
        
    if not tahmin:                                          #bos gecildigi zaman deneme yapilmis sayilmiyor, sonsuz bos gecme hakki var 
        print("Lutfen bos gecmeyiniz....\n")
    elif int(tahmin) == deger and deneme_sayisi==1:
        print("Tebrikler '* * *' kazandiniz.....")
        break
    elif int(tahmin) == deger and 2<=deneme_sayisi<=3:
        print("Tebrikler '* *' kazandiniz.....")
        break
    elif int(tahmin) == deger and 4<=deneme_sayisi<=5:
        print("Tebrikler '*' kazandiniz.....")
        break
    elif deneme_sayisi == 5:                                #5. denemede oyun sona eriyor
        print ("Uzgunuz Oyun Sona Ermistir......")
        break
    else:
        print("Sansinizi Tekrar Deneyin.......\n")
        deneme_sayisi +=1

