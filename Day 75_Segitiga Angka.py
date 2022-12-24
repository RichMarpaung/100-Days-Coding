#panjang = int(input("Masukkan Panjang Segitiga : "))
panjang = int(input("Masukkan Panjang Segitiga : "))
k = 0
angka = 0
angka_akhir = 0
for i in range (1,panjang+1):
    for spasi in range (1,panjang-i+1):
        print(end= "  ")
        angka +=1
    while k != ((2*i)-1):
        if angka <= panjang-1:
            print(i+k, end= " ")
            angka +=1
        else:
            angka_akhir+=1
            print((i+k)-(2*angka_akhir),end=" ")
        k+=1
    angka = angka_akhir = k = 0

    print()
        
k=0
angka = 0
angka1 =0
for i in range (1,panjang+1):
    #print(i)
    for space in range(1,(panjang-i)+1):
        print(end='  ')
        angka +=1
    while k != ((2*i)-1):
        if angka<=panjang-1:
            print(i+k,end=' ')
            angka+=1
        else:
            angka1 +=1
            print (i+k-(2*angka1),end=' ')
        k+=1
    angka=angka1=k=0
    print()
        
