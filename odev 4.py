
sesli_harfler = "euıoüaiöEUIOÜAİÖ"

with open("futbolcular.txt", "r") as ana_dosya:
##    ana_dosya.seek(0)
##    isim = ana_dosya.readlines()

    for i in ana_dosya:
        if i[0] in sesli_harfler:
            with open("isimlistesi.txt","a+") as alt_dosya:
                alt_dosya.write(i)
        
