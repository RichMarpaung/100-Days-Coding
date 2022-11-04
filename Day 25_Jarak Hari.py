print("MOHON MASUKKAN DATA DENGAN ANGKA")
day = int(input("Masukkan Tanggal : "))
bulan = int(input("Masukan Bulan : "))
tahun = int(input("Masukan Tahun : "))

hasil_hari = day - 1
hasil_bulan = bulan - 1
hasil_tahun = tahun - 1900
if tahun >=1900:
    jmlh = hasil_hari + (hasil_bulan*30)+(hasil_tahun*360)
    print (f"Jarak Hari Antara {day}-{bulan}-{tahun} dengan 1-1-1900 ")
    print ("adalah :")
    print (jmlh,"hari")
else:
    print ("Mohon Masukkan Tahun di atas 1900")
