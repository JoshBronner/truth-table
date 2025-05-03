# Purpose of file: Generate truth table

from itertools import product
from typing import List
from .expressions import *
from .tokens import *
from .expression_parser import ExpressionParser
from .lexer import lexer
from .atom_extraction import extract_atoms

class TruthTable:
    def __init__(self, input_statement:str) -> None:
        self._tokens = lexer(input_statement)
        self._expression = ExpressionParser(self._tokens).parsed_expression
        self._atoms = extract_atoms(self._expression)
        self._combinations = list(product([True, False], repeat=len(self._atoms)))
        self._assignments = [dict(zip(self._atoms, combination)) for combination in self._combinations]
        
        self.truth_table = self.generate_truth_table()


    def generate_truth_table(self) -> List[dict[str:bool]]:
        table = []

        for assignment in self._assignments:
            eval_case = self._expression.evaluate(assignment)
            row = {**assignment, str(self._expression):eval_case}
            table.append(row)

        return table