import xlrd

#membuka file excel
namafile = 'Book1.xls'
excel = xlrd.open_workbook(namafile)

#aktif di sheet
sheet = excel.sheet_by_index(0)

#membaca cell
print(sheet.cell_value(3,2))

#menghitung jumlah kolom dan baris
jum_col = sheet.ncols
jum_row = sheet.nrows

print(f'jumlah kolom = {jum_col}, jumlah baris = {jum_row}')
#mengambil header
header = []
for kolom in range(jum_col):
    # print(sheet.cell_value(0,kolom))
    header.append(sheet.cell_value(0,kolom))
print('header 1:')
print(header)
print('header 2:')
print(sheet.row_values(0))

#mengambil data
print('data 1:')
data = []
for baris in range(jum_row):
    if baris == 0:
        continue
    else:
        for kolom in range(jum_col):
            data.append(sheet.cell_value(baris,kolom))
            # print(sheet.cell_value(baris,kolom))
        print(tuple(data) )
        data.clear()
print('data 2:')
for baris in range(jum_row):
    if baris == 0:
        continue
    print(tuple(sheet.row_values(baris)))