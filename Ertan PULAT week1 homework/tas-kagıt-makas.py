#TAŞ,KAĞIT,MAKAS OYUNU
import random 

secimler = ["taş","kağıt","makas"]
print ("Taş,kağıt,makas oyunumuz 10 el sonunda bitecektir.")

while True :
    oyuncusecim = input("taş mı,kağıt mı,makas mı?:")
    bil_secim = random.choice(secimler)
   
    if secimler =="taş":   
        print("Bilgisayarın seçimi : Taş Sonuç:Berabere")
    elif secimler=="kağıt":
        print("Bilgisayarın seçimi : Kağıt Sonuç : Kaybettiniz ")
    else:   
        print("Bilgisayarın seçimi : Makas Sonuç : Kazandınız ")
        break
        