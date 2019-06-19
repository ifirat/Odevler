kelime = input("Bir Kelime Giriniz : ")

print("*"*(len(kelime)+6),
      "\n", "|*|", " "*len(kelime), "|*|",
      "\n", "|*|", " "*len(kelime), "|*|",
      "\n", "|*|", kelime, "|*|",
      "\n", "|*|", "-"*len(kelime),"|*|",
      "\n", "|*|", " "*len(kelime), "|*|",
      "\n", "|*|", " "*len(kelime), "|*|",
      "\n", "*"*(len(kelime)+6), sep="")
