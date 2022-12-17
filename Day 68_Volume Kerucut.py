import os
def vol_kerucut ():
    r = float(input("Masukkan Jari-jari Kerucut : "))
    if r % 2 ==0 or r % 2 == 1:
        r = int(r)
    t = float(input("Masukkan Tinggi Kerucut : "))
    if t % 2 == 0 or t % 2 == 1 :
        t = int(t)
    if r % 7 == 0 :
        phi = 22/7
    else:
        phi = 3.14
    v = (1/3)*(r**2)*t
    if v % 2 == 1 or v % 2 == 0:
        v = int(v)
    print (40*"=")
    print(f"Jari-jari Kerucut \t= {r} cm")
    print(f"Tinggi Kerucut \t\t= {t} cm ")
    print(f"Volume Kerucut \t\t= {v} cm")
    print (40*"=")
os.system('cls')
vol_kerucut()