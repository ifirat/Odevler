
anahtar=1
while anahtar==1:
    user_name = input("3 ile 18 Karakter Arasinda Kullanıcı Adı Giriniz :")
    if 3 <= len(user_name) <= 18:
        if "0" in user_name :
            print("kullanici adi icerisinde rakam kullanilamaz...\n")
        elif "1" in user_name :
            print("kullanici adi icerisinde rakam kullanilamaz...\n")
        elif "2" in user_name :
            print("kullanici adi icerisinde rakam kullanilamaz...\n")
        elif "3" in user_name :
            print("kullanici adi icerisinde rakam kullanilamaz...\n")
        elif "4" in user_name :
            print("kullanici adi icerisinde rakam kullanilamaz...\n")
        elif "5" in user_name :
            print("kullanici adi icerisinde rakam kullanilamaz...\n")
        elif "6" in user_name :
            print("kullanici adi icerisinde rakam kullanilamaz...\n")
        elif "7" in user_name :
            print("kullanici adi icerisinde rakam kullanilamaz...\n")
        elif "8" in user_name :
            print("kullanici adi icerisinde rakam kullanilamaz...\n")
        elif "9" in user_name :
            print("kullanici adi icerisinde rakam kullanilamaz...\n")
        else:
            while anahtar==1:
                parola = input("6 ile 12 Karakter arasinda Parola Giriniz :")
                if 6 <= len(parola) <= 12:
                    print("Kullanici adiniz :", user_name)
                    print("Parolaniz        :", parola)
                    dosya = open ('KullaniciBilgileri.txt', 'w')
                    print("Kullanici adiniz :", user_name, file=dosya)
                    print("Parolaniz        :", parola, file=dosya)
                    dosya.close()
                    anahtar=2
                    
                else:
                    print("Lutfen 6 ile 12 karakter arasinda parola giriniz ..... \n")
    else:
        print("Lutfen 3 ve 18 karakter arasinda bir kullanici adi olusturunuz...\n")

##if "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in user_name:
##    print("0,1,2,3 rakami kullanici adi icerisinda kullanilmistir...")
##else:
##    print("0 rakami kullanici adi icerisinda kullanilmamistir...")
##or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9"
