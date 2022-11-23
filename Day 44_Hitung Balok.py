import os
import time
def keliling_balok ():
    panjang = float(input("Masukkan Panjang Balok \t: "))
    lebar = float(input("Masukkan Lebar Balok \t: "))
    tinggi = float(input("Masukkan Tinggi Balok \t: "))
    kel = 4*(panjang*lebar*tinggi)
    if kel % 2 == 1 or kel % 2 == 0 :
        kel = int(kel)
    else:
        kel = round(kel,2)
    os.system('cls')
    print(40*'=')
    print(f"Panjang Balok \t: {panjang} cm")
    print(f"Lebar Balok \t: {lebar} cm")
    print(f"Tinggi Balok \t: {tinggi} cm")
    print(f"Keliling Balok  \t: {kel} cm")
    print(40*'=')
def luas_balok ():
    panjang = float(input("Masukkan Panjang Balok \t: "))
    lebar = float(input("Masukkan Lebar Balok \t: "))
    tinggi = float(input("Masukkan Tinggi Balok \t: "))
    luas = 2*((panjang*lebar)+(lebar*tinggi)+(panjang*tinggi))
    if luas % 2 == 1 or luas % 2 == 0 :
        luas = int(luas)
    else:
        luas = round(luas,2)
    os.system('cls')
    print(40*'=')
    print(f"Panjang Balok \t: {panjang} cm")
    print(f"Lebar Balok \t: {lebar} cm")
    print(f"Tinggi Balok \t: {tinggi} cm")
    print(f"Luas Balok \t: {luas} cm²")
    print(40*'=')
def volume_balok () : 
    panjang = float(input("Masukkan Panjang Balok \t: "))
    lebar = float(input("Masukkan Lebar Balok \t: "))
    tinggi = float(input("Masukkan Tinggi Balok \t: "))
    volume = panjang*lebar*tinggi
    if volume % 2 == 1 or volume % 2 == 0 :
        volume = int(volume)
    else:
        volume = round(volume,2)
    os.system('cls')
    print(40*'=')
    print(f"Panjang Balok \t: {panjang} cm")
    print(f"Lebar Balok \t: {lebar} cm")
    print(f"Tinggi Balok \t: {tinggi} cm")
    print(f"Volume Balok \t: {volume} cm³")
    print(40*'=')
def sisi_balok ():
    os.system('cls')
    print("Mencari Sisi Balok\n1. Panjang Balok\n2. Lebar Balok\n3. Tinggi Balok")
    tanya = input("Masukkan Yang di Cari 1-3 : ")
    if tanya == '1':
        os.system('cls')
        print("Yang di Diketahui \n1. Luas Balok\n2. Volume Balok")
        dik = input("Masukkan Yang di Ketahui 1-2 : ")
        if dik == '1':
            os.system('cls')
            luas = float(input("Masukkan Luas Balok \t: "))
            lebar = float(input("Masukkan Lebar Balok \t: "))
            tinggi = float(input("Masukkan Tinggi Balok \t: "))
            panjang = ((luas/2)-(lebar*tinggi))/(lebar+tinggi)
            if panjang%2==1 or panjang%2==0:
                panjang = int(panjang)
            else :
                panjang = round(panjang,2)
            os.system('cls')
            print(40*"=")
            print(f"Luas Balok \t:{luas} cm²\nLebar Balok \t: {lebar} cm\nTinggi Balok \t: {tinggi} cm")
            print(f"Tinggi Balok \t: {tinggi}")
            print(40*"=")
            
        elif dik == '2':
            os.system('cls')
            volume = float(input("Masukkan Volume Balok \t: "))
            lebar = float(input("Masukkan Lebar Balok \t: "))
            tinggi = float(input("Masukkan Tinggi Balok \t: "))
            panjang = volume/(lebar*tinggi)
            if panjang%2==1 or panjang%2==0:
                panjang = int(panjang)
            else :
                panjang = round(panjang,2)
            os.system('cls')
            print(40*"=")
            print(f"Volume Balok \t:{volume} cm³\nLebar Balok \t: {lebar} cm\nTinggi Balok \t: {tinggi} cm")
            print(f"Panjang Balok : {lebar}")
            print(40*"=")
    elif tanya == '2':
        os.system('cls')
        print("Yang di Diketahui \n1. Luas Balok\n2. Volume Balok")
        dik = input("Masukkan Yang di Ketahui 1-2 : ")
        if dik == '1':
            os.system('cls')
            luas = float(input("Masukkan Luas Balok \t: "))
            panjang = float(input("Masukkan Panjang Balok \t: "))
            tinggi = float(input("Masukkan Tinggi Balok \t: "))
            lebar = ((luas/2)-(panjang*tinggi))/(panjang+tinggi)
            if lebar%2==1 or lebar%2==0:
                lebar = int(lebar)
            else :
                lebar = round(lebar,2)
            os.system('cls')
            print(40*"=")
            print(f"Luas Balok \t:{luas} cm²\nPanjang Balok \t: {panjang} cm\nTinggi Balok \t: {tinggi} cm")
            print(f"Lebar Balok \t: {lebar}")
            print(40*"=")
        elif dik == '2':
            os.system('cls')
            volume = float(input("Masukkan Volume Balok \t: "))
            panjang = float(input("Masukkan Panjang Balok \t: "))
            tinggi = float(input("Masukkan Tinggi Balok \t: "))
            lebar = volume/(panjang*tinggi)
            if lebar%2==1 or lebar%2==0:
                lebar = int(lebar)
            else :
                lebar = round(lebar,2)
            os.system('cls')
            print(40*"=")
            print(f"Volume Balok \t:{volume} cm³\nPanjang Balok \t: {panjang} cm\nTinggi Balok \t: {tinggi} cm")
            print(f"Lebar Balok \t: {lebar}")
            print(40*"=")
    elif tanya == '3':
        os.system('cls')
        print("Yang di Diketahui \n1. Luas Balok\n2. Volume Balok")
        dik = input("Masukkan Yang di Ketahui 1-2 : ")
        if dik == '1':
            os.system('cls')
            luas = float(input("Masukkan Luas Balok \t: "))
            panjang = float(input("Masukkan Panjang Balok \t: "))
            lebar = float(input("Masukkan lebar Balok \t: "))
            tinggi = ((luas/2)-(panjang*lebar))/(panjang+lebar)
            if tinggi%2==1 or tinggi%2==0:
                tinggi = int(tinggi)
            else :
                tinggi = round(tinggi,2)
            os.system('cls')
            print(40*"=")
            print(f"Luas Balok \t:{luas} cm²\nPanjang Balok \t: {panjang} cm\nLebar Balok \t: {lebar} cm")
            print(f"Tinggi Balok \t: {tinggi}")
            print(40*"=")
        elif dik == '2':
            os.system('cls')
            volume = float(input("Masukkan Volume Balok \t: "))
            panjang = float(input("Masukkan Panjang Balok \t: "))
            lebar = float(input("Masukkan lebar Balok \t: "))
            tinggi = volume/(panjang*lebar)
            if tinggi%2==1 or tinggi%2==0:
                tinggi = int(tinggi)
            else :
                tinggi = round(tinggi,2)
            os.system('cls')
            print(40*"=")
            print(f"Volume Balok \t: {volume} cm³\nPanjang Balok \t: {panjang} cm\nLebar Balok \t: {lebar} cm")
            print(f"Tinggi Balok \t: {tinggi}")
            print(40*"=")
        else:
            print("Pilihan Tidak Valid!!!")
            time.sleep(5)
            lanjut = 'y'

lanjut = 'y'
while lanjut == 'y'or lanjut == "Y":
    os.system('cls')
    print(11*"=","PERHITUNGAN BALOK",11*"=")
    print("1. Keliling Balok\n2. Luas Balok \n3. Volume Balok \n4. Sisi Balok")
    print(40*"=")
    pilih = input("Masukkan Pilihan (1-4) : ")
    if pilih == '1' :
        os.system('cls')
        keliling_balok()
        lanjut = input("Apakah Mau Mengulang Program Y/N : ")
    elif pilih == '2':
        os.system('cls')
        luas_balok()
        lanjut = input("Apakah Mau Mengulang Program Y/N : ")
    elif pilih == "3":
        os.system('cls')
        volume_balok()
        lanjut = input("Apakah Mau Mengulang Program Y/N : ")
    elif pilih == '4':
        os.system('cls')
        sisi_balok()
        lanjut = input("Apakah Mau Mengulang Program Y/N : ")
    else:
        print('Pilihan Anda Tidak VALID !!!!')
        time.sleep(5)
        lanjut = 'y'

