panjang = int(input("Masukkan Tinggi Segitiga: "))
panjang //= 2

bintang = 1
while bintang <= panjang :
    print(" "*(panjang-bintang+1),"* "*bintang)
    bintang += 1
while bintang >= 0 :
    print(" "*(panjang-bintang+1),"* "*bintang)
    bintang-=1