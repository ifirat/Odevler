
while True:
    try:
           
        giris=int(input("""1-) Hesap Olusturma
2-) Cikis

Islem numarasini giriniz :"""))
        if giris==1:
            tekrar=0
        elif giris==2:
            break
        else:
            print("\nHatali rakam girdiniz tekrar deneyiniz...")
            continue
            

        tekrar=0
        while tekrar==0:                        #kullanici adi icin dongu baslangici

            username = input("Kullanıcı Adı :")
                     
            if not username :        
                print("Kullanici adi bos birakilamaz...")
                continue
            else: 
                with open("kullanici bilgileri.txt","a+") as kullanici: 
                    kullanici.seek(0)           ##imleci dosyanin basina aliyoruz
                    veri=kullanici.readlines()  ##dosyayi liste olarak okutuyoruz
                    sayac=0
                    
                    for i in veri:              ##tek numarali satirlarda kullanici adi, cift numarali satirlarda parola kayitli
                        sayac+=1                
                        if sayac % 2 != 0:      ## mod islemi ile tek numarali satirlara islem yacak dongu baslangici            
                            
                            if username+"\n" == i:
                                print("Bu kullanici adi kullanilmaktadir. Lutfen tekrar deneyiniz..")
                                break
                    if sayac==len(veri):        ##tum liste kontrol edildikten sonra donguden cikmak icin kosul
                        tekrar=1
                    

        while True:                             ##parola icin dongu baslangici
            password = input("Parola        :")
            
            if not password:
                print(" Parola bolumu bos birakilamaz...")
                continue
            break

        print("\nKullanici Adi : ", username)
        print("Parola        : ", password)
        print("HESABINIZ OLUSTURULDU....\n")
        with open("kullanici bilgileri.txt","a") as kullanici:
            kullanici.write(username + "\n")
            kullanici.write(password + "\n")

    except ValueError:
        print("\nLutfen dogru rakam giriniz....")
