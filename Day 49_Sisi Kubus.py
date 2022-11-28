import os
def sisi_luas (luas) : 
    sisi = luas**(1/2) / 6 
    if sisi % 2 ==1 or sisi % 2 ==0:
        return int(sisi)
    else :
        return sisi
def sisi_vol (volume):
    sisi = volume**(1/3)
    if sisi % 2 ==1 or sisi % 2 ==0:
        return int(sisi)
    else : 
        return sisi

print("Diketahui : \n1. Luas \n2.Volume")
dik = input("Apa yang di Ketahui (1-2) : ")
os.system('cls') 
if dik == '1':
    luas = float(input("Masukkan Luas Kubus : "))
    if luas % 2 ==1 or luas % 2 ==0:
        luas =  int(luas)
    os.system('cls')
    print(40*"=")
    print(f"Luas Kubus : {luas} cm²")
    print(f"Panjang Sisi Kubus : {round(sisi_luas(luas),2)} cm")
    print(40*"=")
    
elif dik == '2':
    vol = float(input("Masukkan Volume Kubus : "))
    if vol % 2 ==1 or vol % 2 ==0:
        vol = int(vol)
    os.system('cls')
    print(40*"=")
    print(f"Volume Kubus : {vol} cm³")
    print(f"Panjang Sisi Kubus : {round(sisi_vol(vol),2)} cm")
    print(40*"=")
 
else:
    print("Pilihan Tidak Valid")