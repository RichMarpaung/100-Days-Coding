print("Menghitung Pajak Bumi Bangunan")
luas_tanah= float(input("Masukkan Luas Tanah (m²): "))
luas_bangunan = float(input("Maskkan Luas Bangunan (m²) : "))

harga_tanah = 10000000
harga_bangunan = 15000000
njop_tanah = luas_tanah*harga_tanah
njop_bangunan = luas_bangunan*harga_bangunan
njop = njop_tanah+njop_bangunan
pbb = njop * 0.005


print("========================================")
print(f"Luas Tanah \t: {luas_tanah} m² dengan harga {harga_tanah}/m²")
print(f"Luas Bangunan \t: {luas_bangunan}m²  dengan harga {harga_bangunan}/m")
print("========================================")
print(f"NJOP Tanah \t: {luas_tanah} * Rp.{harga_tanah} \t= Rp.{int(njop_tanah)}")
print(f"NJOP Bangunan \t: {luas_bangunan} * Rp.{harga_bangunan} \t= Rp.{int(njop_bangunan)}")
print(f"NJOP \t\t: Rp.{int(njop_tanah)} + Rp .{int(njop_bangunan)} = Rp.{int(njop)}")
print("========================================")
print(f"PBB \t\t: {int(njop)} * 0.5% =Rp.{int(pbb)}")
