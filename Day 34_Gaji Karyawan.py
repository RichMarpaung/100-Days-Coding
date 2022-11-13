import os
print("Menentukan Gaji Karyawan Sesuai Golongan")
nama = input("Masukkan Nama Anda : ")
golongan = input("Masukkan Golongan A,B,C,D : ")
jam = int(input("Masukkan Jam Kerja (dalam jam): "))

#Gaji Pokok
if golongan == 'A' or golongan == 'a':
    total_gaji = jam*5000
elif golongan == 'B' or golongan == 'b':
    total_gaji = jam*7000
elif golongan == 'C' or golongan == 'c':
    total_gaji = jam*8000
elif golongan == 'D' or golongan == 'd':
    total_gaji = jam*10000

#Gaji lembur
if jam > 48 :
    total_gaji = total_gaji + (jam-48)*4000
os.system('cls')
print (f"Nama \t : {nama}\nGolongan : {golongan}\nJam Kerja: {jam} Jam")
print(f"\nGaji anda adalah :Rp.{total_gaji}")