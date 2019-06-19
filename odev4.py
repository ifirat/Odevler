print('*'*10 + 'FAIZ HESAPLAMA PROGRAMI' + '*'*10)

print('-'*5 + 'Lutfen istenilen bilgileri dogru ve eksiksiz giriniz!!!!!!'
      + '-' * 5, '\n')

##KULLANICIDAN ALINAN BILGILER

ana_para = input('Ana Para Miktari  : ')
yil      = input('Faiz Suresi (YIL) : ')
oran     = input('Faiz orani        : ')

## FAIZ HESAPLAMA FORMULU

faiz        = float(ana_para) * float(yil) * (float(oran)/100)
aylik_faiz  = faiz/(float(yil)*12)
gunluk_faiz = faiz/(float(yil)*365)
toplam_tutar= float(ana_para) + faiz

print('Toplam Faiz Tutari : ',faiz,' Euro','\n',
      'Aylik Faiz Tutari  : ', aylik_faiz, ' Euro', '\n',
      'Gunluk Faiz Tutari : ', gunluk_faiz, ' Euro', '\n',
      '='*40, '\n',
      'TOPLAM TUTAR       : ', toplam_tutar, ' Euro', sep='')

hesap_dosya = open('faizHesaplama.txt', 'w')

print('Ana Para Tutari    : ',ana_para,' Euro','\n',
      'Toplam Faiz Tutari : ',faiz,' Euro','\n',
      'Aylik Faiz Tutari  : ', aylik_faiz, ' Euro', '\n',
      'Gunluk Faiz Tutari : ', gunluk_faiz, ' Euro', '\n',
      '='*40, '\n',
      'TOPLAM TUTAR       : ', toplam_tutar, ' Euro', sep='', file=hesap_dosya)

hesap_dosya.close()

      
      
      
