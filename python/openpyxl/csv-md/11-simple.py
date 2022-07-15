import re

# Master Detail Faktur Exporter Class
class FakturMD:
  header_fk  = \
    '"FK","Kode","Ganti","Faktur","Masa","Tahun","Tanggal",' + \
    '"NPWP","Nama","Alamat","DPP","PPn","PPnBM","Keterangan",' + \
    '"FG","UM DPP","UM PPn","UM PPnBM","Referensi"'

  def __init__(self, filename):
    # prepare header
    keys = re.split(r',(?=")', self.header_fk)
    self.keys = [key.replace('"', '') for key in keys]

    # parse lines
    with open(filename) as f:
      self.lines = f.readlines()
      f.close()

  def run(self):
    count = 0

    for line in self.lines:
      count += 1
      if count==4:
        print(f'line {count}:\n{line}')
        values = re.split(r',(?=")', line)
        values = [value.replace('"', '') for value in values]

        pairs = dict(zip(self.keys, values))

        for key in pairs:
          print(f'{key:>10} : {pairs[key][:40]}')

def main():
  filename = 'faktur-keluaran.csv'
  md = FakturMD(filename)
  md.run()

main()


