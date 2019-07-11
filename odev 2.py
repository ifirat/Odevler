

kucuk_harf="qwertyuiopasdfghjklzxcvbnmğüşıöç"
buyuk_harf="QWERTYUIOPASDFGHJKLZXCVBNMĞÜŞİÖÇ"
sayi = "1234567890"
k_harf_kumesi=""
b_harf_kumesi=""
sayi_kumesi=""
diger=""

while True:
    
    veri = input("Bír yazi giriniz :")
    if veri=="":
        print("Lutfen bos birakmayiniz")
    else:
        for i in veri:
            if i in kucuk_harf:
                k_harf_kumesi += i
            elif i in buyuk_harf:
                b_harf_kumesi += i
            elif i in sayi:
                sayi_kumesi += i
            else:
                diger+=i

    print("""\n Girmiş olduğunuz "{}" yazısında\n
    {} adet büyük harf
    {} adet küçük harf
    {} adet sayı
    {} adet diğer semboller vardır.\n""".format(veri, len(k_harf_kumesi), len(b_harf_kumesi), len(sayi_kumesi), len(diger)))
        
