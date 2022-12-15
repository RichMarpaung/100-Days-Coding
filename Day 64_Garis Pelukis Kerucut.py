import os
def garis_pelukis ():
    r = float(input("Masukkan Jari-jari Kerucut (cm) : "))
    if r % 2 == 1 or r % 2 == 0:
        r = int(r)
    t = float(input("Masukkan Tinggi Kerucut (cm) \t: "))
    if t % 2 == 1 or t % 2 == 0:
        t = int(t)
    S = (r**2+t**2)**0.5
    if S % 2 == 1 or S % 2 == 0:
        S = int(S)
    print (40*"=")
    print(f"Jari-jari Kerucut \t= {r} cm")
    print(f"Tinggi Kerucut \t\t= {t} cm ")
    print(f"Panjang garis Pelukis\t= {S} cm")
    print (40*"=")
os.system('cls')
garis_pelukis()
