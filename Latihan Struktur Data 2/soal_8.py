nilai = {
"Andi": 80,
"Budi": 60,
"Citra": 75,
"Dina": 70
}

lulus = []
tidak_lulus = []

for nama, n in nilai.items():
    if n >= 75:
        lulus.append(nama)
    else:
        tidak_lulus.append(nama)

print("Mahasiswa lulus:", lulus)
print("Mahasiswa tidak lulus:", tidak_lulus)