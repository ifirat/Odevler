print("####    SAYI TAHMIN OYUNU    ####")

sayi = 28
deneme_sayisi=0
   
while True:
    try:
                
        tahmin=int(input("0-100 arasinda bir sayi giriniz :"))
        deneme_sayisi += 1          
                
                
        if tahmin > sayi :
            fark = tahmin - sayi
            if fark > 50:
                print("\nCok yuksek tahminde bulundun, daha dusuk bir sayi girmelisin\n")
            elif 50 >= fark >= 20:
                print("\nYuksek bir tahminde bulundun, daha dusuk bir sayi girmelisin\n")
            elif 20 > fark > 8 :
                print("\nYaklastin daha biraz daha inmelisin\n")
            elif 8 >= fark >= 1 :
                print("\nCok yaklastin biraz daha inmelisin\n")
            elif fark==0 :
                print("\ntebrikler sayiyi ", deneme_sayisi , ". denemede buldunuz\n")
                break
        
        else:
            fark = sayi - tahmin
            if fark > 50:
                print("\nCok dusuk tahminde bulundun, daha yuksek bir sayi girmelisin\n")
            elif 50 >= fark >= 20:
                print("\nDusuk bir tahminde bulundun, daha yuksek bir sayi girmelisin\n")
            elif 20 > fark > 8 :
                print("\nYaklastin daha biraz daha cikmalisin\n")
            elif 8 >= fark >= 1 :
                print("\nCok yaklastin biraz daha cikmalisin\n")
            elif fark==0 :
                print("\ntebrikler sayiyi ", deneme_sayisi , ". denemede buldunuz\n")
                break
  
    except ValueError:
        print("####  Lutfen bir sayi giriniz  ####")
    
    
