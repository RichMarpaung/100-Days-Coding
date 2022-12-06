import os
def luas_tanpa_tutup():
    La = float(input("Masukkan Luas Alas \t: "))
    if La % 2== 0 or La%2==1:
        La = int(La)
    Ls = float(input("Masukkan Luas Selimut \t: "))
    if Ls % 2== 0 or Ls%2==1:
        Ls = int(Ls)
    Luas_tanpa = La + Ls
    if Luas_tanpa % 2 == 1 or Luas_tanpa %2==0:
        Luas_tanpa = int(Luas_tanpa)
    else :
        Luas_tanpa = round(Luas_tanpa,2)
    os.system('cls')
    print (40*"=")
    print(f"Luas Alas Tabung \t: {La} cm")
    print(f"Luas Selimut Tabung \t: {Ls} cm")
    print(f"Luas Permukaan Tabung Tanpa Tutup : {Luas_tanpa} cm²")
    print (40*"=")
luas_tanpa_tutup()