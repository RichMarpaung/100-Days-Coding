import os
def luas_alas():
    r = float(input("Masukkan Jari-Jari (cm) : "))
    if r % 2 == 1 or r %2==0:
        r = int(r)
    if r %7 == 0 :
        L_alas = (22/7)*r*r
    else :
        L_alas = 3.14*r*r
    if L_alas % 2 == 1 or L_alas %2==0:
        L_alas = int(L_alas)
    else :
        L_alas = round(L_alas,2)
    os.system('cls')
    print (40*"=")
    print(f"Jari-jari Tabung \t: {r} cm")
    print(f"Luas Alas Tabung \t: {L_alas} cm²")
    print (40*"=")
luas_alas()