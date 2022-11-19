import os
def kenetik (masa,kecepatan):
    energi_kenetik = 1/2 *(masa*(kecepatan**2))
    if energi_kenetik % 2 == 0 or energi_kenetik %2==1:
        return int(energi_kenetik)
    else:
        return round(energi_kenetik,2)
def potensial (masa,tinggi,grafitasi = 10):
    energi_potensial = masa*grafitasi*tinggi
    if energi_potensial % 2 == 0 or energi_potensial %2==1:
        return int(energi_potensial)
    else:
        return round(energi_potensial,2)
def mekanik (kenetik,potensial):
    energi_mekanik = kenetik+potensial
    if energi_mekanik % 2 == 0 or energi_mekanik %2==1:
        return int(energi_mekanik)
    else:
        return round(energi_mekanik,2)
    
lanjut = 'y'
while lanjut == 'y' or lanjut == "Y":
    os.system('cls')
    print("Perhitungan Energi\n1. Energi Kenetik\n2. Energi Potensial\n3. Energi Mekanik")
    pilih = input("\nMasukkan Pilihan anda : ")
    if pilih == '1':
        os.system('cls')
        print(11*"=","Energi Kenetik",11*"=")
        m = float(input("Masukkan Massa Benda (kg)\t: "))
        v = float(input("Masukkan Kecepatan Benda (m/s)\t: "))
        print(38*"=")
        print(f"Energi Kenekik : {kenetik(m,v)} joule")
    elif pilih == '2':
        os.system('cls')
        print(11*"=","Energi Potensial",11*"=")
        m = float(input("Masukkan Massa Benda (kg): "))
        h = float(input("Masukkan Tinggi Benda (m): "))
        g = float(input("Masukkan Grafitasi (m/s)): "))
        print(38*"=")
        print(f"Energi Potensial : {potensial(m,h,g)} joule")
    elif pilih == '3':
        os.system('cls')
        print(11*"=","Energi Mekanik",11*"=")
        k = float(input("Masukkan Energi Kenetik (joule)\t: "))
        p = float(input("Masukkan Massa Benda (joule)\t: "))
        print(38*"=")
        print(f"Energi Mekanik : {mekanik(k,p)} joule")
    else:
        os.system('cls')
        print("Pilihan Tidak Valid !!!")
    
    lanjut = input("\nMulai Program Lagi Y/N : ")



        
