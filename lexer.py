from typing import List
from tokens import *

    
_UNARY_OPERATORS = {
    '¬': TokenType.NOT
}

_BINARY_OPERATORS = {
    'v': TokenType.DISJUNCTION,
    '^': TokenType.CONJUNCTION,
    '⇒': TokenType.IMPLIES,
    '⇔': TokenType.BICONDITIONAL
}

# Takes string, returns list of Tokens. It lexers.
def lexer(statement:str) -> List[Token|Subexpression]:
    tokens:List[Token] = []
    stack:List[List[Token]] = []

    for i, char in enumerate(statement):
        if char in _UNARY_OPERATORS:
            tokens.append(Token(_UNARY_OPERATORS[char], char, i))
        elif char in _BINARY_OPERATORS:
            tokens.append(Token(_BINARY_OPERATORS[char], char, i))
        elif char.isalpha():
            tokens.append(Token(TokenType.ATOM, char, i))
        elif char == '(':
            stack.append((tokens, i))
            tokens = []
        elif char == ')':
            previous_tokens, position = stack.pop()
            subexpression = Subexpression(tokens, position)
            tokens = previous_tokens
            tokens.append(subexpression)

    return tokens
