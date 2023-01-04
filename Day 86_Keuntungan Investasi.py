modal = int(input("Masukkan Modal awal : "))
tahun = int(input("Masukkan Jangan Tahun : "))

for i in range (1,tahun+1):
    untung = modal*(5/100)
    print(f"Keuntungan tahun ke-{i} adalah Rp.{untung}")
    modal += untung