from nodes import Node
from typing import Optional
from Element import Element
class Document(Node):    
    def __init__(self):
        self.encoding = "utf-8"
        self.content_type = "application/xml"
        self.url = "about:blank"
        self.origin: str # Change to type Origin once implemented 
        self.type = 0 # xml or html (0 or 1?)
        self.mode = "no-quirks" # "no-quirks", "quirks", or "limited-quirks"
        self.allow_declatative_shadow_roots = False


class DocuentType(Node):
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
