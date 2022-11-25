def keliling (sisi):
    kel = sisi*12
    if kel % 2 ==1 or kel % 2 ==0:
        return int(kel)
    return kel

sisi = float(input("Masukkan Panjang Sisi (cm): "))
if sisi % 2 ==1 or sisi % 2 ==0:
    sisi = int(sisi)

print(40*"=")
print(f"Panjang sisi \t: {sisi} cm")
print(f"Rumus Keliling Kubus adalah : Sisi * 12")
print(f"Keliling Kubus adalah {sisi} cm * 12 = {keliling(sisi)} cm")
print(40*"=")