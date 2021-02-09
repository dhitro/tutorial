import mysql.connector
import xlrd

#membuat koneksi mysql
#membuat koneksi
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="latihan_mysqlpy"
)

#membuat table
mycursor = mydb.cursor()

#membuat table
mycursor.execute("""
        CREATE TABLE IF NOT EXISTS  mahasiswa 
        (id INT AUTO_INCREMENT PRIMARY KEY,
        nama VARCHAR(255),
        kelas VARCHAR(255), 
        jurusan VARCHAR(255))""")

#membaca file excel , insert
namefile = "Book1.xls"
excel = xlrd.open_workbook(namefile)
sheet = excel.sheet_by_index(0)
jum_row = sheet.nrows

for baris in range(jum_row):
    if baris == 0:
        continue
    else:
        # insert data
        sql = "INSERT INTO mahasiswa(nama,kelas,jurusan) VALUES(%s,%s,%s)"
        val = tuple(sheet.row_values(baris))
        mycursor.execute(sql, val)
        mydb.commit()