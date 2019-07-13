turkce_karakterler    = "üğşıçöÜĞİŞÇÖ"
ingilizce_karakterler = "ugsicoUGISCO"
ceviri = str.maketrans(turkce_karakterler, ingilizce_karakterler)

with open("futbolcular.txt", "r") as ana_dosya:
##    ana_dosya.seek(0)
##    isim = ana_dosya.readlines()

    for i in ana_dosya:
        i=i.translate(ceviri)
        with open("isimlistesiingilizce.txt","a+") as alt_dosya:
            alt_dosya.write(i)
        
