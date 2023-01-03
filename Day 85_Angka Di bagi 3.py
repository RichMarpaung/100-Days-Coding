angka = int(input("Masukkan Angka : "))
jumlah = 0
for i in range(1,angka+1):
    if i % 3 == 0 :
        jumlah+=1
print(f"Jumlah Angka Yang bisa di bagi 3 dari 1-{angka} adalah {jumlah}")