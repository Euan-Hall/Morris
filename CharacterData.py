from nodes import Node
from typing import Optional

class CharacterData(Node):
    def __init__(self):
        self.data: str

class Comment(CharacterData):
    def __init__(self):
        self.data: Optional[str] = None

class ProcessingInstruction(CharacterData):
    def __init__(self):
        self.target: str