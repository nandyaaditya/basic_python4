

kontak = []


while True:
    print("Selamat datang!")
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        print("Daftar kontak:")
        for ktk in kontak:
            print("Nama: {} ".format(ktk["Nama"]))
            print("No Telepon: {} ".format(ktk["telepon"]))
    elif pilihan == "2":
        nama = input("Nama: ")
        tlp = input("No Telepon: ")
        tambah_kontak = {"Nama": nama, "telepon": tlp}
        kontak.append(tambah_kontak)
        print("Kontak berhasil ditambahkan")
    elif pilihan == "3":
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia")

