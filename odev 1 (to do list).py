
yapilacak_liste   = []
biten_liste     = []
cikis=0
cikis1=0
##listelemetodo = [(str(i+1) + "-" + str(yapilacak_liste[i]+"\n")) for i in range(len(yapilacak_liste))]
##listelemetodone = [[(str(i+1) + "-" + str(biten_liste[i]+"\n")) for i in range(len(biten_liste))]]
while cikis==0:
    try:
        if yapilacak_liste==[]:
            print("\nListenizde henuz hic gorev bulunmamaktadir.\n")
        else:
            
            for i in range(len(yapilacak_liste)):
                print(i+1,"-",yapilacak_liste[i])
            
    
        menu = int(input("""        1- Gorev Ekle
        2- Gorev Sil
        3- Gorev Atama
        4- Yapilan Gorevleri Goruntuleme
        5- Yapilacaklar Listesini Bosaltma
        6- Cikis

        Lutfen Yapmak Istediginiz Islemin Numarasini Giriniz : """))

        while cikis1==0:    
            if menu==1:
            
                if yapilacak_liste==[]:
                    print("Listenizde henuz hic gorev bulunmamaktadir.")
                else:
                    for i in range(len(yapilacak_liste)):
                        print(i+1,"-",yapilacak_liste[i])
                gorev = input("\nGorev Tanimini Giriniz (cikis icin:q):")
                    
                if not gorev:
                    print("Lutfen Bos birakmayiniz veya cikis icin 'q' tusunu kullaniniz")

                elif gorev in "qQ":
                    break
                else:    
                    yapilacak_liste.append(gorev)

            elif menu==2:
                try:
                    if yapilacak_liste==[]:
                        print("GOREV LISTENIZ BOSTUR...")
                        break
                    else:               
                        for i in range(len(yapilacak_liste)):
                            print(i+1,"-",yapilacak_liste[i])
                       
                        silinen = int(input("Silmek Istediginiz Gorevin Numarasini Giriniz (cikis '0') :"))
                        if silinen==0 :
                            break
                        else:
                            del yapilacak_liste[silinen-1]
                except ValueError:
                    print("Lutfen bos birakmayiniz ve bir sayi giriniz...")
                except IndexError:
                    print("Lutfen gecerli bir sayi giriniz...")
            elif menu==3:
                try:
                    
                    if yapilacak_liste==[]:
                        print("Yapilacak listenizde gorev bulunmamaktadir.")
                        break
                    else:
                        for i in range(len(yapilacak_liste)):
                            print(i+1,"-",yapilacak_liste[i])
                        atama = int(input("yapilanlar listesine aktarilacak gorev numarasini giriniz (CIKIS ICIN '0') :"))
                        if atama==0:
                            break
                        else:
                            atanmis = yapilacak_liste.pop(atama-1)
                            biten_liste.append(atanmis)     
                        
                            print("Listenizdeki '{}' Gorevi Yapilan Listesine Basari ile Aktarilmistir".format(atanmis))
                except IndexError:
                    print("Lutfen Gecerli Bir Sayi Giriniz...")
                except ValueError:
                    print("Lutfen bos birakmayiniz...")
            elif menu==4:
                if biten_liste==[]:
                    print("\nYAPILAN GOREV LISTENIZ BOSTUR...\n")
                    break
                else :                    
                    for i in range(len(biten_liste)):
                        print(i+1,"-",biten_liste[i])
                    break

            elif menu==5:
                soru=input("Yapilacaklar Listenizi silmek istediginizden eminmisiniz (E/H) :")
                if not soru:
                    print("Lutfen Bos Birakmayiniz")
                elif soru in "eE":
                    yapilacak_liste.clear()
                    print("Listeniz Silinmistir...")
                    break
                elif soru in "hH":
                    break
                else:
                    print("Lutfen 'E' veya 'H' seceneklerinden birini kulaniniz... ")
            elif menu==6:
                cikis=1
                break
            else:
                print("gecerli bir sayi giriniz...")
                break
            
    except ValueError:
        print("Lutfen bos birakmayiniz ve gecerli bir sayi giriniz")

            
