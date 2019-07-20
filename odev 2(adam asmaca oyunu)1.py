woord = "bisiklet"

sayac=0
sekil=["","","","","","",""]
sonuc=[]
hak=6

for a in range(len(woord)):
    sonuc.append("-")


adam=["|","|","|","|","_____","|"]


        
while True:
                  

        icerik = """                        {4}
                       {3}     {5}               {7} HAKKINIZ KALDI!!!
                       {2}     {6}       
                       {1}
                       {0}
                       ---"""
        print(icerik.format(sekil[0],sekil[1],sekil[2],sekil[3]
                            ,sekil[4],sekil[5],sekil[6],hak))
        
        print(*sonuc)
        if hak==0 :
            break
        letter = input("Bir Harf Giriniz :")
        konum=-1
        
        

        if not letter:
                print("Lutfen Bos Birakmayiniz")
        elif len(letter)>1:
                print("Lutfen Tek bir Harf giriniz")
        elif not letter.isalpha():
                print("Lutfen Sadece Harf Giriniz.")
        elif letter in sonuc:
            print("BU HARFI DAHA ONCE BILDINIZ. LUTFEN FARKLI BIR HARF GIRINIZ.")
        elif sayac==5:
            
            sekil[6]="0"
            sekil[sayac]="|"
            print("NE YAZIK KI OYUNU KAYBETTINIZ")
            hak = 0
            
            for a in range(len(woord)):
                sonuc[a]=woord[a]
            print("DOGRU CEVAP :",*sonuc)
            
        else:
            if letter not in woord:
                print("Bu Harf Bulunamamistir.")
                sayac+=1
                hak-=1
                if sayac<6:
                    sekil[sayac-1]=adam[sayac-1]
                   
                
                
            elif letter in woord:
                for i in woord:
                    konum+=1
                    if i==letter:
                        sonuc[konum]=letter
                       
                        
                    
                    
  
