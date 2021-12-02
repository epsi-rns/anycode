#!/usr/bin/env python

from testbed import people

for key, person in people.items():
  number     = str(key).zfill(2)
  name_only  = person[1]
  name_title = person[2]

  # layer related
  layer_id   = 'person-id-' + number
  layer_name = number + ' - ' + name_only
  print(layer_id)
  print(layer_name)
  
  # display name
  text_id   = 'display-id-' + number
  print(text_id)
  print(name_title)

  # just another newline
  print()
