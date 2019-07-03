
while True:
    try:
    
        sayi=int(input("asal sayi olup olamdigini ogrenmek istediginiz pozitif tamsayi :"))

        if sayi<=1:
            print("""Yalniz 1'e ve kendisine kalansiz bolunebilen
        1'den buyuk dogal sayilara asal say denir""")
            print("\nLUTFEN 1'DEN BUYUK BIR SAYI GIRINIZ\n")
        elif sayi!=2 and sayi%2==0:
            print("girmis oldugunuz", sayi, " sayisi asal sayi DEGILDIR.\n")
        elif sayi!=3 and sayi%3==0:
            print("girmis oldugunuz", sayi, " sayisi asal sayi DEGILDIR.\n")
        elif sayi!=5 and sayi%5==0:
            print("girmis oldugunuz", sayi, " sayisi asal sayi DEGILDIR.\n")
        else:
            print("girmis oldugunuz", sayi, " sayisi asal sayidir.\n") 

    except ValueError:
        print("Lutfen bir sayi giriniz...\n")
