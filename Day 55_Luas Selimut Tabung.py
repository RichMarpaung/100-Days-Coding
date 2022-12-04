import os
def luas_selimut ():
    r = float(input("Masukkan Jari-Jari (cm) : "))
    if r % 2 == 1 or r %2==0:
        r = int(r)
    t = float(input("Masukkan Tinggi (cm) \t: "))
    if t % 2 == 1 or t %2==0:
        t = int(t)
    if r %7 == 0 :
        Ls = 2 * (22/7) * r * t
    else :
        Ls = 2 * 3.14 * r * t
    if Ls % 2 == 1 or Ls %2==0:
        Ls = int(Ls)
    else :
        Ls = round(Ls,2)
    os.system('cls')
    print (40*"=")
    print(f"Jari-jari Tabung \t: {r} cm")
    print(f"Tinggi Tabung \t\t: {t} cm")
    print(f"Luas Selimut Tabung \t: {Ls} cm²")
    print (40*"=")

luas_selimut()