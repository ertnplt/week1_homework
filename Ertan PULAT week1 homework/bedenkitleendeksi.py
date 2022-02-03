print("Beden Kitle Endeksi Hesaplama Programına Hoşgeldiniz.")
Kilo = float(input("Kilonuzu Giriniz (kg):"))
Boy = float(input("Boyunuzu Giriniz (m):"))
Beden_Kitle_Endeksi = Kilo/(Boy*Boy)
if Beden_Kitle_Endeksi < 25:
    print("NORMAL DEĞERDESİNİZ")
elif Beden_Kitle_Endeksi >=25 and Beden_Kitle_Endeksi >=30:
    print ("FAZLA KİKOLUSUNUZ")
elif Beden_Kitle_Endeksi >=30 and Beden_Kitle_Endeksi >=40:
    print("OBEZ")
else:
    print("AŞIRI KİLOLU")

    
         