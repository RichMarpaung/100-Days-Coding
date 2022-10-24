import os
os.system('cls')

print(10*"=","Konfersi Suhu",10*"=")
print("""1. Celcius
2. Fahrenheit
3. Reaumur
4. Kelvin """)

x =int(input("Pilih Satuan Suhu Awal : "))
if x == 1:
    print("\nAnda Memilih Satuan Celcius ")
    c = float(input("Masukkan Besar Suhu : "))
    print(10*"=","Hasil Konversi",10*"=")
    print(f"Suhu Awal = {c}°C")
    f = 9/5*c+32
    r = 4/5*c
    k = c+273
    print(f"Fahrenheit = {f}°F")
    print(f"Reaumur = {r}°R")
    print(f"Kelvin = {k}°K")
elif x == 2:
    print("\nAnda Memilih Satuan Fahrenheit ")
    f = float(input("Masukkan Besar Suhu : "))
    print(10*"=","Hasil Konversi",10*"=")
    print(f"Suhu Awal = {f}°F")
    c = round(5/9*(f-32),2)
    r = round(4/9*(f-32),2)
    k = round((f-32)*5/9+273,2)
    print(f"Celcius = {c}°C")
    print(f"Reaumur = {r}°R")
    print(f"Kelvin = {k}°K")
elif x == 3:
    print("\nAnda Memilih Satuan Reaumur ")
    r = float(input("Masukkan Besar Suhu : "))
    print(10*"=","Hasil Konversi",10*"=")
    print(f"Suhu Awal = {r}°R")
    c = 5/4*r
    f = (9/4*r)+32
    k = 5/4*r+273
    print(f"Celcius = {c}°C")
    print(f"Fahrenheit = {f}°F")
    print(f"Kelvin = {k}°K")
elif x == 4:
    print("\nAnda Memilih Satuan Kelvin ")
    k = float(input("Masukkan Besar Suhu : "))
    print(10*"=","Hasil Konversi",10*"=")
    print(f"Suhu Awal = {k}°K")
    c = k-273
    f = 9/5*(k-273)+32
    r = 4/5*(k-273)
    print(f"Celcius = {c}°C")
    print(f"Fahrenheit = {f}°F")
    print(f"Reaumur = {r}°R")
else :
    print("Pilihan Tidak Tersedia")