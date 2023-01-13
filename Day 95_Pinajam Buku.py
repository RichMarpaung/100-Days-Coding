# Daftar buku yang tersedia di perpustakaan
buku = {
    "Fiksi": ["Novel", "Komik", "Cerita Bergambar"],
    "Non-Fiksi": ["Buku Sains", "Buku Sejarah", "Buku Biografi"]
}

# Daftar peminjam
peminjam = {}

def tambah_peminjam(nama, judul):
  # Mengecek apakah buku tersedia
  tersedia = False
  for jenis, daftar_buku in buku.items():
    if judul in daftar_buku:
      tersedia = True
      break
      
  # Jika buku tersedia, menambahkan nama peminjam ke daftar peminjam
  if tersedia:
    if nama in peminjam:
      peminjam[nama].append(judul)
    else:
      peminjam[nama] = [judul]
      
    print(f"Buku {judul} berhasil dipinjam oleh {nama}")
  else:
    print(f"Maaf, buku {judul} tidak tersedia.")

tambah_peminjam("Andi", "Novel")
tambah_peminjam("Budi", "Buku Sains")
tambah_peminjam("Cindy", "Komik")
tambah_peminjam("David", "Buku Matematika")

print(peminjam)