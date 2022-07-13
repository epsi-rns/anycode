filename = 'faktur-keluaran.csv'

# prepare header

header = '"FK","Kode","Ganti","Faktur","Masa","Tahun","Tanggal",' + \
         '"NPWP","Nama","Alamat","DPP,"PPn","PPnBM","Keterangan",' + \
         '"FG","UM DPP","UM PPn","UM PPnBM","Referensi"'

keys = header.split('",')
keys = [key.replace('"', '') for key in keys]

# parse lines

with open(filename) as f:
  lines = f.readlines()
  f.close()

count = 0
for line in lines:
  count += 1
  if count==4:
    print(f'line {count}:\n{line}')
    values = line.split('",')
    values = [value.replace('"', '') for value in values]

    pairs = dict(zip(keys, values))

    for key in pairs:
      print(f'{key:>10} : {pairs[key][:40]}')
