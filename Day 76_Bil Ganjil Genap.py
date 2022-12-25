data_ganjil = []
data_genap = []
panjang = int(input("Masukkan Panjang Data : "))
for i in range (panjang+1):
    if i == 0 :
        continue
    if i %2 == 0:
        data_genap.append(i)
    if i %2 == 1:
        data_ganjil.append(i)
print("Bilangan Ganjil : ",data_ganjil)
print("Bilangan Genap : ",data_genap)
