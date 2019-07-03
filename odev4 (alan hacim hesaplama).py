altmenu_cikis=0
while altmenu_cikis==0:
    try:
    
        menu = int(input("""1- Üçgen Alan Hesaplama
2- Kare Alan Hesaplama
3- Dikdörtgen Alan Hesaplama
4- Küp Hacim Hesaplama
5- Koni Hacim Hesaplama
6- Küre Hacim Hesaplama
7- Çıkış

Lutfen hesaplama yapmak istediginiz seklin numarasini giriniz  :"""))

        if menu==7:
            break

        elif menu==1:
            while True:
                try:
                    ucgen_menu = int(input("""\n1- Üçgen Kenar Uzunlukları İle Alan Hesaplama
2- Üçgen Yüksekliği İle Alan Hesaplama
3- Geri
4- Çıkış

Lütfen Menu Numarasını Giriniz : """))
                    if ucgen_menu==1:
                        kenar_1 = False
                        kenar_2 = False
                        kenar_3 = False
                        while True:
                            try:
                                if kenar_1==False:
                                    kenar_1 = int(input("\nBirinci Kenar Uzunluğu :"))
                                else:
                                    pass
                                if kenar_2==False:
                                    kenar_2 = int(input("\nİkinci Kenar Uzunluğu :"))
                                else:
                                    pass
                                if kenar_3==False:
                                    kenar_3 = int(input("\nÜçüncü Kenar Uzunluğu :"))
                                else:
                                    break
                            except ValueError:
                                print("Lutfen sadece rakam giriniz.....")
                        u_cevre = (kenar_1+kenar_2+kenar_3)/2
                        u_alan = (u_cevre*(u_cevre-kenar_1)*(u_cevre-kenar_2)*(u_cevre-kenar_3))**0.5
                        print("\nÜçgenin Alanı :", u_alan, " cm2\n")

                    elif ucgen_menu==2:
                        yukseklik = False
                        taban = False
                        while True:
                            try:
                                if yukseklik==False:
                                    yukseklik = int(input("Yükseklik :"))
                                else:
                                    pass
                                if taban==False:
                                    taban = int(input("Taban Uzunluğu :"))
                                else:
                                    break
                            except ValueError:
                                print("Lutfen sadece rakam giriniz.....")
                        
                        u_alan = (yukseklik*taban)/2
                        print("Üçgenin Alanı :", u_alan, " cm2")

                    elif ucgen_menu==3:
                        break

                    elif ucgen_menu==4:
                        altmenu_cikis=1
                        break

                    else:
                        print("\n#### Lütfen Geçerli Bir Menu Rakamı Giriniz... ####\n")    

                except ValueError:
                    print("\n#### Lutfen sadece rakam giriniz..... ####")


        elif menu==2:
            kare_menu=False
            while True:
                try:
                    
                    if kare_menu==False:
                        kare_kenar=int(input("\nKenar Uzunlugu giriniz :"))
                        kare_menu=True
                    if kare_menu==True:
                        kare_alan = kare_kenar**2
                        print("\nKare Alanı :", kare_alan, " cm2\n")
                        kare_menu = int(input("""1- Tekrar İşlem Yapma
2- Ana Menü
3- Çıkış

Lütfen yapmak istediğiniz işlem numarasını giriniz :"""))
                    if kare_menu==1:
                        kare_menu=False
                        continue
                        
                    elif kare_menu==2:
                        break
                    elif kare_menu==3:
                        altmenu_cikis=1
                        break
                    else:
                        print("\n#### Lütfen Geçerli Bir Menu Rakamı Giriniz... ####\n")
                except ValueError:
                    print("\n#### Lütfen Bir Rakam Giriniz... ####\n")               
            
##        else:
##            print("\n#### Lütfen Geçerli Bir Menu Rakamı Giriniz... ####\n")              
##        
##    except ValueError:
##        print("\n#### Lütfen Bir Rakam Giriniz... ####\n")       
##                                     
        elif menu==3:
            dortgen_menu=False
            kenar_1=False
            kenar_2=False
            while True:
                try:
                    
                    if dortgen_menu==False and kenar_1==False:
                        kenar_1=int(input("\nBirinci Kenar Uzunluğunu giriniz :"))
                        
                    if dortgen_menu==False and kenar_2==False:
                        kenar_2=int(input("\nİkinci Kenar Uzunluğunu giriniz :"))
                        dortgen_menu=True
                        
                    dortgen_alan = kenar_1*kenar_2
                    print("\nDikdörtgenin Alanı :", dortgen_alan, " cm2\n")
                       
                    dortgen_menu = int(input("""1- Tekrar İşlem Yapma
2- Ana Menü
3- Çıkış

Lütfen yapmak istediğiniz işlem numarasını giriniz :"""))
                    if dortgen_menu==1:
                        dortgen_menu=False
                        kenar_1=False
                        kenar_2=False
                        continue
                        
                    elif dortgen_menu==2:
                        break
                    elif dortgen_menu==3:
                        altmenu_cikis=1
                        break
                    else:
                        print("\n#### Lütfen Geçerli Bir Menu Rakamı Giriniz... ####\n")
                except ValueError:
                    print("\n#### Lütfen Bir Rakam Giriniz... ####\n")               


        elif menu==4:
            kup_menu=False
            while True:
                try:
                    
                    if kup_menu==False:
                        kup_kenar=int(input("\nKüp Kenar Uzunluğunu giriniz :"))
                        kup_menu=True
                    if kup_menu==True:
                        kup_hacim = kup_kenar**3
                        print("\nKüp Hacim :", kup_hacim, " cm3\n")
                        kup_menu = int(input("""1- Tekrar İşlem Yapma
2- Ana Menü
3- Çıkış

Lütfen yapmak istediğiniz işlem numarasını giriniz :"""))
                    if kup_menu==1:
                        kup_menu=False
                        continue
                        
                    elif kup_menu==2:
                        break
                    elif kup_menu==3:
                        altmenu_cikis=1
                        break
                    else:
                        print("\n#### Lütfen Geçerli Bir Menu Rakamı Giriniz... ####\n")
                except ValueError:
                    print("\n#### Lütfen Bir Rakam Giriniz... ####\n")


        elif menu==5:
            koni_menu=False
            yaricap=False
            yukseklik=False
            while True:
                try:
                    
                    if koni_menu==False and yaricap==False:
                        yaricap=int(input("\nYarıçap Uzunluğunu Giriniz :"))
                        
                    if koni_menu==False and yukseklik==False:
                        yukseklik=int(input("\nYüksekliği Giriniz :"))
                        koni_menu=True
                        
                    koni_hacim = 3.14*(yaricap**2)*yukseklik
                    print("\nKoninin Hacmi :", koni_hacim, " cm3\n")
                       
                    koni_menu = int(input("""1- Tekrar İşlem Yapma
2- Ana Menü
3- Çıkış

Lütfen yapmak istediğiniz işlem numarasını giriniz :"""))
                    if koni_menu==1:
                        koni_menu=False
                        yaricap=False
                        yukseklik=False
                        continue
                        
                    elif koni_menu==2:
                        break
                    elif koni_menu==3:
                        altmenu_cikis=1
                        break
                    else:
                        print("\n#### Lütfen Geçerli Bir Menu Rakamı Giriniz... ####\n")
                except ValueError:
                    print("\n#### Lütfen Bir Rakam Giriniz... ####\n")

                    

        elif menu==6:
            kure_menu=False
            while True:
                try:
                    
                    if kure_menu==False:
                        yaricap=int(input("\nYarıçap Uzunluğunu giriniz :"))
                        kure_menu=True
                    if kure_menu==True:
                        kure_hacim = 4/3*3.14*(yaricap**3)
                        print("\nKüre Hacim :", kure_hacim, " cm3\n")
                        kure_menu = int(input("""1- Tekrar İşlem Yapma
2- Ana Menü
3- Çıkış

Lütfen yapmak istediğiniz işlem numarasını giriniz :"""))
                    if kure_menu==1:
                        kure_menu=False
                        continue
                        
                    elif kure_menu==2:
                        break
                    elif kure_menu==3:
                        altmenu_cikis=1
                        break
                    else:
                        print("\n#### Lütfen Geçerli Bir Menu Rakamı Giriniz... ####\n")
                except ValueError:
                    print("\n#### Lütfen Bir Rakam Giriniz... ####\n") 



            
        else:
            print("\n#### Lütfen Geçerli Bir Menu Rakamı Giriniz... ####\n")              
        
    except ValueError:
        print("\n#### Lütfen Bir Rakam Giriniz... ####\n")



