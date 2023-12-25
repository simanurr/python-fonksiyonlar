def bölen(sayı):
    for i in range(1,sayı):
        if(sayı % i == 0):
            print(i)
while(True):
    sayı = input("sayı giriniz(çıkmak için q ya basın):")
    if(sayı == "q"):
        print("programdan çıkılıyor...")
        break
    else:
        sayı = int(sayı)
        bölen(sayı)