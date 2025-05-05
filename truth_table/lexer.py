'''

# Purpose of file: Get tokens from string input

from typing import List
from .tokens import *

    
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
    cont = False

    for i, char in enumerate(statement):
        if cont:
            cont = False
            continue
        elif char == '-' or char == '–':
            if i+1 < len(statement) and statement[i+1] == '>':
                cont = True
                stack[-1].append(Token(TokenType.IMPLIES, '⇒', i))
        elif char in _UNARY_OPERATORS:
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

'''

from typing import List, Tuple
from .tokens import *


OPERATORS = {
    '==': TokenType.BICONDITIONAL,
    '<>': TokenType.BICONDITIONAL,
    '⇔': TokenType.BICONDITIONAL,
    '⟺': TokenType.BICONDITIONAL,
    '<->': TokenType.BICONDITIONAL,
    '↔': TokenType.BICONDITIONAL,
    '⇒': TokenType.IMPLIES,
    '=>': TokenType.IMPLIES,
    '->': TokenType.IMPLIES,
    '→': TokenType.IMPLIES,
    '⊃': TokenType.IMPLIES,
    '>': TokenType.IMPLIES,
    '^': TokenType.CONJUNCTION,
    '∧': TokenType.CONJUNCTION,
    '&': TokenType.CONJUNCTION,
    '.': TokenType.CONJUNCTION,
    '·': TokenType.CONJUNCTION,
    '*': TokenType.CONJUNCTION,
    '¬': TokenType.NOT,
    '-': TokenType.NOT,
    '–': TokenType.NOT,
    '~': TokenType.NOT,
    '∼': TokenType.NOT,
    'v': TokenType.DISJUNCTION,
    '∨': TokenType.DISJUNCTION,
}

def match_operator(statement_fragment:str) -> Tuple[TokenType|None,int]:
    if statement_fragment in OPERATORS:
        return OPERATORS[statement_fragment], len(statement_fragment)
    elif len(statement_fragment) > 0:
        return match_operator(statement_fragment[:-1])
    return None, 0

def lexer(statement:str) -> List[Token|Subexpression]:
    i = 0
    stack: List[List[Token|Subexpression]] = [[]]
    while i < len(statement):
        if statement[i] == '(':
            stack.append([])
            i+=1
        elif statement[i] == ')':
            if len(stack) == 1:
                raise SyntaxError(f"Unmatched parentheses at point {i}")
            inner = stack.pop()
            subexpression = Subexpression(inner, i)
            stack[-1].append(subexpression)
            i+=1
        else:
            oper, l = match_operator(statement[i:i+3])
            if oper is not None:
                stack[-1].append(Token(oper, oper.value, i))
                i+=l
            elif statement[i].isalpha():
                stack[-1].append(Token(TokenType.ATOM, statement[i], i))
                i+=1
            else:
                print(f'Logging:\n char is "{statement[i]}"')
                i+=1
    if len(stack) != 1:
        raise SyntaxError("Unclosed Parentheses in Expression")
    
    return stack[0]
                

