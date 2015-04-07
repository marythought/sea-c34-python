#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.

class Element(object):
    def __init__(self, name=""):
        # Initialize a page element
        self.name = name
        # some other stuff:
        self.tagopen = "<" + str(name) + ">"
        self.tagclose = "</" + str(name) + ">"
        self.text = []
        # self.ind = " "

    def append(self, text):
        self.text.append(text+"\n")

    def render(self, outfile, ind =" "):
        #move tagopen close etc down here
        x = "\n<>" + "\n" + str(self.text) + "\n</>"
        outfile.write(x)


class Html(Element):
    def __init__(self, name="body", ind=0):
        self.tagopen = "<" + str(name) + ">"
        self.tagclose = "</" + str(name) + ">"
        self.ind = ind*" "
        header = "<!DOCTYPE html>"

    def append(self, text):
        self.text += self.tagopen+self.ind+text+self.tagclose+"\n"

    # something for the <DOC type tag>


class Body(Element):
    def __init__(self, name="body", ind=8):
        self.tagopen = "<" + str(name) + ">"
        self.tagclose = "</" + str(name) + ">"
        self.ind = ind*" "

    def append(self, text):
        self.text += self.tagopen+self.ind+text+self.tagclose+"\n"


class P(Element):
    def __init__(self, name="p", ind=16):
        self.name = name
        self.tagopen = "<" + str(name) + ">"
        self.tagclose = "</" + str(name) + ">"
        self.ind = ind*" "

