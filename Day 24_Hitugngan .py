import os
os.system("cls")
print ("="*10,"OPERATOR SEDERHANA",10*"=")
while True :
    
    x = int(input("""      Pilih Operator
    1. Penjumlahan (+)
    2. Pengurangan (-)
    3. Perkalian   (*)
    4. Pembagian   (/)
    5. Pembagian(dibulatkan kebawah) (//)
    6. Sisa Bagi / Modulo  (%)
    7. Perpangkatan (**)

    Pilih Operator : """))
    os.system("cls")
    a = int(input("Masukkan Angka : "))
    b = int(input("Masukkan Angka : "))
    if x == 1:
        hasil = a+b
        print("")
        print ("="*10,"OPERATOR Penjumlahan",10*"=")
        print(f"Hasil Operasi = {a} + {b} = {hasil}\n")
        print("="*30)
    elif x==2:
        hasil= a-b
        print("")
        print ("="*10,"OPERATOR Pengurangan",10*"=")
        print(f"Hasil Operasi = {a} - {b} = {hasil}\n")
        print("="*30)
    elif x==3:
        hasil= a*b
        print("")
        print ("="*10,"OPERATOR Perkalian",10*"=")
        print(f"Hasil Operasi = {a} * {b} = {hasil}\n")
        print("="*30)
    elif x==4:
        hasil= a/b
        print("")
        print ("="*10,"OPERATOR Pembagian",10*"=")
        print(f"Hasil Operasi = {a} / {b} = {hasil}\n")
        print("="*30)
    elif x==5:
        hasil= a//b
        print("")
        rint ("="*5,"OPERATOR Pembagian(Dibulatkan Kebawah)",5*"=")
        print(f"Hasil Operasi = {a} * {b} = {hasil}\n")
        print("="*30)
    elif x==6:
        hasil= a%b
        print("")
        print ("="*10,"OPERATOR Modulo",10*"=")
        print(f"Hasil Operasi = {a} * {b} = {hasil}\n")
        print("="*30)
    elif x==7:
        hasil= a**b
        print("")
        print ("="*10,"OPERATOR Perpangkaran",10*"=")
        print(f"Hasil Operasi = {a} ** {b} = {hasil}\n")
        print("="*30)
    else :
        print("Pilihan Tidak Tersedia")
        print("="*30)
        

