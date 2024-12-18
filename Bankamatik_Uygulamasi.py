#kayıt olmalı bankamatik sistemi
#MustBANK

def kayit(hesap):
    hesapAdi=str(input("Hesap adınızı giriniz :"))
    pin=int(input("PIN giriniz :"))
    baslangic_bakiye = float(input("Lütfen başlangiç bakiyenizi giriniz: "))
    hesap[hesapAdi] = {"pin": pin, "bakiye": baslangic_bakiye}

def giris(hesap):
    hesapAdi=str(input("Hesap adınızı giriniz :"))
    pin=int(input("PIN giriniz"))
    
    if hesapAdi in hesap and hesap[hesapAdi]["pin"]==pin:
        return hesapAdi
    else:
        return None

def bakiye_sorgu(hesap,hesapAdi):
    print(f"Hesabınızda {hesap[hesapAdi]["bakiye"]} TL bulunmaktadır.")

def para_yatir(hesap,hesapAdi,kullanilan_bakiye):
    hesap[hesapAdi]["bakiye"]+=kullanilan_bakiye
    print(f"{kullanilan_bakiye} TL hesabiniza yatirildi.Toplam Bakiye {hesap[hesapAdi]['bakiye']} TL")

def para_cek(hesap,hesapAdi,kullanilan_bakiye):
    if hesap[hesapAdi]["bakiye"]>=kullanilan_bakiye:
        hesap[hesapAdi]["bakiye"]-=kullanilan_bakiye
        print(f"{kullanilan_bakiye} TL hesabinizdan para çekildi.Toplam Bakiye {hesap[hesapAdi]['bakiye']} TL")
    else:
        print("Bakiye yetersiz")


def anagiris():

    print("MustBANK'A HOŞGELDİNİZ")

    hesap={}

    while True:
        print("\nYeni hesap aç [1]")
        print("\nHesaba giriş yap [2]")
        print("\nÇikiş yap [3]")
        secim = int(input("\nLütfen seçiminizi yapiniz (1/2/3) :"))
        if(secim==1):
            kayit(hesap)
        elif(secim==2):
            giris_yap=giris(hesap)
            if giris_yap:
                print("Giriş Başarılı")
                while True:
                    print("\n Bakiye sorgulama [1]")
                    print("\n Para yatirma [2]")
                    print("\n Para çekme [3]")
                    print("\n Çikiş yap [4]")
                    secim2 =int(input("Lütfen seçiminizi yapınız (1/2/3/4) "))
                    if secim2==1:
                        bakiye_sorgu(hesap,giris_yap)
                    elif secim2==2:
                        kullanilan_bakiye=float(input("Lütfen yatırmak istediğiniz tutarı yazınız :"))
                        para_yatir(hesap,giris_yap,kullanilan_bakiye)
                    elif secim2==3:
                        kullanilan_bakiye=float(input("Lütfen çekmek istediğiniz tutarı yazınız :"))
                        para_cek(hesap,giris_yap,kullanilan_bakiye)
                    elif secim2==4:
                        print("Hesabınızdan çıkış yapılıyor...")
            else :
                print("Hatalı pin girişi tekrar deneyiniz .")
        elif secim==3:
            print("Çıkış yapılıyor")
            break
        else :
            print("Hatalı bir seçim yaptınız")

anagiris()
