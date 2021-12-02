#!/usr/bin/env python

import inkex, simplestyle
from lxml import etree

def draw_SVG_square(w,h, x,y, parent):
    style = { 'stroke'        : 'none',
              'stroke-width'  : '1',
              'fill'          : '#000000'
            }

    attribs = {
        'style'     : str(inkex.Style(style)),
        'height'    : str(h),
        'width'     : str(w),
        'x'         : str(x),
        'y'         : str(y)
            }
    circ = etree.SubElement(
        parent, inkex.addNS('rect','svg'), attribs )
    return circ

class Kotak(inkex.EffectExtension):
  def effect(self):
    parent = self.svg.get_current_layer()
    draw_SVG_square(100,100, 0,0, parent)

if __name__ == '__main__':
  Kotak().run()


