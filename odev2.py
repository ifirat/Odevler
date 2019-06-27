print("####   UZAKLIK BIRIMI DONUSUMU    ##### \n,\n")

donusum = "1"

while donusum != "q":       ## degisken Q dan farkliysa döngüyü baslatmak icin input almaya devam et
    donusum = input("""
KM ===> MIL donusumu icin '1' tusuna basiniz
MIL ===> KM donusumu icin '2' tusuna basiniz
ÇIKMAK İÇİN 'Q' TUŞUNA BASINIZ
:""")
    if donusum == "q":      ## degisken Q ise donguden cik
        print("programdan cikiyorsunuz....", "\n")
    elif donusum == "1":    ## degisken 1 ise km ==> mil donusumunu hesaplayip ekrana yazdir ve donguye devam et
        km_donusum = input("KM olarak uzunlugu giriniz :")
        sonuc = float(km_donusum) / 1.609344
        print( km_donusum , "KM ====> ", sonuc , " Mildir", "\n")   
    elif donusum == "2":    ## degisken 2 ise mil ==> km donusumunu hesaplayip ekrana yazdir ve donguye devam et
        mil_donusum = input("MIL olarak uzunlugu giriniz :")
        sonuc = float(mil_donusum) * 1.609344
        print( mil_donusum , "MIL ====> ", sonuc , " KM dir", "\n")
    else:                   ## menude istenen degerlerden farkli bir deger girilirse, kullaniciyi uyar ve donguye devam et
        print("Lutfen '1' veya '2' degerlerinden birini giriniz !!!", "\n")
        
    




