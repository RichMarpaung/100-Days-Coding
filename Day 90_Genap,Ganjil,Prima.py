def is_prima (x):
  for i in range(2, x):
    if x % i == 0:
      return False

  return True

def cari_bilangan_prima (awal, akhir):

  for x in range(awal, akhir + 1):
    if is_prima(x):
      list_bilangan_prima.append(x)

  return list_bilangan_prima
def bil_ganjil(awal,akhir):
  for i in range(awal,akhir+1):
    if i %2== 1:
      ganjil.append(i)
def bil_genap(awal,akhir):
  for i in range(awal,akhir+1):
    if i %2== 1:
      genap.append(i)

list_bilangan_prima = []
ganjil = []
genap = []
awal = int(input("Masukkan Awal : "))
akhir = int(input("Masukkan Akhir : "))
cari_bilangan_prima(awal,akhir)
bil_ganjil(awal,akhir)
bil_genap(awal,akhir)
print(f"Bilangan Ganjil :{ganjil}")
print(f"Bilangan Genap :{genap}")
print(f"Bilangan Prima :{list_bilangan_prima}")
