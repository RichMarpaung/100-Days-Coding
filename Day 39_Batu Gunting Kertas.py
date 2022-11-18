import random
import os
def keluaran (player,lawan):
    print("\n===============================")
    print(f"Anda Memilih \t: {player}")
    print(f"Lawan Memilih \t: {lawan}")
    print("===============================")

t = ["BATU","GUNTING","KERTAS"]

lawan = t[random.randint(0,2)] # Mengacak Pilihan Lawan

player = False

while player== False:
    os.system('cls')
    print("===============================")
    print ("   BATU , GUNTING , KERTAS")
    print("===============================")
    pilihan = input("Masukkan Pilihan Anda : ")
    player = pilihan.upper()
    if player == lawan :
        keluaran(player,lawan)
        print("Seri!!")
    elif player == "BATU":
        if lawan == "KERTAS":
            keluaran(player,lawan)
            print ("Anda Kalah !!!")
            print(f"{lawan} Menutup {player}")
        else:
            keluaran(player,lawan)
            print ("Anda Menang !!!")
            print(f"{lawan} Memukul {player}")
    elif player == "KERTAS":
        if lawan == "GUNTING":
            keluaran(player,lawan)
            print ("Anda Kalah !!!")
            print(f"{lawan} Memotong {player}")
        else:
            keluaran(player,lawan)
            print ("Anda Menang !!!")
            print(f"{lawan} Menutup {player}")
    elif player == "GUNTING":
        if lawan == "BATU":
            keluaran(player,lawan)
            print ("Anda Kalah !!!")
            print(f"{lawan} Memukul {player}")
        else:
            keluaran(player,lawan)
            print ("Anda Menang !!!")
            print(f"{lawan} Memotong {player}")
    else:
        print("\n===============================")
        print("Input Tidak Valid. Perhatikan Penulisan Anda !!")
    lanjut = input("\nMau Main Lagi ? Y/N : ")
    if lanjut == 'Y' or lanjut == 'y':
        player = False
        lawan = t[random.randint(0,2)]    
    else:
        break
