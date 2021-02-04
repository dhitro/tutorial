import mysql.connector

#membuat koneksi
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="latihan_mysqlpy"
)

# print(mydb)

#membuat database
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE latihan_mysqlpy")

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

#membuat table
mycursor.execute("CREATE TABLE IF NOT EXISTS  mahasiswa (id INT AUTO_INCREMENT PRIMARY KEY,nama VARCHAR(255),kelas VARCHAR(255), jurusan VARCHAR(255))")

#insert
sql = "INSERT INTO mahasiswa(nama,kelas,jurusan) VALUES(%s,%s,%s)"
val = ("test7","1-A","matematika")
mycursor.execute(sql,val)
mydb.commit()

#delete
nama = "test"
mycursor.execute(f"DELETE FROM mahasiswa where nama ='{nama}'")
mydb.commit()

#update

mycursor.execute(f"UPDATE mahasiswa SET nama = 'test6' where id =5")
mydb.commit()

#select
mycursor.execute("SELECT * FROM mahasiswa")
result = mycursor.fetchall()
for data in result:
    print(data[1])

#drop table
mycursor.execute("DROP TABLE mahasiswa")
