from Document import Document
from Element import Element
from typing import Optional 

class Node:
    """
    Base class for DOM classes.

    Variables:
    Children
    """
    def __init__(self, parent=None):
        self.ELEMENT_NODE: int = 1
        self.ATTRIBUTE_NODE: int = 2
        self.TEXT_NODE: int = 3
        self.CDATA_SECTION_NODE: int = 4
        self.ENTITY_REFERENCE_NODE: int = 5 # Not done?
        self.ENTITY_NODE: int = 6 # Not done?
        self.PROCESSING_INTSTRUCTION_NODE: int = 7
        self.COMMENT_NODE: int = 8
        self.DOCUMENT_NODE: int = 9
        self.DOCUMENT_TYPE_NODE: int = 10
        self.DOCUMENT_FRAGMENT_NODE: int = 11
        self.NOTATION_NODE: int = 12
        self.nodeType: int
        self.nodeName: str

        self.node_document: Optional[Document] = None

        self.parentNode: Optional[Node] = None
        self.parentEleent: Optional[Element] = None
        self.children = []

    def hasChildren(self):
        return self.children is not None
    
    def getFirstChild(self):
        return self.children[0]
    
    def getLastChild(self):
        return self.children[-1]
    
    def getNextSibling(self):
        pass

    def getPreviousSibling(self):
        pass
    
    def isConnected(self):
        pass

    def getRootNode(self):
        # Keep going through parent's until parent is None. Then return current node.
        pass
    



