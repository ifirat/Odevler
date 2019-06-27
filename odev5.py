print("""###### ATM ######

$$$$$$ EN GUVENILIR BANKA IPEK BANKA HOSGELDINIZ $$$$$$

""")

bakiye = 1000

while True:
    islem = input("""1- Bakiye Kontrolu
2- Para yatirma
3- Para Cekme

Yapmak Istediginiz Islem Numarasini Giriniz : """)

    ## BAKIYE SORGULAMA
    if int(islem) == 1:         

        print("\n <<<<<<  Bakiyeniz :", bakiye , "EURO   >>>>>>\n")

    ## BAKIYE SORGULAMA UST MENUYE GECIS
        gecis = int(input("""Ana Menuye donmek icin   ==> 4
Isleminizi Bitirmek icin ==> 5
tusuna basiniz...... : """))

        if gecis == 5: 
            break
            

    ## PARA YATIRMA    
    elif int(islem)==2:     

        para_yatirma = int(input("\n Yatirmak istediginiz miktari giriniz :"))

        bakiye = bakiye + para_yatirma

        print(" \n <<<<<<  Yeni Bakiyeniz :", bakiye , "EURO  >>>>>> \n")

    ## PARA YATIRMA UST MENUYE GECIS 
        gecis = int(input("""Ana Menuye donmek icin   ==> 4
Isleminizi Bitirmek icin ==> 5
tusuna basiniz...... : """))                            

        if gecis == 5:
            break
        
    ## PARA CEKME
    elif int(islem)==3:     

        para_cekme = int(input("\n Cekmek istediginiz miktari giriniz :"))

        bakiye_kontrol = bakiye - para_cekme

        if bakiye_kontrol < 0:
            print("\n <<<<<< Bakiyeniz yetersiz... >>>>>> ")

            print("\n <<<<<< Bakiyeniz :", bakiye , "EURO  >>>>>>\n")

        else:
            print("\n <<<<<< Yeni Bakiyeniz :", bakiye_kontrol , "EURO  >>>>>>\n")
            bakiye = bakiye_kontrol

    ## PARA CEKME UST MENUYE GECIS 
        gecis = int(input("""Ana Menuye donmek icin   ==> 4
Isleminizi Bitirmek icin ==> 5
tusuna basiniz...... : """))

        if gecis == 5:
            break
    
    

