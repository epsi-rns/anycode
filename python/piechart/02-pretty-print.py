import pprint

# dict { location : (number of trainee, date of training) }

response = {
  'Bandung' : (50, '10 Oct'),
  'Banjar'  : (31, '13 Oct'),
  'Bekasi'  : (28, '15 Oct'),
  'Bogor'   : (50, '26 Oct'),
  'Cimahi'  : (10, '28 Oct'),
  'Cirebon' : (46, '08 Nov'),
  'Depok'   : (38, '08 Nov'),
  'Sukabumi': (47, '20 Nov')
}

locations = [key for key, value in response.items()]
elements  = [value for key, value in response.items()]

my_print  = pprint.PrettyPrinter(width=60, compact=True)
my_print.pprint(locations)
my_print.pprint(elements)
