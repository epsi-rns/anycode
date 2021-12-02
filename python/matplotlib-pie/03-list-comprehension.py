import pprint

my_print = pprint.PrettyPrinter(width=60, compact=True)

# dict { location : (trainee, date, additional data) }

response = {
  'Bandung' : (50, '10 Oct', 0.1),
  'Banjar'  : (31, '13 Oct', 0.1),
  'Bekasi'  : (28, '15 Oct', 0.1),
  'Bogor'   : (50, '26 Oct', 0.1),
  'Cimahi'  : (10, '28 Oct', 0.2),
  'Cirebon' : (46, '08 Nov', 0.1),
  'Depok'   : (38, '08 Nov', 0.1),
  'Sukabumi': (47, '20 Nov', 0.1)
}

elements = list(response.values())
trainees = [el[0] for el in elements]
date     = [el[1] for el in elements]
explode  = [el[2] for el in elements]
legends  = [
    "%s/ %s" % (value[1], key)
    for key, value
    in response.items() ]
total    = sum(trainees)

my_print.pprint(legends)
my_print.pprint(trainees)

print("Total of %d trainees." % total)
print("Respondent = {:d} Trainees.".format(total))
