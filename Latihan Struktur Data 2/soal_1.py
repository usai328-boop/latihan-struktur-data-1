barang = ["beras", "gula", "minyak"]
harga = [12000, 8000, 15000]

total = 0

print("Daftar belanja:")
for i in range(len(barang)):
    
    print(f"{barang[i]} - Rp{harga[i]}")
    total += harga[i]

print("Total yang harus dibayar: Rp", total)