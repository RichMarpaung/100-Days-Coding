#penarikan
#penyetoran
#sisa saldo
import time
import os


lanjut = "y"
saldo = 500000000
while lanjut == 'y' or lanjut == 'Y':
        os.system('cls')
        print("""
        Selamat Datang Di Bank Saya
        1. Menu Penarikan
        2. Penyetoran
        3. Sisa Saldo
        4. Transfer
        """)
        pilih = input("Masukkan Pilihan Menu : ")
        if pilih == '1':
            os.system('cls')
            print(f"Saldo Anda Saat ini :Rp. {saldo}")
            tarik = int(input("Masukkan Jumlah Uang Yang Di Tarik :" ))
            os.system('cls')
            if tarik > saldo :
                print("Saldo Tidak Mencukupi !!")
                lanjut = input("Mau Melakukan Transaksi lain ? (y/n): ")
            else:
                os.system('cls')
                saldo = saldo - tarik
                print("Tarik Berhasil !!!")
                print (f"Sisa Saldo Anda = {saldo}")
                lanjut = input("Mau Melakukan Transaksi lain ? (y/n): ")
        elif pilih == '2':
            os.system('cls')
            print(f"Saldo Anda Saat ini :Rp. {saldo}")
            setor = int(input("Masukkan Jumlah Uang Yang Di setor : "  ))
            os.system('cls')
            saldo = saldo + setor
            print("Tarik Berhasil !!!")
            print (f"Sisa Saldo Anda = {saldo}")
            lanjut = input("Mau Melakukan Transaksi lain ? (y/n): ")
        
            
        elif pilih == '3':
            os.system('cls')
            print(f"Saldo Anda Saat ini : Rp. {saldo}")
            lanjut = input("Mau Melakukan Transaksi lain ? (y/n): ")
            
        elif pilih == '4':
            os.system('cls')
            print(f"Saldo Anda Saat ini :Rp. {saldo}")
            Tranffer = int(input("Masukkan Jumlah Uang Yang Di Tranffer :" ))
            os.system('cls')
            if Tranffer > saldo :
                print("Saldo Tidak Mencukupi !!")
                lanjut = input("Mau Melakukan Transaksi lain ? (y/n): ")
            else:
                os.system('cls')
                saldo = saldo - Tranffer
                print("Tranffer Berhasil !!!")
                print (f"Sisa Saldo Anda = {saldo}")
                lanjut = input("Mau Melakukan Transaksi lain ? (y/n): ")
        else :
            os.system('cls')
            print("Pilihan Tidak Tersedia!!!")
            time.sleep(3)

                