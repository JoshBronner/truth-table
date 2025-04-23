from enum import Enum, auto
from typing import List

class TokenType(Enum):
    ATOM = auto()
    UNARY = auto()
    BINARY = auto()
    SUBEXPRESSION = auto()

class Token:
    def __init__(self, type:TokenType, value:str, position:int):
        self.type = type
        self.value = value
        self.position = position
    
    def __repr__(self):
        return f"{self.type} TOKEN: {self.value} at position {self.position}"

class Subexpression:
    def __init__(self, value:List[Token], position:int):
        self.value = value
        self.position = position

    def __repr__(self):
        return f"SUBEXPRESSION - {self.value}, {self.position}"