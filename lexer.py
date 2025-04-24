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
    stack: List[List[Token|Subexpression]] = [[]]

    for i, char in enumerate(statement):
        if char in _UNARY_OPERATORS:
            stack[-1].append(Token(_UNARY_OPERATORS[char], char, i))
        elif char in _BINARY_OPERATORS:
            stack[-1].append(Token(_BINARY_OPERATORS[char], char, i))
        elif char.isalpha():
            stack[-1].append(Token(TokenType.ATOM, char, i))
        elif char == '(':
            stack.append([])
        elif char == ')':
            if len(stack) == 1:
                raise SyntaxError(f"Unmatched parentheses at point {i}")
            inner = stack.pop()
            subexpression = Subexpression(inner, i)
            stack[-1].append(subexpression)

    if len(stack) != 1:
        raise SyntaxError("Unclosed parentheses in expression")

    return stack[0]