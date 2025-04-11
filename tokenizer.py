import parser
import nodes
from enum import Enum
from dataclasses import dataclass


class Tokenizer(Enum):
    def __init__(self):
        DOCTYPE = 1
        start_tag = 2
        end_tag = 3
        comment = 4
        character = 5 
        EOF = 6

@dataclass
class t_doctype:
    name: str
    public_id: str
    sys_id: str
    force_quirks_flag: bool


@dataclass
class t_tag:
    name: str
    self_closing: bool
    attributes: list

@dataclass
class t_comment_or_character:
    data: str
    