import os
tgl_ini = int(input("Masukkan Tanggal Saat ini : "))
bln_ini = int(input("Masukkan Bulan Saat ini (dalam angka) : "))
thn_ini = int(input("Masukkan Tahun Saat ini : "))

print(40*"=")
tgl_tuju =int(input("Masukkan Tanggal Yang di Tuju : "))
bln_tuju = int(input("Masukkan Bulan Yang di Tuju (dalam angka): "))
thn_tuju = int(input("Masukkan Tahun yang di Tuju : "))

jarak_hari  =  tgl_ini - tgl_tuju
jarak_bulan = (bln_ini - bln_tuju )*30
jarak_tahun = (thn_ini - thn_tuju)*360

hasil = jarak_hari+jarak_bulan+jarak_tahun
os.system('cls')
if hasil > 0 :
    print(f"=====Jarak Hari=====")
    print(f"dari Tanggal \t: {tgl_ini}-{bln_ini}-{thn_ini}")
    print(f"Ke Tanggal \t: {tgl_tuju}-{bln_tuju}-{thn_tuju}")
    print(f"Adalah  {hasil} hari yang lalu")

elif hasil < 0 :
    print(f"=====Jarak Hari=====")
    print(f"dari Tanggal \t: {tgl_ini}-{bln_ini}-{thn_ini}")
    print(f"Ke Tanggal \t: {tgl_tuju}-{bln_tuju}-{thn_tuju}")
    print(f"Adalah {hasil*-1} hari ke depan")
else:
    print("Ya Hari INI, Masa Ga Tau")



