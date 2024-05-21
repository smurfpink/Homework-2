import tugas as tg2

print(f'{5*"="}Selamat Datang Di Program Manajemen Barang{5*"="}')
print("Masukkan Pilihan\n1.Tambah Barang\n2.Cari Barang\n3.Hapus Barang\n4.Edit Barang\n5.Tampilkan Data Barang\n6.Tampilkan Jumlah Data\n7.Keluar")

while True:
    pilihan = int(input('Masukkan Pilihan: '))
    if pilihan == 1:
        tg2.sum()
    elif pilihan == 2:
        tg2.search()
    elif pilihan == 3:
        tg2.delete()
    elif pilihan == 4:
        tg2.edit()
    elif pilihan == 5:
        print(f"{10*'='}Toko Elektronik{10*'='}")
        tg2.view_data()
    elif pilihan == 6:
        tg2.view_item_cout()
    elif pilihan == 7:
        print("Terima Kasih Telah Menggunakan Program Kami")
        break