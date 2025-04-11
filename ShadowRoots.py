from nodes import Node
from typing import Optional
from enum import Enum
from Element import Element

class ShadowRoot(Node):
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