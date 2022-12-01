import os
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
    print(40*'=')
    print("Rumus Volume Balok : panjang * lebar * tinggi")
    print(f"LUas \t\t : {panjang} * {lebar} * {tinggi}")
    print(f"Volume Balok \t: {volume} cm³")
    print(40*'=')
volume_balok()