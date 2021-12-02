#!/usr/bin/env python
import inkex
from inkex.elements import TextElement

class Hello(inkex.GenerateExtension):
    def add_arguments(self, pars):
        pars.add_argument("--greeting_text",
            type=str, default="Yellow Here",
            help="Cute Greeting Text")

    def generate(self):
      textElement = TextElement()
      textElement.text = str(self.options.greeting_text)
      return textElement

if __name__ == '__main__':
    Hello().run()
