import os
def luas_permukaan():
    r = float(input("Masukkan Jari-Jari (cm) : "))
    if r % 2 == 1 or r %2==0:
        r = int(r)
    t = float(input("Masukkan Tinggi (cm) \t: "))
    if t % 2 == 1 or t %2==0:
        t = int(t)
    #Penggunaan Phi dalam 22/7 atau 3.14
    if r %7 == 0 :
        L = 2 * ((22/7)*r)*(r+t)
    else :
        L = 2 * (3.14*r)*(r+t)
    if L % 2 == 1 or L %2==0:
        L = int(L)
    else :
        L = round(L,2)
    os.system('cls')
    print (40*"=")
    print(f"Jari-jari Tabung \t: {r} cm")
    print(f"Tinggi Tabung \t\t: {t} cm")
    print(f"Luas Permukaan Tabung \t: {L} cm²")
    print (40*"=")
luas_permukaan()