from itertools import product
from typing import List, Optional
from expressions import *
from tokens import *

class TruthTable:
    def __init__(self, input_statement:str) -> None:
        self._statement:List[Token|Subexpression] = self._tokenize(input_statement)
        self._table = self._create_table(self._statement)

    # FIXME Either values must be set to functions reference or dict must be changed to list (or removed entirely)
    _UNARY_OPERATORS = {
        '¬': TokenType.NOT
    }

    # FIXME Either values must be set to functions reference or dict must be changed to list (or removed entirely)
    _BINARY_OPERATORS = {
        'v': TokenType.DISJUNCTION,
        '^': TokenType.CONJUNCTION,
        '⇒': TokenType.IMPLIES,
        '⇔': TokenType.BICONDITIONAL
    }
    
    # Takes in String statement, returns tokenized statement in list of dictionaries. Sublists are parenthesis
    def _tokenize(self, statement:str) -> List[Token|Subexpression]:
        tokens:List[Token] = []
        stack:List[List[Token]] = []

        for i, char in enumerate(statement):
            if char in self._UNARY_OPERATORS:
                tokens.append(Token(self._UNARY_OPERATORS[char], char, i))
            elif char in self._BINARY_OPERATORS:
                tokens.append(Token(self._BINARY_OPERATORS[char], char, i))
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
    
    # Takes in list of tokens, returns all possible combinations of atomic truths in list of dicts
    def _extract_atoms(self, tokens:List[Token], collected_atoms:Optional[List[str]]=None) -> List[dict]:
        if collected_atoms == None:
            collected_atoms = []
        for token in tokens:
            if token.type == TokenType.ATOM and token.value not in collected_atoms:
                collected_atoms.append(token.value)
            elif token.type == TokenType.SUBEXPRESSION:
                self._extract_atoms(token.value, collected_atoms)
        combinations = list(product([True, False], repeat=len(collected_atoms)))
        atomic_truths = [dict(zip(collected_atoms, combination)) for combination in combinations]
        return atomic_truths