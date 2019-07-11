

rakam = "0123456789"


while True:
    giris = input("Lutfen giris yapiniz :")
    toplam = 0
    rakamlar=""
    if giris=="":
        print("\nLutfen bos birakmayiniz......\n")

    else:
        for i in giris:
            if i in rakam:
                toplam +=int(i)
                rakamlar+=i
        if rakamlar!="":
            print("\nGirmis oldugunuz ** {} ** verisindeki rakamlarin toplami ** {} ** dir.\n".format(giris, toplam))

        else:
            print("\nGirmis oldugunuz ** {} ** verisinde hic rakam BULUNMAMAKTADIR..\n".format(giris))
            
