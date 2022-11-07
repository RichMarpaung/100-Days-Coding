def mean (data):
    jumlah = sum(data)
    panjang = len(data)
    hasil = jumlah / panjang
    return hasil
def median (deret):
    deret.sort()
    n = len(deret)
    tengah = n //2
    if n % 2 == 1 :
        return deret[tengah]
    if n%2 == 0:
        hasil = (deret[tengah-1] +deret[tengah]) / 2
        return hasil
def nilai_terbanyak(deret):
  # dictionary untuk mapping nilai terbanyak
  peta_kemunculan = {}
  # perulangan satu-persatu tiap bilangan
  for bilangan in deret:
    # periksa apakah sudah pernah muncul atau belum
    if bilangan in peta_kemunculan:
      peta_kemunculan[bilangan] += 1
    else:
      peta_kemunculan[bilangan] = 1
  # cari kemunculan terbanyak
  bilangan_terbesar = deret[0] # ambil angka pertama sebagai yg terbanyak
  for bilangan in peta_kemunculan.keys():
    jumlah = peta_kemunculan[bilangan]
    if jumlah > peta_kemunculan[bilangan_terbesar]:
      bilangan_terbesar = bilangan

  return bilangan_terbesar
       
data_masuk = input("Masukkan Data (pisahkan dengan koma) : ")

deret = []
for angka in data_masuk.split(','):
    deret.append(int(angka))
#Mean
print(f"Data = {deret}")
print(f'Mean = {mean(deret)}')
#median
print(f"Data = {deret}")
print(f"Median = {median(deret)}")
#modus
print(f"Data = {deret}")
print(f"Modus = {nilai_terbanyak(deret)}")

