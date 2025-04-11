from nodes import Node
from enum import Enum
class Element(Node):
    """
    Element class (reperesnets HTML element, i.e. P, DIV)

    Variables:
    tag_name -> Type String
    attr -> Array of class Attributes; help(attr) for more.

    Inherits class Node.
    """
    def __init__(self, parent=None):
        self.namespace: str
        self.prefix: str
        self.localName: str
        self.attributes: list
        self.custom_element_state: CustomElementState = CustomElementState.UNDEFINED
        self.element_defenition: str
        
        super().__init__(parent)

        
class CustomElementState(Enum):
    UNDEFINED = "undefined"
    FAILED = "failed"
    UNCUSTOMIZED = "uncustomized"
    PRECUSTOMIZED = "precustomized"
    CUSTOM = "custom"