import os
harga = 150000
jumlah = int(input("Masukkan jumlah Barang : "))
if jumlah > 5 :
    diskon = harga*jumlah*0.2
    total = (harga*jumlah) - diskon
    os.system('cls')
    print("Harga Barang/unit : Rp.150000")
    print(f"Jumlah Barang \t  : {jumlah} unit")
    print("=====Kamu Mendapat Discont 20%======")
    print(f"Total Harga \t  : Rp.{int(total)}")
elif jumlah >0 and jumlah<=5:
    total = (harga*jumlah) 
    print("Harga Barang/unit : Rp.150000")
    print(f"Jumlah Barang \t  : {jumlah} unit")
    print(f"Total Harga \t  : Rp.{int(total)}")
else:
    print("Jumlah Yang Anda Masukkan Tidak Valid")