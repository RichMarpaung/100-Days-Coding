import os
def luas_alas ():
    r = float(input("Masukkan Jari-Jari Kerucut (cm)     : "))
    if r % 2 == 1 or r % 2 == 0:
        r = int(r)
    if r % 7 == 0 :
        phi = 22/7
    else :
        phi = 3.14
    L = phi * (r**2)
    if L % 2 == 1 or L % 2 == 0:
        L = int(L) 
    print (40*"=")
    print(f"Jari-jari Kerucut \t= {r} cm")
    print(f"Luas Alas Kerucut \t= {L} cm²")
    print (40*"=")
os.system('cls')
luas_alas()