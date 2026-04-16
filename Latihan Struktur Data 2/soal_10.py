produk = [
{"nama": "Laptop", "harga": 7000000},
{"nama": "Mouse", "harga": 150000},
{"nama": "Keyboard", "harga": 300000},
{"nama": "Monitor", "harga": 2000000}
]

# sorting
produk.sort(key=lambda x: x["harga"])

print("Produk setelah diurutkan:")
for item in produk:
    print(item["nama"], "-", item["harga"])