import os
os.system('cls')
def volume (sisi):
    vol = sisi**3
    if vol % 2 ==1 and vol % 2 ==0:
        return int(vol)
    return vol
def keliling (sisi):
    kel = sisi*12
    if kel % 2 ==1 or kel % 2 ==0:
        return int(kel)
    return kel
def luas_kubus (sisi):
    luas = 6*sisi*sisi
    if luas % 2 ==1 or luas % 2 ==0:
        return int(luas)
    return l
def sisi_luas (luas) : 
    sisi = luas**(1/2) / 6 
    if sisi % 2 ==1 or sisi % 2 ==0:
        return int(sisi)
    return sisi
def sisi_vol (volume):
    sisi = volume**(1/3)
    if sisi % 2 ==1 or sisi % 2 ==0:
        return int(sisi)
    return sisi
lanjut = 'y'
while lanjut == 'y'or lanjut == "Y":
    os.system('cls')
    print(11*"=","PERHITUNGAN KUBUS",11*"=")
    print("1. Keliling Kubus\n2. Volume Kubus\n3. Luas Kubus\n4. Sisi Kubus")
    print(40*"=")
    pilih = input("Masukkan Pilihan (1-4) : ")
    if pilih == '1':
        sisi = float(input("Masukkan Panjang Sisi (cm): "))
        if sisi % 2 ==1 or sisi % 2 ==0:
            sisi = int(sisi)
        os.system('cls')
        print(40*"=")
        print(f"Panjang sisi \t: {sisi} cm")
        print(f"Keliling Kubus \t: {keliling(sisi)} cm")
        print(40*"=")
        lanjut = input("Apakah Mau Mengulang Program Y/N : ")
    elif pilih=='2':
        sisi = float(input("Masukkan Panjang Sisi (cm): "))
        if sisi % 2 ==1 or sisi % 2 ==0:
            sisi = int(sisi)
        os.system('cls')
        print(40*"=")
        print(f"Panjang sisi \t: {sisi} cm")
        print(f"Volume Kubus \t: {volume(sisi)} cm³")
        print(40*"=")
        lanjut = input("Apakah Mau Mengulang Program Y/N : ")
    elif pilih=='3':
        sisi = float(input("Masukkan Panjang Sisi (cm): "))
        if sisi % 2 ==1 or sisi % 2 ==0:
            sisi = int(sisi)
        os.system('cls')
        print(40*"=")
        print(f"Panjang sisi \t: {sisi} cm")
        print(f"Luas Kubus \t: {luas(sisi)} cm²")
        print(40*"=")
        lanjut = input("Apakah Mau Mengulang Program Y/N : ")
    elif pilih=='4':
        print("Diketahui : \n1. Luas \n2.Volume")
        dik = input("Apa yang di Ketahui (1-2) : ")
        os.system('cls')
        if dik == '1':
            luas = float(input("Masukkan Luas Kubus : "))
            os.system('cls')
            print(40*"=")
            print(f"Luas Kubus : {luas} cm²")
            print(f"Panjang Sisi Kubus : {round(sisi_luas(luas))} cm")
            print(40*"=")
            lanjut = input("Apakah Mau Mengulang Program Y/N : ")
        elif dik == '2':
            luas = float(input("Masukkan Luas Kubus : "))
            os.system('cls')
            print(40*"=")
            print(f"Volume Kubus : {luas} cm³")
            print(f"Panjang Sisi Kubus : {round(sisi_vol(luas))} cm")
            print(40*"=")
            lanjut = input("Apakah Mau Mengulang Program Y/N : ")
        else:
            print("Pilihan Tidak Valid")
    else :
        print("Pilihan Tidak Valid")
    


