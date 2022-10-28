while True:
    print("="*40)
    print("Komfersi Panjang Centimeter, Meter, Kilometer")
    print("="*40)
    print("""Pilih Satuan Panjang Awal
    1. Cetimeter
    2. Meter
    3. Kilometer""")
    pilih = input("Masukkan Pilihan : ")
    if pilih == "1":
        ukuran = int(input("\nMasukkan Ukuran Centimeter :"))
        m = ukuran/100
        k = ukuran/100000
        print(f"{ukuran} cm = {m} m \n{ukuran} cm = {k}km\n")
    elif pilih == "2":
        ukuran = int(input("\nMasukkan Ukuran Meter :"))
        cm = ukuran*100
        k = ukuran/1000
        print(f"{ukuran} m = {cm} cm \n{ukuran} m = {k}km\n")
    elif pilih == "3":
        ukuran = int(input("\nMasukkan Ukuran Kilometer :"))
        cm = ukuran*100000
        m = ukuran*1000
        print(f"{ukuran} km = {cm} cm \n{ukuran} cm = {m}m\n")
    else:
        print("Pilihan Tidak Tersedia\n")