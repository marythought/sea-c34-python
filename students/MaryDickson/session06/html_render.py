#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.

class Element(object):
    # tag = ??
    def __init__(self, name="element"):
        # Initialize a page element
        self.name = name
        # some other stuff:
        self.open = "<" + str(name) + ">"
        self.close = "</" + str(name) + ">"
        self.text = ""

    def append(self, text):
        self.text = str(text)
        print text
        self.text += "\n"+text

    def render(self, outfile):
        x = "\n<>" + "\n" + str(self.text) + "\n</>"
        outfile.write(x)

