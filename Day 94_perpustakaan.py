# Program perpustakaan sederhana

# Dictionary untuk menyimpan informasi buku
buku = {
    "judul": "Belajar Python",
    "pengarang": "John Smith",
    "tahun_terbit": 2020
}

# Fungsi untuk menampilkan informasi buku
def tampilkan_info_buku(buku):
  print(f"Judul buku: {buku['judul']}")
  print(f"Pengarang: {buku['pengarang']}")
  print(f"Tahun terbit: {buku['tahun_terbit']}")

# Panggil fungsi untuk menampilkan informasi buku
tampilkan_info_buku(buku)