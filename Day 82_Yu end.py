syarat = True
while syarat == True:
    angka = int(input("Masukkan Angka : "))
    if angka % 2==0:
        print("genap")
    elif angka%2==1:
        print("You and i, end")
        syarat =False
    