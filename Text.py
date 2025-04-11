from nodes import Node

class Text(Node):
    def __init__(self, parent=None):
        self.text: str
        super().__init__(parent)

class CDATASection(Text):
    pass