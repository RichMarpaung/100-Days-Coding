import random

angka_rahasia = random.randint(1, 1000)


batas_percobaan = 10
print("Tebak Angka Rahasia 1-1000")
print("Kamu memiliki 10 kesempatan")
for percobaan in range(batas_percobaan):
  jawaban = int(input(f'\n[Percobaan {percobaan + 1}] Masukkan angka: '))

  if jawaban == angka_rahasia:
    print("Selamat, Tebakan mu Benar")
    break
  elif jawaban<angka_rahasia:
    print("Tebakan mu terlalu kecil!")
  elif jawaban > angka_rahasia:
    print("Tebakan mu terlalu besar!")
  

else:
    print("\nSayang Sekali kesempatan Habis")
    print(f"Angka Rahasia nya adalah {angka_rahasia}")