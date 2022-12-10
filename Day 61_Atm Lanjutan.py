import os 
import random
import time
data_user = [
    {
    "id" : "2305",
    "nama" : "Owner",
    "no_rek" : "23052002",
    "pin" : "130922",
    "saldo" : 99000000
    },
    {
    "id" : "2305",
    "nama" : "Owner2",
    "no_rek" : "12345678",
    "pin" : "232312",
    "saldo" : 99000000
    }
    ]
def acak_norek():
    ada = "ada"
    while ada == "ada":
        no_rek_baru = random.randint(10000000,99999999)
        for i in range(len(data_user)):
            if data_user[i]["no_rek"] != no_rek_baru :
                ada == "tidak"
                return str(no_rek_baru)
            else :
                ada == "ada"
def acak_id():
    ada = "ada"
    while ada == "ada":
        id_user_baru = random.randint(1000,9999)
        for i in range(len(data_user)):
            if data_user[i]["id"] != id_user_baru :
                ada == "tidak"
                return str(id_user_baru)
            else :
                ada == "ada"
def cek_pin_baru(pin_baru):
    for user in data_user:
        if user['pin'] == pin_baru:
            return 'ada'
    return pin_baru

def daftar ():
    yakin = 'n'
    while yakin == "n":
        os.system('cls')
        print(60*"=")
        print("\t\t   Menu Buka Rekening Baru".upper())
        print(60*"=")
        print("")
        nama_baru = input("    Masukkan Nama Anda \t\t: ")
        print("")
        pin_baru = input("    Masukkan Pin Baru (min 6) \t: ")
        print("")
        autenti_pin_baru = input("    Masukkan Kembali Pin \t: ")
        print("")
        no_rek_baru = acak_norek()
        id_user_baru = acak_id()
        periksa_pin_baru = cek_pin_baru(pin_baru)
        print(60*"=")
        tanya = input("Apakah Data Sudah Benar Y/N : ")
        
        if tanya == 'y' or tanya == "Y":
            os.system('cls')
            if len(pin_baru) < 6 :
                os.system('cls')
                print(60*"=")
                print("\t\t   Menu Buka Rekening Baru".upper())
                print(60*"=")
                print("")
                print("")
                print("   Pin Yang Anda Masukkan TIdak Valid Mohon Coba Lagi!!".upper())
                print("")
                print("")
                print(60*"=")
                time.sleep(5)
                yakin = 'n'
            elif pin_baru != autenti_pin_baru:
                print(60*"=")
                print("\t\t   Menu Buka Rekening Baru".upper())
                print(60*"=")
                print("")
                print("")
                print("         Mohon Periksa Kembali Autentifikasi Pin Anda!!".upper())
                print("")
                print("")
                print(60*"=")
                time.sleep(5)
                yakin = 'n'
            elif periksa_pin_baru == 'ada':
                os.system('cls')
                print(60*"=")
                print("\t\t   Menu Buka Rekening Baru".upper())
                print(60*"=")
                print("")
                print("")
                print("    Pin Yang Anda Masukkan Sudah Digunakan Mohon Coba Lagi!!".upper())
                print("")
                print("")
                print(60*"=")
                time.sleep(5)
                yakin = 'n'

            else :
                tambah = dict(id = id_user_baru,nama = nama_baru,no_rek = no_rek_baru,pin = pin_baru,saldo = 0)
                data_user.append(tambah)
                print(60*'=')
                print("\t\t   Menu Buka Rekening Baru".upper())
                print(60*'=')
                print("")
                print(14*" ","SELAMAT PEMBUATAN AKUN BERHASIL")
                print("")
                print(22*" ","SILAHKAN LOGIN")
                print("")
                print(60*'=')
                time.sleep(5)
                yakin = 'y'
                atm_nyala = 'y'
        else:
            yakin = 'n'
def cek_login(p):
    for user in data_user:
        if user['pin'] == p:
            return user
    return False
def cek_id (id):
    for i in range (len(data_user)):
        if str(data_user[i]['id']) == str(id):
            return int(i)
    return -1
def cek_norek(nomor_rek):
    for i in range(len(data_user)):
        if str(data_user[i]['no_rek']) == str(nomor_rek):
            return int(i)
    return -1
def tarik_uang (uang):
    pengguna = cek_id(user_id)
    if pengguna >=0:
        if data_user[pengguna]['saldo'] >= int(uang):
            data_user[pengguna]['saldo'] = data_user[pengguna]['saldo'] - int(uang)
            print('')
            print(60*"=")
            print('')
            print("\t\t      Transaksi Berhasil".upper())
            print('')
            print(60*"=")
        else:
            print('')
            print(60*"=")
            print('')
            print("\t\t   Saldo Anda Tidak Mencukupi")
            print('')
            print(f"\t\tSaldo Anda Saat ini Rp. {data_user[pengguna]['saldo']}")
            print('')
            print(60*"=")
           

def setor_uang(uang):
    pengguna = cek_id(user_id)
    if pengguna >= 0 :
        data_user[pengguna]['saldo'] = data_user[pengguna]['saldo'] + int(uang)
        print('')
        print(60*"=")
        print('')
        print("\t\t      Transaksi Berhasil".upper())
        print('')
        print(60*"=")
        

def transfer (uang,norek_tujuan):
    pengguna = cek_id(user_id)
    penerima = cek_norek(norek_tujuan)
    if pengguna >= 0:
        if data_user[pengguna]['saldo'] > int(uang):
            data_user[pengguna]['saldo'] = data_user[pengguna]['saldo'] - int(uang)
            data_user[penerima]['saldo'] = data_user[penerima]['saldo'] + int(uang)
            print('')
            print(60*"=")
            print("\t\t      Transaksi Berhasil".upper())
            print('')
            print(f"  Anda Berhasil mentransfer Rp.{str(uang)} ke Rekening {norek_tujuan}".upper())
            print('')
            print(60*"=")
           
        else:
            print('')
            print(60*"=")
            print('')
            print("\t\t   Saldo Anda Tidak Mencukupi")
            print('')
            print(f"\t\tSaldo Anda Saat ini Rp. {data_user[pengguna]['saldo']}")
            print('')
            print(60*"=")



status_login = False
user_id = 0
ulang_tansaksi = 'n'

atm_nyala = 'y'
while atm_nyala == "y":
    os.system('cls')
    print(60*'=')
    print(13*" ","SELAMAT DATANG DI ATM BANK WONG CILIK")
    print(60*'=')
    print("\n\t\t1. Sudah Punya Akun (Login) \n\n\t\t2. Belum Punya Akun (Daftar)\n ")
    print(60*'=')
    print('')
    ask = input("Pilih Menu : ")
    if ask == '1' :
        status_login = False
    elif ask == '2':
        daftar()
        status_login = True
        atm_nyala = 'y'
    else :
        os.system('cls')

        print(60*'=')
        print("\t\t!!! PILIHAN TIDAK VALID !!!")
        print(60*'=')
        print("")
        print("")
        print("\t\t  CEK KEMBALI PILIHAN ANDA")
        print("")
        print("")
        print(60*'=')
        time.sleep(2)
        status_login = True
        atm_nyala = 'y'

    while status_login == False :
        os.system('cls')
        print(60*'=')
        print(22*" ","BANK WONG CILIK")
        print(60*'=')
        print("\n",20*" ","MASUKKAN PIN ANDA\n")
        pin = input(27*" ")
        periksa = cek_login(pin)
        if periksa: 
            print("\n")
            print(60*'=')
            print(20*" ","SELAMAT DATANG " + periksa['nama'].upper())
            print(60*'=')
            time.sleep(2)
            user_id = periksa['id']
            ulang_tansaksi = 'y'
            status_login = True
        else:
            os.system ('cls')
            print(60*'=')
            print(22*" ","BANK WONG CILIK")
            print(60*'=')
            print('')
            print('')
            print(22*" ","Pin Anda Salah !!!".upper())
            print('')
            print('')
            print(60*'=')
            tanya = input("Ingin Mencoba Login Lagi? y/n ").upper()
            if tanya == 'Y':
                status_login = False
            else:
                status_login = True
                atm_nyala = 'y'
           
    
    while ulang_tansaksi == 'y' or ulang_tansaksi == "Y":
        user_aktif = data_user[cek_id(user_id)]
        os.system('cls')
        print(60*'=')
        print(22*" ","BANK WONG CILIK")
        print(60*'=')
        print("")
        print("1. Tarik Tunai \n2. Setor Tunai \n3. Transfer \n4. Cek Saldo \n5. Info Pengguna \n6. Keluar")
        print("")
        print(60*'=',"\n")
        pilih = input("Masukkan Pilihan Menu : ")
        if pilih == '1':
            os.system('cls')
            print(60*'=')
            print(21*" ","MENU PENARIKAN UANG")
            print(60*'=')
            print("")
            print(20*" ","MASUKKAN NOMINAL UANG")
            print("")
            print(19*" ","DENGAN KELIPATAN RIBUAN")
            print("")
            uang =input("\t\t\t Rp. ")
            if int(uang) % 1000 == 0 :
                tarik_uang(uang)
                print('')
                ulang_tansaksi = input("Apakah Anda Ingin Melakukan Transaksi Lain (Y/N) : ")
            else:
                print(60*'=')
                print('')
                print("\t\tNOMINAL TIDAK VALID COBA LAGI!!!")
                print('')
                print(60*'=')
                time.sleep(2)
        elif pilih == '2':
            os.system('cls')
            print(60*'=')
            print(23*" ","MENU SETOR TUNAI")
            print(60*'=')
            print("")
            print(20*" ","MASUKKAN NOMINAL UANG")
            print("")
            print(19*" ","DENGAN KELIPATAN RIBUAN")
            print("")
            uang =input("\t\t\t Rp. ")
            if int(uang) % 1000 == 0 and uang != 0 :
                setor_uang(uang)
                print('')
                ulang_tansaksi = input("Apakah Anda Ingin Melakukan Transaksi Lain (Y/N) : ")
            else:
                print(60*'=')
                print('')
                print("\t\tNOMINAL TIDAK VALID COBA LAGI!!!")
                print('')
                print(60*'=')
                time.sleep(2)
                os.system('cls')
        elif pilih == '3':
            os.system('cls')
            print(60*'=')
            print(22*" ","MENU TRANSFER UANG")
            print(60*'=')
            print("")
            
            print(19*" ","MASUKKAN REKENING TUJUAN")
            print("")
            rek_tujuan = input("\t\t\t   ")
            cek_tujuan = cek_norek(rek_tujuan)
            if cek_tujuan >= 0:
                os.system('cls')
                print(60*'=')
                print(22*" ","MENU TRANSFER UANG")
                print(60*'=')
                print("")
                print(20*" ","MASUKKAN NOMINAL UANG")
                print("")
                print(19*" ","DENGAN KELIPATAN RIBUAN")
                print("")
                uang =input("\t\t\t Rp. ")
                if int(uang) % 1000 == 0 and uang != 0 :
                    transfer(uang,rek_tujuan)
                    print('')
                    ulang_tansaksi = input("Apakah Anda Ingin Melakukan Transaksi Lain (Y/N) : ")
                else:
                    print(60*'=')
                    print('')
                    print("\t\tNOMINAL TIDAK VALID COBA LAGI!!!")
                    print('')
                    print(60*'=')
                    time.sleep(2)
                    os.system('cls')
            else:
                print(60*'=')
                print('')
                print("\t\tNOMOR REKENING TIDAK DI TEMUKAN")
                print('')
                print(60*'=')
                time.sleep(2)
                os.system('cls')
        elif pilih == '4':
            os.system('cls')
            print(60*'=')
            print(22*" ","BANK WONG CILIK")
            print(60*'=')
            print("")
            print("")
            print(20*" ","Saldo Anda saat ini".upper())
            print("")
            print(f"\t\t\tRp. {user_aktif['saldo']}")
            print("")
            print("")
            print(60*'=')
            print("")
            ulang_tansaksi = input("Apakah Anda Ingin Melakukan Transaksi Lain (Y/N) : ")
        elif pilih == '5':
            os.system('cls')
            print(60*'=')
            print(22*" ","BANK WONG CILIK")
            print(60*'=')
            print("")
            print(f"\t\tID \t\t: {user_aktif['id']}")
            print("")
            print(f"\t\tNAMA \t\t: {user_aktif['nama']}")
            print("")
            print(f"\t\tNomor Rekening \t: {user_aktif['no_rek']}")
            print("")
            print(60*'=')
            ulang_tansaksi = input("Apakah Anda Ingin Melakukan Transaksi Lain (Y/N) : ")
        elif pilih == '6':
            ulang_tansaksi = 'n'
            status_login = False
        else :
            os.system('cls')
            print(60*'=')
            print(22*" ","BANK WONG CILIK")
            print(60*'=')
            print("\n\n\t    PILIHAN Anda TIDAK VALID YA GAYS YAK !!!")
            time.sleep(2)

                
            


