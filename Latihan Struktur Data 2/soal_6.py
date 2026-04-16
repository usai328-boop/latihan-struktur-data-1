inventaris = {
"Pensil": 10,
"Buku": 3,
"Penghapus": 2,
"Pulpen": 7
}

print("Barang dengan stok rendah:")

for barang, stok in inventaris.items():
    if stok < 5:
        print(barang, "- stok:", stok)