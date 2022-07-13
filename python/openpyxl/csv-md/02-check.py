filename = 'faktur-keluaran.csv'

# prepare header

hd_fk  = '"FK","Kode","Ganti","Faktur","Masa","Tahun","Tanggal",' + \
         '"NPWP","Nama","Alamat","DPP,"PPn","PPnBM","Keterangan",' + \
         '"FG","UM DPP","UM PPn","UM PPnBM","Referensi"'

hd_fpr = '"LT","Nama","Alamat","Perekam","Wilayah","Timestamp","Hash"'

hd_of  = '"OF","Kode","Nama","Satuan","Jumlah","Total",' + \
         '"Diskon","DPP","PPN","Tarif","PPnBM"'

keys_fk = hd_fk.split('",')
keys_fk = [key.replace('"', '') for key in keys_fk]

keys_fpr = hd_fpr.split('",')
keys_fpr = [key.replace('"', '') for key in keys_fpr]

keys_of = hd_of.split('",')
keys_of = [key.replace('"', '') for key in keys_of]

# parse lines

with open(filename) as f:
  lines = f.readlines()
  f.close()

count = 0
for line in lines:
  count += 1
  if (count>3) and (count<10):
    values = line.split('",')
    values = [value.replace('"', '') for value in values]

    if values[0]=="FK":
      pairs = dict(zip(keys_fk, values))
      for key in pairs:
        print(f'{key:>10} : {pairs[key][:40]}')
      print()

    if values[0]=="FAPR":
      pairs = dict(zip(keys_fpr, values))
      for key in pairs:
        print(f'{key:>10} : {pairs[key][:40]}')
      print()

    if values[0]=="OF":
      pairs = dict(zip(keys_of, values))
      for key in pairs:
        print(f'{key:>10} : {pairs[key][:40]}')
      print()
