antrian = []

while True:
    print("\n=== MENU ===")
    print("1. Tambah Antrian")
    print("2. Layani Nasabah")
    print("3. Lihat Antrian")
    print("4. Keluar")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        nama = input("Nama nasabah: ")
        antrian.append(nama)
        print(nama, "masuk antrian")

    elif pilihan == "2":
        if len(antrian) > 0:
            print("Melayani:", antrian.pop(0))
        else:
            print("Antrian kosong")
    
    elif pilihan == "3":
        print("Antrian sekarang:", antrian)
    
    elif pilihan == "4":
        print("Terima kasih")
        break
    
    else:
        print("Pilihan tidak valid")