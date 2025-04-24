from expressions import *
from tokens import *
from typing import List

class ExpressionParser:

    def __init__(self, tokenized_expression:List[Token|Expression]):
        self._expression = tokenized_expression
        self._count = 0
        self.parsed_expression = self.parse_expression()

    # Moves to next token in tokens list
    def _advance(self) -> None:
        self._count += 1
    
    # Gets current token in token list
    def _current(self) -> Token|Subexpression|None:
        if self._count < len(self._expression):
            return self._expression[self._count]
        return None
    
    # Begins parsing of expression. Primary method of class.
    def parse_expression(self) -> Expression:
        return self._parse_biconditional()

    # Biconditional parser, for recursive descent. 
    def _parse_biconditional(self) -> Expression:
        expr = self._parse_implies()
        while self._current().type == TokenType.BICONDITIONAL:
            self._advance()
            right = self._parse_implies()
            expr = Biconditional(expr, right)
        return expr

    # Implies parser, for recursive descent.
    def _parse_implies(self) -> Expression:
        expr = self._parse_disjunction()
        if self._current().type == TokenType.IMPLIES:
            self._advance()
            right = self._parse_implies()
            expr = Implies(expr, right)
        return expr 

    # Disjunction parser, for recursive descent.
    def _parse_disjunction(self) -> Expression:
        expr = self._parse_conjunction()
        while self._current().type == TokenType.DISJUNCTION:
            self._advance()
            right = self._parse_conjunction()
            expr = Disjunction(expr, right)
        return expr

    # Conjunction parser, for recursive descent.
    def _parse_conjunction(self) -> Expression:
        expr = self._parse_not()
        while self._current().type == TokenType.CONJUNCTION:
            self._advance()
            right = self._parse_not()
            expr = Conjunction(expr, right)
        return expr

    # Not parser, for recursive descent.
    def _parse_not(self) -> Expression:
        if self._current().type == TokenType.NOT:
            self._advance()
            expr = self._parse_not()
            return Not(expr)
        else:
            return self._parse_base()
        
    # Subexpression and Atom parser, for recursive descent
    def _parse_base(self) -> Expression:
        if self._current().type == TokenType.SUBEXPRESSION:
            subparser = ExpressionParser(self._current().value)
            expr = subparser.parse_expression()
            self._advance()
        elif self._current().type == TokenType.ATOM:
            expr = Atom(self._current().value)
            self._advance()   
        else:
            raise SyntaxError("Invalid TokenType")     

        return expr