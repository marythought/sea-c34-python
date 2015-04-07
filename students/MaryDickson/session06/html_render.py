#!/usr/bin/env python


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

    def render(self, outfile, ind=" "):
        #move tagopen close etc down here
        x = "\n<>" + "\n" + str(self.text) + "\n</>"
        # indent
        # open tag
        # for each child,
        #   all child.render() ?
        # closing tag
        outfile.write(x)


class Html(Element):
    def __init__(self, name="body", ind=0):
        self.tagopen = "<" + str(name) + ">"
        self.tagclose = "</" + str(name) + ">"
        self.ind = ind*" "
        header = "<!DOCTYPE html>"

    def append(self, text):
        self.text += self.tagopen + self.ind + text + self.tagclose + "\n"

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


"""
#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    """An HTML element."""
    tag = u"html"
    indent = u"    "

    def __init__(self, content=None):
        self.content = self.indent + str(self.content) if content else ""

    def append(self, string):
        """Append string to content."""
        self.content += (
            u"{indent}{str}\n".format(indent=self.indent, str=str(string))
        )

    def render(self, file_out, ind=""):
        """Render the tag and strings in content."""
        output = (
            u"{indent}<{tag}>\n"
            "{indent}{content}"
            "{indent}</{tag}>"
            .format(indent=ind, tag=self.tag, content=self.content)
        )
        file_out.write(output)

"""
