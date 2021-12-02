#!/usr/bin/env python
# coding=utf-8

import inkex
import sys, copy

class DuplicateLayer(inkex.EffectExtension):
  def get_layers(self):
    return {g
        for g in self.svg.xpath('//svg:g')
        if g.get('inkscape:groupmode') == 'layer'
      }

  def find_container(self, layers, label_name):
    for layer in layers:
      name = layer.get('inkscape:label')
      if name == label_name:
        return layer

    return None

  def find_source_layer(self, layers, label_name):
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

    # with open('blewah.svg', 'w') as f:
    self.save("blewah.svg")

  def effect(self):
    all_layers   = self.get_layers()
    container    = self.find_container   (all_layers,'Container')
    source_layer = self.find_source_layer(all_layers, 'Nama00')

    self.duplicate_layer(
      container, source_layer,
      'Nama01', 'Manusia Blewah')

if __name__ == '__main__':
  DuplicateLayer().run()
