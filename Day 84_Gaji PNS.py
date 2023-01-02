gaji = int(input("Masukkan Gaji anda : "))
kerja = input("Masukkan Jenis Pekerjaan Anda : ").lower()

if gaji >= 3000000 and gaji < 5000000:
    if kerja == "pns":
        pajak = (10/100)*gaji
        gaji_bersih = gaji - pajak
        print(f"Anda Kena Pajak 10%")
        print(f"Gaji bersih Anda Adalah  Rp.{gaji_bersih}")
    else:
        pajak = (5/100)*gaji
        gaji_bersih = gaji - pajak
        print(f"Anda Kena Pajak 5%")
        print(f"Gaji bersih Anda Adalah  Rp.{gaji_bersih}")
elif gaji >= 5000000:
    if kerja == "pns":
        pajak = (15/100)*gaji
        gaji_bersih = gaji - pajak
        print(f"Anda Kena Pajak 15%")
        print(f"Gaji bersih Anda Adalah  Rp.{gaji_bersih}")
    else:
        pajak = (5/100)*gaji
        gaji_bersih = gaji - pajak
        print(f"Anda Kena Pajak 10%")
        print(f"Gaji bersih Anda Adalah  Rp.{gaji_bersih}")
else:
    print(f"Gaji bersih Anda Adalah  Rp.{gaji}")