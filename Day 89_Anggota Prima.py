def is_prima (x):
  for i in range(2, x):
    if x % i == 0:
      return False

  return True

list_bilangan_prima = []
def cari_bilangan_prima (awal, akhir):

  for x in range(awal, akhir + 1):
    if is_prima(x):
      list_bilangan_prima.append(x)

  return list_bilangan_prima
awal = int(input("Masukkan Awal : "))
akhir = int(input("Masukkan Akhir : "))
cari_bilangan_prima(awal,akhir)
print(f"Jumlah Bilangan Prima Dari {awal}-{akhir} adalah {len(list_bilangan_prima)}")