a = int(input("Masuukkan angka!!! : "))
for i in range (a):
    for spasi in range (a-i-1):
        print(' ',end = ' ')
    for bintang in range (2*i+1):
        print('*',end=' ')
    print()
    
for i in range (a-1,0,-1):
    for spasi in range (a-i):
        print(' ',end = ' ')
    for bintang in range (2*i-1):
        print('*',end=' ')
    print()

