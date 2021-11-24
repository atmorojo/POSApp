#!/usr/bin/python3 

import firebirdsql

print("Connecting...")
connection  = firebirdsql.connect(
    host    = 'localhost',
    database= 'C:\msys64\home\KITAGROUP\KASIRRUSAK\BACKOFFICE.FDB',
    port    = 3050,
    user    = 'SYSDBA',
    password= 'masterkey'
    )

cursor = connection.cursor()
f = open("laporan.csv", "w")
listToStr = "Struk_trans, Jumlah\n"
struk = ""

def print_trans():
  print("Serving transaction data...")
  global listToStr
  totalbelanja = 0
  global struk
  for c in cursor.fetchall():
    if struk != c[0]:
      if struk != "" and totalbelanja != 0:
        listToStr += "%s,%d\n"%(struk, totalbelanja)
      totalbelanja = 0
      struk = c[0]
    totalbelanja += int(c[3])

def print_invoice():
  print("Serving invoice data...")
  global listToStr
  listToStr += "%s,%s\n"%("Struk_inv", "Jumlah_di_inv")
  for c in cursor.fetchall():
    listToStr += "%s,%d\n"%(c[0], int(c[1]))

def show_tables():
  cursor.execute("SELECT a.RDB$RELATION_NAME FROM RDB$RELATIONS a WHERE COALESCE(RDB$SYSTEM_FLAG, 0) = 0")
  print_cursor()

def show_trans():
  cursor.execute("SELECT STRUK, NAMA_PLU, QTY, NILAI_HJUAL FROM TB_31TRANS WHERE TANGGAL='2021-08-18'")
  print_trans()

def show_invoice():
  cursor.execute("SELECT STRUK, TOTAL FROM TB_32POSINV WHERE TANGGAL='2021-08-18'")
  print_invoice()

show_trans()
show_invoice()

f.write(listToStr)

connection.close()
