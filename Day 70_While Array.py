data = int(input("Masukkan Panjang Data : "))
i = 0
data_list = []
while i <= data:
    data_list.append(i)
    i+=1
print(f"\nData = {data_list}")
i = 0
data_ganjil = []
while i <= data :
    if i % 2 == 1:
        data_ganjil.append(i)
    i+=1
print(f"\nAngka Ganjil Data = {data_ganjil} ")
data_genap = []
i = 0

while i <= data :
    i+=1
    if i % 2 == 0:
        data_genap.append(i)
print(f"\nAngka Ganjil Data = {data_genap} ")

 