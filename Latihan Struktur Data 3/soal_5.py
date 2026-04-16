inventaris = {}

while True:
    print("\n=== MENU INVENTARIS ===")
    print("1. Tambah Barang")
    print("2. Kurangi Stok")
    print("3. Lihat Barang")
    print("4. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama barang: ")
        stok = int(input("Jumlah stok: "))
        inventaris[nama] = stok
        print("Barang ditambahkan")

    elif pilih == "2":
        nama = input("Nama barang: ")
        if nama in inventaris:
            jumlah = int(input("Jumlah yang diambil: "))
            if inventaris[nama] >= jumlah:
                inventaris[nama] -= jumlah
                print("Stok berhasil dikurangi")
            else:
                print("Stok tidak cukup")
        else:
            print("Barang tidak ditemukan")
    elif pilih == "3":
        print("\nDaftar Inventaris:")
        for barang, stok in inventaris.items():
            print(barang, "-", stok)
    elif pilih == "4":
        print("Program selesai")
        break
    else:
        print("Pilihan salah")