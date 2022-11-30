import os
def luas_balok ():
    os.system("cls")
    panjang = float(input("Masukkan Panjang Balok \t: "))
    if panjang % 2 == 1 or panjang % 2 == 0 :
        panjang = int(panjang)
    lebar = float(input("Masukkan Lebar Balok \t: "))
    if lebar % 2 == 1 or lebar % 2 == 0 :
        lebar = int(lebar)
    tinggi = float(input("Masukkan Tinggi Balok \t: "))
    if tinggi % 2 == 1 or tinggi % 2 == 0 :
        tinggi = int(tinggi)
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
    print(40*'=')
    print("Rumus LUas Balok : 2*(p * l) + (l * t) + (p * t)")
    print(f"LUas \t\t : 2*({panjang} * {lebar}) + ({lebar} * {tinggi} + ({panjang} * {tinggi})")
    print(f"LUas Balok\t : {luas} cm²")
    print(40*'=')
luas_balok()