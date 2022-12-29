luas = int(input("Masukkan Luas Tanah : "))
harga = luas*300000
if harga >= 50000000 and harga<100000000:
    pajak = harga*(3/100)
    print(f"Uang bersih {harga-pajak}")
elif harga > 100000000:
    pajak = harga*(5/100)
    print(f"Uang bersih {harga-pajak}")
else:
    pajak = harga*(1/100)
    print(f"Uang bersih {harga-pajak}")
