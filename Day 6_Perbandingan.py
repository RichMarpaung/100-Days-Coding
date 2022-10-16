'''Operasi Perbandingan ini akan menghasilkan nilai Bolean True atau False'''

#Lebih Besar dari ">"
a = 5
b = 2
print("~~~~~~ Lebih Besar Dari (>) ~~~~~~")
hasil = a>b
print(f"{a} > {b} = {hasil}")
hasil = b>a
print(f"{b} > {a} = {hasil}")
hasil = a>a
print(f"{a} > {a} = {hasil}")

print("\n~~~~~~ Lebih Kecil Dari (<) ~~~~~~")
hasil = a<b
print(f"{a} < {b} = {hasil}")
hasil = b<a
print(f"{b} < {a} = {hasil}")
hasil = a>a
print(f"{a} < {a} = {hasil}")

print("\n~~~~~~ Lebih Besar Dari Sama Dengan(>=) ~~~~~~")
hasil = a>=b
print(f"{a} >= {b} = {hasil}")
hasil = b>a
print(f"{b} >= {a} = {hasil}")
hasil = a>a
print(f"{a} >= {a} = {hasil}")

print("\n~~~~~~ Lebih Kecil Dari Sama Dengan (<=) ~~~~~~")
hasil = a<=b
print(f"{a} <= {b} = {hasil}")
hasil = b<a
print(f"{b} <= {a} = {hasil}")
hasil = a>a
print(f"{a} <= {a} = {hasil}")

print("\n~~~~~~ Sama Dengan (==) ~~~~~~")
hasil = b==a
print(f"{b} == {a} = {hasil}")
hasil = a>a
print(f"{a} == {a} = {hasil}")

print("\n~~~~~~ Sama Dengan (!=) ~~~~~~")
hasil = b!=a
print(f"{b} != {a} = {hasil}")
hasil = a>a
print(f"{a} != {a} = {hasil}")