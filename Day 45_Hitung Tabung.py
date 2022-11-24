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
lanjut = 'y'
while lanjut == 'y'or lanjut == "Y":
    os.system('cls')
    print(11*"=","PERHITUNGAN KUBUS",11*"=")
    print("1. Luas Permukaan Tabung\n2. Luas Selimut Tabung\n3. Luas Alas Tabung\n4. Luas Tabung Tanpa Tutup\n5. Volume Tabung\n6. Jari-Jari / Tinggi Tabung")
    print(40*"=")
    pilih = input("Masukkan Pilihan (1-6) : ")
    if pilih == '1':
        os.system('cls')
        luas_permukaan()
        lanjut = input('Apakah Anda Ingin Mengulang Program Y/N : ')
    if pilih == '2':
        os.system('cls')
        luas_selimut()
        lanjut = input('Apakah Anda Ingin Mengulang Program Y/N : ')
    if pilih == '3':
        os.system('cls')
        luas_alas()
        lanjut = input('Apakah Anda Ingin Mengulang Program Y/N : ')
    if pilih == '4':
        os.system('cls')
        luas_tanpa_tutup()
        lanjut = input('Apakah Anda Ingin Mengulang Program Y/N : ')
    if pilih == '5':
        os.system('cls')
        volume()
        lanjut = input('Apakah Anda Ingin Mengulang Program Y/N : ')
    if pilih == '6':
        os.system('cls')
        jari_tabung()
        lanjut = input('Apakah Anda Ingin Mengulang Program Y/N : ')