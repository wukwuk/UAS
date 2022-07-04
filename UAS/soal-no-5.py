import mysql.connector
import os
from prettytable import PrettyTable

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mahasiswa"
)


def tambah():
    cursor = db.cursor()
    os.system('cls')
    nama = input('Masukkan Nama: ')
    nim = input('Masukkan Nim (8 digit tanpa titik): ')
    if len(nim) != 8:
        print('nim salah')
        tambah()
        menu()
    prodi = input('Masukkan Program Studi: ')
    j_kel = input('Pilih Jenis Kelamin (l/p): ')
    if j_kel == 'l':
        j_kel = 'Laki-laki'
    elif j_kel == 'p':
        j_kel = 'Perempuan'
    else:
        print('pilihan salah')
        tambah()
        menu()
    alamat = input('Masukkan alamat: ')
    sql = "insert into data(nama,nim,prodi,j_kel,alamat) values(%s,%s,%s,%s,%s)"
    val = (nama, nim, prodi, j_kel, alamat)
    cursor.execute(sql, val)
    db.commit()
    print("Data berhasil ditambahkan")


def ubah():
    cursor = db.cursor()
    update = input('Pilih data mahasiswa yang akan diubah (berdasarkan id): ')
    os.system('cls')
    nama = input('Masukkan Nama baru: ')
    nim = input('Masukkan Nim baru (8 digit tanpa titik): ')
    if len(nim) != 8:
        print('nim salah')
        ubah()
        menu()
    prodi = input('Masukkan Program Studi baru: ')
    j_kel = input('Pilih Jenis Kelamin (l/p): ')
    if j_kel == 'l':
        j_kel = 'Laki-laki'
    elif j_kel == 'p':
        j_kel = 'Perempuan'
    else:
        print('pilihan salah')
        ubah()
        menu()
    alamat = input('Masukkan alamat baru: ')
    sql = "UPDATE data SET nama=%s,nim=%s,prodi=%s,j_kel=%s,alamat=%s WHERE id=%s"
    val = (nama, nim, prodi, j_kel, alamat, update)
    cursor.execute(sql, val)
    db.commit()
    print("Data berhasil diubah")


def hapus():
    cursor = db.cursor()
    delete = input('Masukkan ID Mahasiswa yang akan dihapus: ')
    sql = "DELETE FROM data WHERE id=%s" % delete
    cursor.execute(sql)
    db.commit()
    print('Data berhasil dihapus')


def menu():
    cursor = db.cursor()
    sql = "SELECT * FROM data"
    cursor.execute(sql)
    hasil = cursor.fetchall()
    t = PrettyTable(['id', 'nama', 'nim', 'prodi', 'j_kel', 'alamat'])
    os.system('cls')
    for row in hasil:
        t.add_row(row)
    print(t)

    print('DAFTAR PERINTAH')
    print('1.Tambah Data')
    print('2.Ubah Data')
    print('3.Hapus Data')
    print('Ketik exit jika ingin keluar')
    menu = input('Pilih Menu(1/2/3/exit): ')

    if menu == '1':
        tambah()
    if menu == '2':
        ubah()
    if menu == '3':
        hapus()
    elif menu == 'exit':
        os.system('cls')
        quit()


if __name__ == "__main__":
    while(True):
        menu()
