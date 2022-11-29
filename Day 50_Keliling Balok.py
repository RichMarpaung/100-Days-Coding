import os
def keliling_balok ():
    os.system('cls')
    panjang = float(input("Masukkan Panjang Balok \t: "))
    if panjang % 2 == 1 or panjang % 2 == 0 :
        panjang = int(panjang)
    lebar = float(input("Masukkan Lebar Balok \t: "))
    if lebar % 2 == 1 or lebar % 2 == 0 :
        lebar = int(lebar)
    tinggi = float(input("Masukkan Tinggi Balok \t: "))
    if tinggi % 2 == 1 or tinggi % 2 == 0 :
        tinggi = int(tinggi)
    kel = 4*(panjang+lebar+tinggi)
    if kel % 2 == 1 or kel % 2 == 0 :
        kel = int(kel)
    else:
        kel = round(kel,2)
    os.system('cls')
    print(40*'=')
    print(f"Panjang Balok \t: {panjang} cm")
    print(f"Lebar Balok \t: {lebar} cm")
    print(f"Tinggi Balok \t: {tinggi} cm")
    print(40*'=')
    print("Rumus Keliling Balok : 4*(Panjang + lebar + tinggi)")
    print(f"Keliling \t: 4*({panjang} + {lebar} + {tinggi})")
    print(f"Keliling Balok\t: {kel} cm")
    print(40*'=')

keliling_balok()