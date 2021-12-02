#!/usr/bin/env python
import inkex

class QueryLayer(inkex.EffectExtension):
  def effect(self):
    self.recurse(1, self.svg)

  def recurse(self, level, nodes):
    for node in sorted(nodes, key =  self._sort):
      if isinstance(node, inkex.ShapeElement):
        if node.get('inkscape:groupmode') == 'layer':
          self.print_layer_name(level, node)
          self.recurse(level+1, node)

  def print_layer_name(self, level, node):
    label_name = node.get('inkscape:label')
    inkex.errormsg('-'*level + ' ' +label_name)

  def _sort(self, node):
    if node.get('inkscape:groupmode') == 'layer':
      return node.get('inkscape:label')
    else:
      return  ""

if __name__ == "__main__":
    QueryLayer().run()
