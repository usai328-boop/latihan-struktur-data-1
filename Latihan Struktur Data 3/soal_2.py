data = {}
total = 0

jumlah = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah):
    nama = input(f"Nama mahasiswa ke-{i+1}: ")
    nilai = int(input(f"Nilai {nama}: "))
    
    data[nama] = nilai
    total += nilai

rata = total / jumlah

print("\nData Mahasiswa:")
for nama, nilai in data.items():
    status = "Lulus" if nilai >= 75 else "Tidak Lulus"
    print(nama, "-", nilai, "-", status)
    print("Rata-rata nilai:", rata)