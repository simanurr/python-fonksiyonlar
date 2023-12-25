def asal(sayı):
    if(sayı == 1):
        return False
    elif(sayı == 2):
        return True
    else:
        for i in range(2,sayı):
            if(sayı % i == 0):
                return False
        return True
while(True):
    sayı = input("sayı giriniz(çıkmak için q ya basın):")
    if(sayı == "q"):
        print("programdan çıkıldı")
        break
    else:
        sayı = int(sayı)
        if(asal(sayı)):
            print("asal sayıdır.")
        else:
            print("asal sayı değildir.")