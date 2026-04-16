kalimat = "saya makan nasi saya minum air"
kata_list = kalimat.split()

frekuensi = {}

for kata in kata_list:
    if kata in frekuensi:
        frekuensi[kata] += 1
    else:
        frekuensi[kata] = 1

print("Frekuensi kata:")
for kata, jumlah in frekuensi.items():
    print(kata, ":", jumlah)