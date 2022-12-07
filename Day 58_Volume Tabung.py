import os
def volume ():
    r = float(input("Masukkan Jari-Jari (cm) : "))
    if r % 2 == 1 or r %2==0:
        r = int(r)
    t = float(input("Masukkan Tinggi (cm) \t: "))
    if t % 2 == 1 or t %2==0:
        t = int(t)
    if r %7 == 0 :
        vol = (22/7)*r*r*t
    else :
        vol = 3.14*r*r*t
    if vol % 2 == 1 or vol %2==0:
        vol = int(vol)
    else :
        vol = round(vol,2)
    os.system('cls')
    print (40*"=")
    print(f"Jari-jari Tabung \t: {r} cm")
    print(f"Tinggi Tabung \t\t: {t} cm")
    print(f"Volume Tabung \t\t: {vol} cm³") 
volume()