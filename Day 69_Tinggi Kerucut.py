def tinggi__vol(v,r) :
    if r %2 == 0 or r % 2 ==1:
        r = int(r)
    if v % 2 == 0 or v % 2 == 1 :
        v=int(v)
    if r % 7 == 0:
        phi = 22/7
    else:
        phi = 3.14
    t = (3*v)/(phi*r)
    t = round(t,2)
    if t % 2 == 0 or t % 2== 1:
        return int(t)
    return t
def tinggi_S(s,r):
    t = ((s**2)- (r**2))**(1/2)
    t = round(t,2)
    if t % 2 == 0 or t % 2== 1:
        return int(t)
    return t
import os
os.system('cls')
print("Mencari Tinggi Kerucut")
print("Pilih yang diketahui\n1. Garis Pelukis\n2. Volume")
pilih = input("Masukkan Pilian : ")
if pilih == '1':
    os.system('cls')
    print (40*"=")
    s = float(input("Masukkan Panjang Garis Pelukis : "))
    r = float(input("Masukkan Jari Jari Kerucut : "))
    print(f"Tinggi Kerucut adalah {tinggi_S(s,r)}cm")
    print (40*"=")
elif pilih == '2':
    os.system('cls')
    print (40*"=")
    v = float(input("Masukkan Volume Kerucut : "))
    r = float(input("Masukkan Jari Jari Kerucut : "))
    print(f"Tinggi Kerucut adalah {tinggi__vol(v,r)}cm")
    print (40*"=")
else:
    print("pilihan Tidak Valid")