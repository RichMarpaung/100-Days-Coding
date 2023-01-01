syarat = True
while syarat == True:
    angka = int(input("Masukkan Angka : "))
    if angka % 3 == 0:
        if angka % 5 == 0:
            print("Master Class")
        else:
            print("Pride Of 3")
    elif angka % 5 == 0:
        if angka%3==0:
            print("Master Class")
        else:
            print("Pride Of 5")