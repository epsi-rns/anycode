#! /usr/bin/python3
import xml.etree.ElementTree as ET
import os
import copy
import sys
from trainees_testbed import people

tree = ET.parse('cert-testbed.svg')
root = tree.getroot()

for key, person in people.items():
  number     = str(key).zfill(2)
  name_only  = person[1]
  name_title = person[2]

  element = root.find(".//*[@id='person-id-" + number + "']")
  name = element.find(".//*[@id='display-id-" + number + "']")
  print(element.get('id') + ' : ' + name.text)
 
  svg_filename = 'Sertifikat - ' + name_only + '.svg'
  element.set('style', 'display:inline')
  tree.write (svg_filename)
  element.set('style', 'display:none')

  pdf_filename = '"./pdf/Sertifikat - ' + name_only + '.pdf"'
  png_filename = '"./Sertifikat - ' + name_only + '.png"'

  pdf_cmd = 'inkscape "' + svg_filename + '" ' +\
            "--export-area-page --batch-process " +\
            "--export-type=pdf --export-filename=" + pdf_filename

  png_cmd = 'inkscape "' + svg_filename + '" ' +\
            "--export-area-page --batch-process --export-dpi=96 " +\
            "--export-type=png --export-filename=" + png_filename +\
            " 2> nul"

  os.system(pdf_cmd)
  os.system(png_cmd)
