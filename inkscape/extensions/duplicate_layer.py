#!/usr/bin/env python

import inkex
import sys, copy

class DuplicateLayer(inkex.EffectExtension):
  def get_layers(self):
    return {g
        for g in self.svg.xpath('//svg:g')
        if g.get('inkscape:groupmode') == 'layer'
      }

  def find_layer(self, layers, label_name):
    for layer in layers:
      name = layer.get('inkscape:label')
      if name == label_name:
        return layer

    return None

  def duplicate_layer(self, container, source_layer, layer_label, text_span):
    new_layer = copy.deepcopy(source_layer)
    new_layer.label = layer_label
    new_layer.style = 'display:none'
    container.append(new_layer)

    for node in new_layer:
      if isinstance(node, inkex.TextElement):
        tspan = node[0]
        tspan.text = text_span

  def effect(self):
    all_layers   = self.get_layers()
    container    = self.find_layer(all_layers,'Container')
    source_layer = self.find_layer(all_layers, 'Template')

    self.duplicate_layer(
      container, source_layer,
      'Zeta Mataharani', 'Zeta Mataharani, MD')

if __name__ == '__main__':
  DuplicateLayer().run()
