# Purpose of file: Take a tokenized list and create an expression for it.

from .expressions import *
from .tokens import *
from typing import List

class ExpressionParser:

    def __init__(self, tokenized_expression:List[Token|Expression]):
        self._expression = tokenized_expression
        self._count = 0
        self.parsed_expression = self.parse_expression()

    # Moves to next token in tokens list
    def _advance(self) -> None:
        self._count += 1
    
    # Gets match token in token list, returns boolean. Consumes current token if it exists.
    def _match(self, expected:TokenType) -> bool:
        if self._count >= len(self._expression):
            return False
        if self._expression[self._count].type == expected:
            self._advance()
            return True
        return False
    
    # Checks current token
    def _peek(self) -> Token|None:
        if self._count < len(self._expression):
            return self._expression[self._count]
        return None
    
    # Begins parsing of expression. Primary method of class.
    def parse_expression(self) -> Expression:
        expr = self._parse_biconditional()
        if self._count < len(self._expression):
            raise SyntaxError(f"Unexpected token after expression end")
        return expr

    # Biconditional parser, for recursive descent. 
    def _parse_biconditional(self) -> Expression:
        expr = self._parse_implies()
        while self._match(TokenType.BICONDITIONAL):
            right = self._parse_implies()
            expr = Biconditional(expr, right)
        return expr

    # Implies parser, for recursive descent.
    def _parse_implies(self) -> Expression:
        expr = self._parse_disjunction()
        if self._match(TokenType.IMPLIES):
            right = self._parse_implies()
            expr = Implies(expr, right)
        return expr 

    # Disjunction parser, for recursive descent.
    def _parse_disjunction(self) -> Expression:
        expr = self._parse_conjunction()
        while self._match(TokenType.DISJUNCTION):
            right = self._parse_conjunction()
            expr = Disjunction(expr, right)
        return expr

    # Conjunction parser, for recursive descent.
    def _parse_conjunction(self) -> Expression:
        expr = self._parse_not()
        while self._match(TokenType.CONJUNCTION):
            right = self._parse_not()
            expr = Conjunction(expr, right)
        return expr

    # Not parser, for recursive descent.
    def _parse_not(self) -> Expression:
        if self._match(TokenType.NOT):
            expr = self._parse_not()
            return Not(expr)
        else:
            return self._parse_base()
        
    # Subexpression and Atom parser, for recursive descent
    def _parse_base(self) -> Expression:
        token = self._peek()
        if token is None:
            raise SyntaxError("Unexpected end to expression")
        if token.type == TokenType.SUBEXPRESSION:
            subex = token.value
            self._advance()
            subparser = ExpressionParser(subex)
            expr = subparser.parsed_expression
        elif token.type == TokenType.ATOM:
            atom = token.value
            self._advance()
            expr = Atom(atom)
        else:
            raise SyntaxError(f"Unexpected Token {token.type} at position {self._count}")
        return expr