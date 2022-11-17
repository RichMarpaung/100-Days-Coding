import os
pilihan="y"
while pilihan=="y" or pilihan =="Y":
    os.system('cls')
    print("""
    ==============================
            Marpaung Coffe
        List Menu Minuman Kopi 
    ==============================
    A. ES Kopi Susu   : Rp 11.000
    B. ES Kopi Coklat : Rp 12.000
    C. ES Kopi Hitam  : Rp 11.000
    D. Ice Americano  : Rp 14.000
    ==============================
    """)
    pesan=str(input("Masukkan list abjad menu kopi \t: "))
    jumlahpesan = 0
    if pesan == "a" or pesan =="A":
        jumlahpesan=int(input("Masukkan jumlah pesanan \t: "))
        listnama= "ES Kopi Susu"
        harga=(11000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5: 
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "b" or pesan == "B":
        jumlahpesan=int(input("Masukkan jumlah pesanan \t: "))
        listnama= "ES Kopi Coklat"
        harga = (12000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "c" or pesan== "C":
        jumlahpesan=int(input("Masukkan jumlah pesanan \t: "))
        listnama= "ES Kopi Hitam"
        harga=int(11000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga=int(harga+ppn)
    elif pesan == "d" or pesan == "D":
        jumlahpesan=int(input("Masukkan jumlah pesanan \t: "))
        listnama= "ES Americano"
        harga=int(14000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
        
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("Menu tidak tersedia, silahkan masukkan abjad menu yang tersedia Y/N : ")
    os.system('cls')
    print("\n--------------------------")
    print("      Marpaung Coffe")
    print("--------------------------")
    print(f"Menu \t\t: {listnama}")
    print(f"Jumlah Pesan \t: {jumlahpesan} pcs")
    print(f"Harga \t\t: Rp.{harga}")
    print(f"Diskon \t\t: Rp.{diskon}")
    print(f"PPN \t\t: Rp.{ppn}")
    print("--------------------------")
    print(f"Jumlah Bayar \t: Rp.{totalharga}")
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N : ")