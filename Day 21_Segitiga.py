panjang = int(input("Masukkan Panjang Segitiga bilangan ganjil : "))
panjang = panjang//2+1

k=0
for i in range (1,panjang+1):
    #print(i)
    for space in range(1,(panjang-i)+1):
        print(end='  ')
    
    while k != (2*i-1):
        print('*', end=' ')
        k+=1
    k=0
    print()
for i in range(panjang-1,0,-1):
    for space in range((panjang-i),0,-1):
        print(end='  ')
    while k != (2*i-1):
        print('*', end=' ')
        k+=1
    k=0
    print()



print('\n')
#panjang = int(input("Masukkan Panjang Segitiga : "))
panjang = int(input("Masukkan Panjang Segitiga : "))
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