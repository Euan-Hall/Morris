from typing import Optional 
from enum import Enum

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
        self.parentElement: Optional[Element] = None
        self.children = []

    def getNodeType(self):
        match self:
            case Element():
                return self.ELEMENT_NODE
            
            case Attributes():
                return self.ATTRIBUTE_NODE
            
            case Text():
                return self.TEXT_NODE
            
            case CDATASection():
                return self.CDATA_SECTION_NODE
            
            case "B":
                return self.ENTITY_REFERENCE_NODE
            
            case "A":
                return self.ENTITY_NODE
            
            case ProcessingInstruction():
                return self.PROCESSING_INTSTRUCTION_NODE
            
            case Comment():
                return self.COMMENT_NODE
            
            case Document():
                return self.DOCUMENT_NODE
            
            case DocumentType():
                return self.DOCUMENT_TYPE_NODE
            
            case DocumentFragment():
                return self.DOCUMENT_FRAGMENT_NODE
            
            case _: # Notation Node?
                raise LookupError(f"Unknown Error whlie matching type: {self}, {type(self)}.")
            
    def getBaseURL(self):
        pass # Sort out later
            
    def getNodeName(self):
        qualifiedName = ""
        match self:
            case Element():
                if self.namespace == None:
                    qualifiedName = self.localName
                else:
                    qualifiedName = f"{self.namespace}:{self.localName}" 
                
                doc = self.getOwnerDocument() # Need to check namespace is HTML?
                if doc and doc.type == 1:
                    qualifiedName = qualifiedName.upper
                return qualifiedName
            case Attributes():
                if self.namespace == None:
                    return self.localName
                return f"{self.namespace}:{self.localname}"
            
            case Text():
                return "#text"
            
            case CDATASection():
                return "#cdata-section" 
            
            case ProcessingInstruction():
                return self.target
            
            case Comment():
                return "#comment"
            
            case Document():
                return "#document"
            
            case DocumentType():
                return self.name
            
            case DocumentFragment():
                return "#document-fragment"
            
            case _:
                raise LookupError(f"Unknown Error whlie matching type: {self}, {type(self)}.")

    def getParentElement(self):
        return self.parentElement
    
    def hasChildren(self):
        return self.children is not None
    
    def getChildNodes(self):
        if self.hasChildren(self):
            return self.children
        return None
    
    def getFirstChild(self):
        if self.hasChildren():
            return self.children[0]
        return None
    
    def getLastChild(self):
        if self.hasChildren:
            return self.children[-1]
        return None
    
    def getNextSibling(self):
        if self.parentNode:
            # Check position in child list
            idx = self.parentNode.children.index(self)
            length = len(self.parentNode.children)
            if length > 1 and idx != length - 1:
                return self.parentNode.children[idx+1]
        return None

    def getPreviousSibling(self):
        if self.parentNode:
            # Check position in child list
            idx = self.parentNode.children.index(self)
            if idx != 0:
                return self.parentNode.children[idx-1]
        return None
    
    def isConnected(self):
        pass

    def getRootNode(self, options=None):
        """Return this’s shadow-including root if options["composed"] is true; otherwise this’s root."""
        if options == "composed": # Implement Options properly
            return None
        
        curr_node = self
        while curr_node.parentNode:
            curr_node = curr_node.parentNode
        return curr_node

    def isConnected(self):
        """A node is connected if its shadow-including root is a document."""
        pass

    def getOwnerDocument(self):
        """Return null, if this is a document; otherwise this’s node document."""
        if self.getNodeType() == self.DOCUMENT_NODE:
            return None
        return self.node_document 
    
    def getNodeValue(self):
        match self:
            case Attributes():
                return self.value
            
            case CharacterData():
                return self.data
            
            case _:
                return None

    def setNodeValue(self, value):
        match self:
            case Attributes():
                if self.element:
                    self.value = value
                else:
                    #To change an attribute attribute to value, run these steps:
                    # Let oldValue be attribute’s value.
                    oldValue = self.value

                    # Set attribute’s value to value.
                    self.value = value

                    # Handle attribute changes for attribute with attribute’s element, oldValue, and value.

                    # To handle attribute changes for an attribute attribute with element, oldValue, and newValue, run these steps:
                    # Queue a mutation record of "attributes" for element with attribute’s local name, attribute’s namespace, oldValue, « », « », null, and null.
                    # If element is custom, then enqueue a custom element callback reaction with element, callback name "attributeChangedCallback", and « attribute’s local name, oldValue, newValue, attribute’s namespace ».
                    # Run the attribute change steps with element, attribute’s local name, oldValue, newValue, and attribute’s namespace.
            
            case CharacterData():
                self.replaceData()    # Finish making this
            
            case _:
                 pass

    def getTextContext(self):
        match self:
            case Element():
                # Concatenate all values of the text nodes of self's children.
                # Must be in the order of the tree
                # Depth first search, pre-order searching for all text nodes. This only does one level.
                out = ""
                if self.children:
                    textNodes = list(filter(lambda x: type(x)==Text(), self.children))
                    for c in textNodes:
                        out += c.text
                return out
            
            case Attributes():
                return self.value
            
            case CharacterData():
                return self.data
            case _:
                return None

class Document(Node):    
    def __init__(self):
        self.encoding = "utf-8"
        self.content_type = "application/xml"
        self.url = "about:blank"
        self.origin: str # Change to type Origin once implemented 
        self.type = 0 # xml or html (0 or 1?)
        self.mode = "no-quirks" # "no-quirks", "quirks", or "limited-quirks"
        self.allow_declatative_shadow_roots = False


class DocumentType(Node):
    def __init__(self):
        self.name: str
        self.public_id: str
        self.sys_id: str

    @property
    def getName(self):
        return self.name
    
    @property
    def getPublicId(self):
        return self.public_id
    
    @property
    def getSystemId(self):
        return self.sys_id
    

class DocumentFragment(Node):
    def __init__(self):
        self.host: Optional[Element] = None


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

class Attributes(Node):
    def __init__(self, parent):
        self.namespace: Optional[str] = None
        self.prefix: Optional[str] = None
        self.localname: str
        self.value: str
        self.element: Optional[Element.Element] = None
        super().__init__(parent)


class ShadowRoot(DocumentFragment):
    def __init__(self):
        host: Element
        if host is None:
            raise ValueError("ShadowRoot must be associated with a non-null host.")
        
        self.mode: ShadowRootMode = ShadowRootMode.open
        self.delegatesFocus: bool = False
        self.slotAssignment: SlotAssignmentMode
        self.clonable: bool = False
        self.serialize: bool = False
        self.host: Element = host

 
class ShadowRootMode(Enum):
    open = "open"
    closed = "closed"

class SlotAssignmentMode(Enum):
    manual = "manual"
    named = "named"


class Text(Node):
    def __init__(self, parent=None):
        self.text: str
        super().__init__(parent)

class CDATASection(Text):
    pass


class CharacterData(Node):
    def __init__(self):
        self.data: str
        self.length: int

    def replaceData(self, offset: int, count: int, data: str):
        if offset > self.length:
            raise IndexError(f"Offset too large for current CharacterData Node: {self}")
        
        if offset + count > self.length:
            count = offset - self.length

        # so on so forth...



class Comment(CharacterData):
    def __init__(self):
        self.data: Optional[str] = None

class ProcessingInstruction(CharacterData):
    def __init__(self):
        self.target: str