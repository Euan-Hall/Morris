from nodes import Node
from typing import Optional
import Element
class Attributes(Node):
    def __init__(self, parent):
        self.namespace: Optional[str] = None
        self.prefix: Optional[str] = None
        self.localname: str
        self.value: str
        self.element: Optional[Element.Element] = None
        super().__init__(parent)