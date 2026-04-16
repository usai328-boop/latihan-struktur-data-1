barang = []
harga = []
total = 0

jumlah = int(input("Masukkan jumlah barang: "))

for i in range(jumlah):
    nama = input(f"Masukkan nama barang ke-{i+1}: ")
    h = int(input(f"Masukkan harga {nama}: "))

    barang.append(nama)
    harga.append(h)

print("\nDaftar belanja:")
for i in range(len(barang)):
    print(f"{barang[i]} - Rp{harga[i]}")
    total += harga[i]

print("Total bayar: Rp", total)