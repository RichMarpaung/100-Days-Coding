while True:
    print("="*40)
    print("Komfersi Berat Ton, Kwintal , Kilometer")
    print("="*40)
    print("""Pilih Satuan Berat Awal
    1. Ton
    2. Kwintal
    3. Kilogram""")
    pilih = input("Masukkan Pilihan : ")
    if pilih == "1":
        berat = int(input("\nMasukkan berat Ton :"))
        kwintal = berat*10
        kilo = berat *1000
        print(f"{berat} ton = {kwintal} kwintal\n{berat} ton = {kilo}kg\n")
    elif pilih == "2":
        berat = int(input("\nMasukkan berat Kwintal :"))
        ton =  berat/10
        kilo = berat *100
        print(f"{berat} kwintal = {ton} ton \n{berat} kwintal = {kilo}kg\n")
    elif pilih == "3":
        berat = int(input("\nMasukkan berat Kilometer :"))
        ton = berat/1000
        kwintal = berat/100
        print(f"{berat} Kg = {ton} ton \n{berat} Kg = {kwintal} Kwintal\n")
    else:
        print("Pilihan Tidak Tersedia\n")