
gelir = input('Aylik Gelirinizi Giriniz  : ')

print('\n','*'*5 + 'AYLIK HARCAMA KALEMLERINI GIRINIZ!!!!!' + '*'*5, '\n')

mutfak = input('Mutfak Harcama Tutari  : ')
egitim = input('egitim Harcama Tutari  : ')
giyim  = input('giyim Harcama Tutari   : ')
ulasim = input('ulasim Harcama Tutari  : ')

aylik_masraf = int(mutfak) + int(egitim) + int(giyim) + int(ulasim)

print('='* 50, '\n','BIR AYLIK TOPLAM MASRAFINIZ : ', aylik_masraf, ' Euro', sep='')

oran = aylik_masraf / int(gelir)

print ('\n\n','AYLIK GELIRINIZIN AYLIK GIDERINIZE ORANI %', oran*100, 'dir', sep='') 

dosya = open ('aylikmasraf.txt', 'w')
print('Aylik Gelir            : ', gelir, ' Euro', '\n',
      '-'*50, '\n',
      'Mutfak Harcama Tutari  : ', mutfak, ' Euro','\n',
      'egitim Harcama Tutari  : ', egitim, ' Euro','\n',
      'giyim Harcama Tutari   : ', giyim, ' Euro','\n',
      'ulasim Harcama Tutari  : ', ulasim, ' Euro','\n',
      '='* 50, '\n','BIR AYLIK TOPLAM MASRAFINIZ : ', aylik_masraf, ' Euro', '\n',
       '\n\n','AYLIK GELIRINIZIN AYLIK GIDERINIZE ORANI %', oran*100, ' dir',
      sep='', file=dosya)

dosya.close()
