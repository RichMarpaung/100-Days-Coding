import os
def luas_permukaan ():
    r = float(input("Masukkan Jari-Jari Kerucut (cm)     : "))
    if r % 2 == 1 or r % 2 == 0:
        r = int(r)
    S = float(input("Masukkan Garis Pelukis Kerucut (cm) : "))
    if S % 2 == 1 or S % 2 == 0:
        S = int(S)
    if r % 7 == 0 :
        phi = 22/7
    else :
        phi = 3.14
    L = phi * r *(S+r)
    if L % 2 == 1 or L % 2 == 0:
        L = int(L) 
    print (40*"=")
    print(f"Jari-jari Kerucut \t= {r} cm")
    print(f"Garis Pelukis Kerucut \t= {S} cm ")
    print(f"Luas Permukaan Kerucut \t= {L} cm")
    print (40*"=")
os.system('cls')
luas_permukaan()