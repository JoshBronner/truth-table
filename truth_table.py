from itertools import product
from typing import List
from expressions import *
from tokens import *

class TruthTable:
    def __init__(self, input_statement:str):
        self._statement:List[Token|Subexpression] = self._tokenize(input_statement)
        self._table = self._create_table(self._statement)

    # FIXME Either values must be set to functions reference or dict must be changed to list (or removed entirely)
    _UNARY_OPERATORS = {
        '¬': Not
    }

    # FIXME Either values must be set to functions reference or dict must be changed to list (or removed entirely)
    _BINARY_OPERATORS = {
        'v': Disjunction,
        '^': Conjunction,
        '⇒': Implies,
        '⇔': Biconditional
    }
    
    # Takes in String statement, returns tokenized statement in list of dictionaries. Sublists are parenthesis
    def _tokenize(self, statement:str) -> List[Token|Subexpression]:
        tokens:List[Token] = []
        stack:List[List[Token]] = []

        for i, char in enumerate(statement):
            if char in self._UNARY_OPERATORS:
                tokens.append(Token(TokenType.UNARY, char, i))
            elif char in self._BINARY_OPERATORS:
                tokens.append(Token(TokenType.BINARY, char, i))
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

    # Takes in list of tokens (parsed statement), returns statement table
    # FIXME refactor
    def _create_table(self, tokens:List[Token|Subexpression]) -> List[dict[str:bool]]:
        truths:List[dict] = []

        
        truths.extend(self._extract_atoms(tokens))
    
    # Takes in list of tokens, returns all possible combinations of atomic truths in list of dicts
    def _extract_atoms(self, tokens:List[Token], atoms:List[str]=[]) -> List[dict]:
        for token in tokens:
            if token.type == TokenType.ATOM and token.value not in atoms:
                atoms.append(token.value)
            elif token.type == 'SUBEXPRESSION':
                self._extract_atoms(token.value, atoms)
        combinations = list(product([True, False], repeat=len(atoms)))
        atomic_truths = [dict(zip(atoms, combination)) for combination in combinations]
        return atomic_truths

    # Takes in a list of tokens, returns a list of expressions (dicts)
    # FIXME add functionality
    def _parse_expression(self, tokens:List[Token|Subexpression]) -> Expression:
        pass

    # Returns truth table
    # FIXME add functionality
    def get_table(self) -> List[dict[str:bool]]:
        pass 

