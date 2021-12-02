# dict { location : (number of trainee, date of training) }

response = {
  'Bandung' : (50, '10 Oct'),
  'Banjar'  : (31, '13 Oct'),
  'Bekasi'  : (28, '15 Oct')
}

locations = list(response.keys())
elements  = list(response.values())

print(locations)
print(elements)
