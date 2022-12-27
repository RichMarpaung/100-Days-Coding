data = int(input("p : "))
data_ganjil = []
data_genap = []
for i in range (1,data+1):
    if i%2==0:
        data_genap.append(i)
    if i%2==1:
        data_ganjil.append(i)
print(f"Ganjil : {len(data_ganjil)}")
print(f"genap : {len(data_genap)}")

data_ganjil = 0
data_genap = 0
for i in range (1,data+1):
    if i%2==0:
        data_genap+=1
    if i%2==1:
        data_ganjil+=1
print(f"Ganjil : {data_ganjil}")
print(f"genap : {data_genap}")

data = int(input("Masukkan Data : "))
jumlah = 0
for i in range (data+1):
    jumlah+=i
print(f"total {jumlah}")

luas_tanah = int(input("Masukkan Luas Tanah : "))
harga = 300000
harga_tanah=int(luas_tanah*harga)

if harga_tanah < 50000000:
    pajak = int(harga_tanah*(1/100))
    total=int(harga_tanah-pajak)
    print(total)

elif harga_tanah >=50000000 and harga_tanah <= 100000000:
    pajak =int (harga_tanah*(3/100))
    print(harga_tanah-pajak)

elif harga_tanah > 100000000:
    pajak =int(harga_tanah*(5/100))
    print(harga_tanah-pajak)
