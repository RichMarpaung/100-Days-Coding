import os
import time
def pria (tinggi_badan):
    berat_ideal_pria = (tinggi_badan-100)-((tinggi_badan-100)*0.1)
    return(berat_ideal_pria)
def wanita(tinggi_badan):
    berat_ideal_waninta = (tinggi_badan-100)-((tinggi_badan-100)*0.15)
    return(berat_ideal_waninta)
lanjut = 'y'
while lanjut == 'y':    
    os.system('cls')
    print("="*10,"Menghitung Berat Badan Ideal",10*"=")
    print("Pilih Gender \n1. Laki-Laki\n2. Perempuan")
    pilih = input("Masukkan Gender : ")
    if pilih == '1':
        os.system('cls')
        tinggi = float(input("Masukkan Tinggi Badan Anda (dalam cm) : "))
        print(f"\nBerat Badan Ideal Anda adalah : {pria(tinggi)}Kg")
        print("\nApakah Anda Mau Ulang? : ")
        lanjut = input("y/n :")

    elif pilih == '2':
        os.system('cls')
        tinggi = float(input("Masukkan Tinggi Badan Anda (dalam cm) : "))
        print(f"\nBerat Badan Ideal Anda adalah : {pria(tinggi)}Kg")
        print("\nApakah Anda Mau Ulang? ")
        lanjut = input("y/n :")
    else :
        os.system('cls')
        print("Pilihan Anda Tidak Tersedia")
        time.sleep(3)
        lanjut = 'y'

os.system('cls')
print("="*10,"Program Selesai",10*'=')