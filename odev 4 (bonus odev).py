liste_sayi = ['1','2','3','4','5','6','7','8','9','10']
liste_harf = ['a','b','c','d','e','f','g','h','i','j']

kombinasyon1 = [a+b for a in liste_sayi for b in liste_harf]
kombinasyon2 = [b+a for b in liste_harf for a in liste_sayi]

print(kombinasyon1,"\n\n\n")
print(kombinasyon2)
