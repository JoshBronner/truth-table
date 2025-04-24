from enum import Enum, auto
from typing import List

class TokenType(Enum):
    ATOM = auto()
    SUBEXPRESSION = auto()

    NOT = auto()
    BICONDITIONAL = auto()
    IMPLIES = auto()
    CONJUNCTION = auto()
    DISJUNCTION = auto()

class Token:
    def __init__(self, type:TokenType, value:str, position:int):
        self.type = type
        self.value = value
        self.position = position
    
    def __repr__(self):
        return f"{self.type} TOKEN: {self.value} at position {self.position}"

class Subexpression(Token):
    def __init__(self, value:List[Token], position:int):
        super().__init__(TokenType.SUBEXPRESSION, value, position)

    def __repr__(self):
        return super().__repr__()