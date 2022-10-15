print(10*"=","Conversi Celcius",10*"=")
c = float(input("Masukkan Besar Suhu : "))
print(10*"=","Hasil Konversi",10*"=")
print(f"Suhu Awal = {c}°C")
f = 9/5*c+32
r = 4/5*c
k = c+273
print(f"Fahrenheit = {f}°F")
print(f"Reaumur = {r}°R")
print(f"Kelvin = {k}°K")

print("\n",10*"=","Conversi Fahrenheit",10*"=")
f = int(input("Masukkan Besar Suhu : "))
print(10*"=","Hasil Konversi",10*"=")
print(f"Suhu Awal = {f}°F")
c = round(5/9*(f-32),2)
r = round(4/9*(f-32),2)
k = round((f-32)*5/9+273,2)
print(f"Celcius = {c}°C")
print(f"Reaumur = {r}°R")
print(f"Kelvin = {k}°K")

print("\n",10*"=","Conversi Reamur",10*"=")
r = int(input("Masukkan Besar Suhu : "))
print(10*"=","Hasil Konversi",10*"=")
print(f"Suhu Awal = {r}°R")
c = 5/4*r
f = (9/4*r)+32
k = 5/4*r+273
print(f"Celcius = {c}°C")
print(f"Fahrenheit = {f}°F")
print(f"Kelvin = {k}°K")

print("\n",10*"=","Conversi Kelvin",10*"=")
k = int(input("Masukkan Besar Suhu : "))
print(10*"=","Hasil Konversi",10*"=")
print(f"Suhu Awal = {k}°K")
c = k-273
f = 9/5*(k-273)+32
r = 4/5*(k-273)
print(f"Celcius = {c}°C")
print(f"Fahrenheit = {f}°F")
print(f"Reaumur = {r}°R")