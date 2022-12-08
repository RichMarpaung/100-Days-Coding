import os
def jari_tabung():
    print('='*11,"Yang Ingin Di cari",11*'=')
    print("1. Jari-Jari Tabung \n2. Tinggi Tabung")
    print(40*'=')
    tanya = input("Pilih Yang ingin di Cari : ")
    if tanya == '1':
        os.system('cls')
        print('='*11,"Yang Diketahui",11*'=')
        print("1. Luas Selimut Tabung\n2. Volume Tabung")
        print(40*'=')
        dik = input("Pilih Yang Diketahui : ")
        if dik == '1':
            os.system('cls')
            luas_selimut = float(input("Masukkan Luas Selimut Tabung : "))
            if luas_selimut % 2 == 0 or luas_selimut %2 ==1:
                luas_selimut = int(luas_selimut)
            t = float(input("Masukkan Tinggi Tabung : "))
            if t % 2 == 0 or t %2 ==1:
                t = int(t)
            r = luas_selimut/(2*3.14*t)
            if r % 2 == 0 or r %2 ==1:
                r = int(r)
            else :
                r = round(r,1)
            os.system('cls')
            print (40*"=")
            print(f"Luas Selimut Tabung \t: {luas_selimut} cm²")
            print(f"Tinggi Tabung \t\t: {t} cm")
            print(f"Jari-jari Tabung \t: {r} cm")
            print (40*"=")
        elif dik == '2':
            os.system('cls')
            v = float(input("Masukkan Volume Tabung : "))
            if v % 2 == 0 or v %2 ==1:
                v = int(v)
            t = float(input("Masukkan Tinggi Tabung : "))
            if t % 2 == 0 or t %2 ==1:
                t = int(t)
            r =(v/(3.14*t))**(1/2)
            if r % 2 == 0 or r %2 ==1:
                r = int(r)
            else :
                r = round(r,1)
            os.system('cls')
            print (40*"=")
            print(f"Volume Tabung \t\t: {v} cm³")
            print(f"Tinggi Tabung \t\t: {t} cm")
            print(f"Jari-jari Tabung \t: {r} cm")
            print (40*"=")
        else :
            print("Pilihan Tidak VALID!!!")
    elif tanya == '2':
        os.system('cls')
        print('='*11,"Yang Diketahui",11*'=')
        print("1. Luas Selimut Tabung\n2. Luas Permukaan \n3. Volume Tabung")
        print(40*'=')
        dik = input("Pilih Yang Diketahui : ")
        if dik == '1':
            os.system('cls')
            luas_selimut = float(input("Masukkan Luas Selimut Tabung : "))
            if luas_selimut % 2 == 0 or luas_selimut %2 ==1:
                luas_selimut = int(luas_selimut)
            r = float(input("Masukkan Jari-jari Tabung : "))
            if r % 2 == 0 or r %2 ==1:
                r = int(r)
            if r % 7 == 0:
                t = luas_selimut/(2*(22/7)*r)
            else :
                t = luas_selimut/(2*(3.14)*r)

            if t % 2 == 0 or t %2 ==1:
                t = int(t)
            else :
                t = round(t,1)
            os.system('cls')
            print (40*"=")
            print(f"Luas Selimut Tabung \t: {luas_selimut} cm²")
            print(f"Jari-jari Tabung \t: {r} cm")
            print(f"Tinggi Tabung \t\t: {t} cm")
            print (40*"=")
        elif dik == '2':
            os.system('cls')
            luas_permukaan = float(input("Masukkan Luas Permukaan Tabung : "))
            if luas_permukaan % 2 == 0 or luas_permukaan %2 ==1:
                luas_permukaan = int(luas_permukaan)
            r = float(input("Masukkan Jari-jari Tabung : "))
            if r % 2 == 0 or r %2 ==1:
                r = int(r)
            if r % 7 == 0:
                t = (luas_permukaan/(2*(22/7)*r))-r
            else :
                t = (luas_permukaan/(2*3.14*r))-r

            if t % 2 == 0 or t %2 ==1:
                t = int(t)
            else :
                t = round(t,1)
            os.system('cls')
            print (40*"=")
            print(f"Luas Selimut Tabung \t: {luas_permukaan} cm²")
            print(f"Jari-jari Tabung \t: {r} cm")
            print(f"Tinggi Tabung \t\t: {t} cm")
            print (40*"=")
        elif dik == '3':
            os.system('cls')
            volume_tabung = float(input("Masukkan Volume Tabung : "))
            if volume_tabung % 2 == 0 or volume_tabung %2 ==1:
                volume_tabung = int(volume_tabung)
            r = float(input("Masukkan Jari-jari Tabung : "))
            if r % 2 == 0 or r %2 ==1:
                r = int(r)
            if r % 7 == 0:
                t = volume_tabung/((22/7)*r**2)
            else :
                t = volume_tabung/((3.14)*r**2)

            if t % 2 == 0 or t %2 ==1:
                t = int(t)
            else :
                t = round(t,1)
            os.system('cls')
            print (40*"=")
            print(f"Luas Selimut Tabung \t: {volume_tabung} cm³")
            print(f"Jari-jari Tabung \t: {r} cm")
            print(f"Tinggi Tabung \t\t: {t} cm")
            print (40*"=")
jari_tabung()