nilai_mahasiswa = {
"Andi": 80,
"Budi": 75,
"Citra": 90,
"Dina": 85
}

total = 0

for nama in nilai_mahasiswa:
    print(nama, ":", nilai_mahasiswa[nama])
    total += nilai_mahasiswa[nama]

rata_rata = total / len(nilai_mahasiswa)

print("Rata-rata nilai:", rata_rata)