Adı = input ("Adınızı Giriniz:")
Soyadı = input ("Soyadınızı Giriniz:")
Numara = int(input ("Numaranızı Giriniz:"))
Ders_adı = input ("Ders Adını Giriniz:")
Vize_Notu = int(input ("Vize Notunuzu Giriniz:"))
Final_Notu = int(input ("Final Notunuzu Giriniz:"))
Yıl_sonu_ort = (int(Vize_Notu) + int(Final_Notu))/2
if (Yıl_sonu_ort) <= 50 :
    print("Dersten Kaldınız")
else :
    print ("Dersten Geçtiniz")
    
