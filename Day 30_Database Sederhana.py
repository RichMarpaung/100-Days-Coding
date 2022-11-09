import os
import time
os.system("cls")
nama = ["Rich Rona S. Marpaung"]
umur =["20"]
nim =["D0222307"]

while True :
    os.system("cls")
    ask = input("""===== Option =====
    1. Tambah Data
    2. Rubah Data
    3. Tampilkan Data
    4. Hapus Data

    Masukkan Pilihan\t: """)
    print("\n")
    if ask == "1" :
        start = "y"
        while (start == "y") :
            os.system("cls")
            print("Masukkan Data Diri")
            nama2 = input("Masukkan Nama Anda :")
            umur2 = input("Masukkan Umur Anda :")
            nim2= input("Masukkan NIM Anda :")
            nama.append(nama2)
            umur.append(umur2)
            nim.append(nim2)
            #ask = input("Mau Nambah Data? y/n\t:")
            c1 = len(nama)
            for i in range(c1) :
                print( 5*"=","Data",i+1,5*"=")
                print (f"Nama\t:{nama[i]}")
                print (f"Um   ur\t:{umur[i]}")
                print (f"NIM\t:{nim[i]}\n")
            start = input("Mau Menambah Data? y/n\t:")
    elif ask == "2" :
        os.system("cls")
        c2 = len(nama)
        print(f"{'DATA SAAT INI':^40}\n")
        for i in range(c2):
            print(5*"=","Data",i+1,5*"=") 
            print (f"Nama\t:{nama[i]}")
            print (f"Umur\t:{umur[i]}")
            print (f"NIM\t:{nim[i]}\n")
        print ("Merubah Data")
        ubah = int(input("Data Berapa Yang Mau di Ubah\t:"))
        nama[ubah-1] = input("Masukkan Nama Baru\t:")
        umur[ubah-1] = input("Masukkan Umur Baru\t:")
        nim[ubah-1] = input("Masukkan NIM Baru\t:")
        print("\n")

    elif ask == "3":
        os.system("cls")
        tanya = "n"
        while tanya =="n":
            tampil = len(nama)
            print(f"{'DATA SAAT INI':^40}\n")
            for i in range(tampil):
                print(5*"=","Data",i+1,5*"=")
                print (f"Nama\t:{nama[i]}")
                print (f"Umur\t:{umur[i]}")
                print (f"NIM\t:{nim[i]}\n")
            tanya = input("Kembali Ke Menu Awal y/n : ")
    elif ask == "4":
        
        os.system("cls")
        c4 = len(nama)
        for i in range(c4):
            print(5*"=","Data",i+1,5*"=")
            print (f"Nama\t:{nama[i]}")
            print (f"Umur\t:{umur[i]}")
            print (f"NIM\t:{nim[i]}\n")
        print("\nPilih Data yang akan Di Hapus")
        hapus = int(input("Hapus Data\t:"))
        hapus_nama = nama[hapus-1]
        hapus_umur = umur[hapus-1]
        hapus_nim = nim[hapus-1]
        nama.remove(hapus_nama)
        umur.remove(hapus_umur)
        nim.remove(hapus_nim)
    else :
        os.system('cls')
        print("Masukkan Option Yang ada!!")
        time.sleep(5)