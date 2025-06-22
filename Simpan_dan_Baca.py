def tampilkan_menu():
    print("\n=== Aplikasi Kontak Telepon ===")
    print("1. Tambah Kontak")
    print("2. Lihat Daftar Kontak")
    print("3. Keluar")

def tambah_kontak():
    nama = input("Masukkan nama kontak: ")
    nomor = input("Masukkan nomor telepon: ")

    with open("kontak.txt", "a") as file:
        file.write(f"{nama},{nomor}\n")
    print(f"Kontak '{nama}' berhasil disimpan.")

def lihat_kontak():
    print("\n=== Daftar Kontak ===")
    try:
        with open("kontak.txt", "r") as file:
            daftar = file.readlines()
            if not daftar:
                print("Belum ada kontak disimpan.")
            else:
                for i, kontak in enumerate(daftar, 1):
                    nama, nomor = kontak.strip().split(",")
                    print(f"{i}. {nama} - {nomor}")
    except FileNotFoundError:
        print("Belum ada file kontak. Tambahkan kontak dulu.")

# Main Loop
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        tambah_kontak()
    elif pilihan == "2":
        lihat_kontak()
    elif pilihan == "3":
        print("Terima kasih, keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
