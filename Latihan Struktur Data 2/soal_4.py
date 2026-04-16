antrian = []

# tambah pasien
antrian.append("Pasien A")
antrian.append("Pasien B")
antrian.append("Pasien C")

print("Antrian awal:", antrian)

while len(antrian) > 0:
    pasien = antrian.pop(0)
    print("Melayani:", pasien)
    print("Sisa antrian:", antrian)