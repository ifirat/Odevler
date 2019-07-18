sayi=1224


while True:
    try :
        tahmin=int(input("Tahmininizi Giriniz:"))

        if 1000 > tahmin or tahmin > 9999 :
            print("Lutfen 999' dan buyuk ve 10.000 den kucuk bir sayi giriniz")
            continue
            
        miktar=0
        ayni=0
        miktar1=0
        sayi_konumlu=[]
        tahmin_konumlu=[]
        tahmin=str(tahmin)
        sayi=str(sayi)
        
     
        for i in range(len(sayi)):                  # sayi ve konumu yan yana yazacak sekilde her elemani iki farkli sayidan yeni bir liste olusturuldu
            sayi_konumlu.append([sayi[i],i])
        

        for i in range(len(tahmin)):                # tahmin ve konumu yan yana yazacak sekilde her elemani iki farkli sayidan olusan yeni bir liste olusturuldu
            tahmin_konumlu.append([tahmin[i],i])
        

        for i in tahmin_konumlu:      # bu konumlu iki liste karsilastirildi ve buradan tam eslesen rakamlarin sayisi tespit edildi.          
            if i in sayi_konumlu:
                ayni+=1
        
        for a in sayi:                # bu dongude sayimizin icindeki rakamlar tahmin edilen sayi icerisinde dondurulerek kac tane rakamin ayni oldugu bilgisi alindi
            if a in tahmin:
                miktar+=1
        

        for a in tahmin:                # bir onceki for dongusunde eger sayi icinde birden fazla ayni rakam varsa hatali islem yapiyor. tam tersi durumda bu dongude tahmin icinde birden fazla rakam varsa hatali islem yapiyor. bunu onlemek icin her iki durumu da dikkate alip dogru olani kullacak kosul olusturduk
            if a in sayi:
                miktar1+=1
        

        if miktar>miktar1:       # sayilarin icerisinde ayni rakamdan birden fazla olursa hatali islem yaptigindan dolayi bu if else komutunu yazdik
            print("\nSONUC :  +",ayni , "  " , ayni-miktar1, "\n")   # tam eslesen sayisindan ayni rakam miktari cikarilarak istenilen sonuc elde edildi. 
        else:
            print("\nSONUC :  +",ayni , "  " , ayni-miktar, "\n")
    except ValueError:
        print("Lutfen Bos Birakmayiniz ve Sayi Giriniz...")



    
