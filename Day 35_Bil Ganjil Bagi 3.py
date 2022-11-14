print(10*'=',"Menggunakan For",10*'=')
n = int(input("Masukkan Panjang Data : "))
data = []
for i in range(1,n+1,2):
    if i % 3 == 0:
        data.append(i)
print(f"Data : {data}")
print(f"Hasil Jumlah Semua data : {sum(data)}")

print('')
print(10*'=',"Menggunakan While",10*'=')
n = int(input("Masukkan Panjang Data : "))
i = 1
data = []
while i<=n:
    if i % 2 == 1:
        if i % 3 == 0:
            data.append(i)
            i += 1
    i += 1
print (f"data{data}")
print(f"Hasil JUmlah semua Data : {sum(data)}")