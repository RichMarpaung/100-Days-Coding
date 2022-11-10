import os
import time
os.system('cls')

x = []
y = []
z = []
def tambah():
    nama = input("Masukkan Nama Anda\t: ")
    nim = input("Masukkan nim Anda\t: ")
    umur = input("Masukkan umur Anda\t: ")
    x.append(nama)
    y.append(nim)
    z.append(umur)
def cetak():
    c1 = len(x)
    for i in range (c1):
        print(f"\n===  Data{i+1}  ===")
        print(f"Nama\t: {x[i]}")
        print(f"nim\t: {y[i]}")
        print(f"umur\t: {z[i]}")

def ubah():
    ubah = int(input("Data yang mau di ubah :"))
    x[ubah-1] = input("Masukkan Nama Baru : ")
    y[ubah-1] = input("Masukkan NIM Baru : ")
    z[ubah-1] = input("Masukkan Umur Baru : ")

def hapus():
    hapus = int(input("Masukkan Data yang mau dihapus : "))
    hapus_nama = x[hapus-1]
    hapus_nim = y[hapus-1]
    hapus_umur = z[hapus-1]
    x.remove(hapus_nama)
    y.remove(hapus_nim)
    z.remove(hapus_umur
    )
while True:
    os.system('cls')
    print("=====  Menu  =====")
    print("1. Tambah Data\n2. Ubah Data\n3. Cetak Data\n4. Hapus Data")
    ask = input("\nMasukkan Pilihan\t: ")
    if ask == "1":
        os.system('cls')
        lanjut = 'y'
        while lanjut == 'y':
            print("Menambah Data\n")
            tambah()
            cetak()
            print("\nApakah Anda Ingin Menambah Data lagi?")
            lanjut = input("y/n : ")
    elif ask == "2":
        os.system('cls')
        cetak()
        ubah()
    elif ask == "3":
        os.system('cls')
        menu = 'n'
        while menu == 'n':
            cetak()
            menu = input("\nKembali ke Menu y/n : ")
    elif ask == '4':
        cetak()
        hapus()
    else:
        os.system('cls')
        print("Pilihan Tidak Tersedia Coba lagi")
        time.sleep(3)
