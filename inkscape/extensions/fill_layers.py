#!/usr/bin/env python

import inkex
import sys, copy
from trainees.testbed import people

class FillLayers(inkex.EffectExtension):
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

  def duplicate_layer(self, container, source_layer, layer_id, layer_label):
    new_layer = copy.deepcopy(source_layer)
    new_layer.label = layer_label
    new_layer.set('id', layer_id)
    new_layer.style = 'display:none'
    container.append(new_layer)
    return new_layer

  def modify_display_name(self, target_layer, text_id, display_name):
    text_node = target_layer[0]
    if isinstance(text_node, inkex.TextElement):
      tspan = text_node[0]
      tspan.set('id', text_id)
      tspan.text = display_name

  def effect(self):
    all_layers   = self.get_layers()
    container    = self.find_layer(all_layers, 'Container')
    source_layer = self.find_layer(all_layers, 'Template')

    for key, person in people.items():
      number     = str(key).zfill(2)
      name_only  = person[1]
      name_title = person[2]

      # layer related
      layer_id     = 'person-id-' + number
      layer_label  = number + ' - ' + name_only
      target_layer = self.duplicate_layer(
        container, source_layer, layer_id, layer_label)

      # display name
      text_id   = 'display-id-' + number
      self.modify_display_name(target_layer, text_id, name_title)

if __name__ == '__main__':
  FillLayers().run()
