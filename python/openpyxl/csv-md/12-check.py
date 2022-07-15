import re

def split_quotes(header):
  keys = re.split(r',(?=")', header)
  return [key.replace('"', '') for key in keys]

# Master Detail Faktur Exporter Class
class FakturMD:
  def __init__(self, filename):
    # prepare header
    self.init_header_keys()

    # parse lines
    with open(filename) as f:
      self.lines = f.readlines()
      f.close()

  def init_header_keys(self):
    header_fk  = \
      '"FK","Kode","Ganti","Faktur","Masa","Tahun","Tanggal",' + \
      '"NPWP","Nama","Alamat","DPP","PPn","PPnBM","Keterangan",' + \
      '"FG","UM DPP","UM PPn","UM PPnBM","Referensi"'

    header_fpr = \
      '"LT","Nama","Alamat","Perekam","Wilayah","Timestamp","Hash"'

    header_of  = \
      '"OF","Kode","Nama","Satuan","Jumlah","Total",' + \
      '"Diskon","DPP","PPN","Tarif","PPnBM"'

    self.keys_fk  = split_quotes(header_fk)
    self.keys_fpr = split_quotes(header_fpr)
    self.keys_of  = split_quotes(header_of)

  def print_header_keys(self, keys, values):
    pairs = dict(zip(keys, values))
    for key in pairs:
      print(f'{key:>10} : {pairs[key][:40]}')
    print()

  def run(self):
    count = 0

    for line in self.lines:
      count += 1

      # ignore the first three lines
      if (count>3) and (count<10):
        values = split_quotes(line)

        if values[0]=="FK":
          self.print_header_keys(self.keys_fk, values)

        if values[0]=="FAPR":
          self.print_header_keys(self.keys_fpr, values)

        if values[0]=="OF":
          self.print_header_keys(self.keys_of, values)

def main():
  filename = 'faktur-keluaran.csv'
  md = FakturMD(filename)
  md.run()

main()
