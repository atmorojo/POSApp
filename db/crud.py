#!/usr/bin/python3

import firebirdsql

# Kami mencoba buat fungsi dengan nama-nama yang mudah kami
# ingat, sejauh yang kami pahami dari arti CRUD. Tapi cuma 
# fungsi yang kami butuhkan aja, sih.
#       buka    koneksi ke database
#       baca    _read_, ambil data dari tabel
#       update  update XD

class SumberData:
  def __init__(self, dbhost, dbport, fdbfile, dbuser, dbpassword):
    self.connection = firebirdsql.connect(
        host    = dbhost,
        database= fdbfile,
        port    = dbport,
        user    = dbuser,
        password= dbpassword
        )

  def tutup(self):
    self.connection.close()

#  def baca_tabel(self):
#    self.cur.execute("SELECT a.RDB$RELATION_NAME \
#        FROM RDB$RELATIONS a \
#        WHERE COALESCE(RDB$SYSTEM_FLAG, 0) = 0")

  def baca_produk(self, kodebar):
    cur = self.connection.cursor()
    cur.execute("SELECT KODE, NAMA_PLU, HPP, \
        BARCODE1, HJUAL_ISI1, HJUAL_ISI2, \
        HJUAL_ISI3 FROM TB_12MASTER \
        WHERE BARCODE1='" + kodebar + "'")

    item = cur.fetchall()[0]
    produk = DataProduk(item[0], item[1], item[2], item[3], item[4], item[5], item[6])

    cur.close()
    return produk

  def get_data_produk(self):
    data_produk = list()
    cur = self.connection.cursor()
    cur.execute("SELECT KODE, NAMA_PLU, \
        HJUAL_ISI1, HJUAL_ISI2, \
        HJUAL_ISI3 FROM TB_12MASTER")
    items = cur.fetchall()

    for item in items:
      data_produk.append((item[0], item[1], str(item[2]), str(item[3]), str(item[4])))

    return data_produk


# def update_tabel():

#  def daftar_tabel(self):
#    baca_definisi_master()
#    for baris in sumber_data.fetchall():
#      print(*baris, sep = "\n")

class DataProduk:
  def __init__(self, kode, nama, hpp, barcode, harga1, harga2, harga3):
    self.kode = kode
    self.nama = nama
    self.hpp = hpp
    self.barcode = barcode
    self.harga1 = harga1
    self.harga2 = harga2
    self.harga3 = harga3

  def getKode(self):
    return self.kode

  def getNama(self):
    return self.nama

  def getHpp(self):
    return float(self.hpp)

  def getBarcode(self):
    return self.barcode

  def getHarga1(self):
    return float(self.harga1)

  def getHarga2(self):
    return float(self.harga2)

  def getHarga3(self):
    return float(self.harga3)
