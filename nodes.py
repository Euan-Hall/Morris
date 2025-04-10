class Node:
    """
    Base class for DOM classes.

    Variables:
    Children
    """
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []

        # If this node has a parent and isn't present as a child in the list, add to list.
        if self.parent:
            if self not in self.parent.children:
                self.parent.addChild(self)

    def addChild(self, child):
        self.children.append(child)

    def generateDict(self):
        child = []

        # If this node has children, generate a dictionary
        if self.children:
            for c in self.children:
                temp =c.generateDict()
                child.append(temp)

        return {"Type" : type(self), 
                "Children" : child}

class Text(Node):
    def __init__(self, text, parent=None):
        self.text = text
        super().__init__(parent)

class Element(Node):
    """
    Element class (reperesnets HTML element, i.e. P, DIV)

    Variables:
    tag_name -> Type String
    attr -> Array of class Attributes; help(attr) for more.

    Inherits class Node.
    """
    def __init__(self, tag_name, attr, parent=None):
        self.tag_name = tag_name
        self.attr = [attr] # Hash of Attributes
        super().__init__(parent)


class Document(Node):
    def __init__(self, url="localhost", parent=None):
        self.url = url
        super().__init__(parent)


class Attr(Node):
    def __init__(self, parent, localname=None, name=None, value="", element=None):
        self.localname = localname 
        self.name = name
        self.value = str(value)
        self.element = element
        super().__init__(parent)



