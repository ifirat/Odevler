
try:
    with open("futbolcular.txt","r") as takim:
        takim.seek(0)
        icerik=takim.readline()
        for line in takim:
            if "Fenerbahçe" in line:
                with open("Fenerbahce.txt","a+") as fener:
                    fener.write(line)
            elif "Galatasaray" in line:
                with open("Galatasaray.txt","a+") as cimbom:
                    cimbom.write(line)
            elif "Besiktas" in line:
                with open("Besiktas.txt","a+") as kartal:
                    kartal.write(line)       
except FileNotFoundError:
    print("Kaynak dosya bulunamadi. Lutfen kontrol ediniz....")


