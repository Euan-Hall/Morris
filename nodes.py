class Node:
    def __init__(self):
        self.childeren = []

class Text(Node):
    def __init__(self, text):
        self.text = text

class Element(Node):
    def __init__(self, ElementData):
        self.ElementData = ElementData
