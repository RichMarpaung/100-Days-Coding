panjang = int(input("Masukkan Panjang Segitiga : "))

k = 0
while k <= panjang:
    print(" "*(panjang-k),"* "*k)
    k+=1

#Segitiga Ganjil
k = 0
while k<=panjang:
    print(" "*(panjang-k),"*"*(2*k-1))
    k+=1