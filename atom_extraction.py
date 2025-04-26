# Purpose of file: General utils. Currently just atom extraction, hence file name.

from typing import List
from expressions import *

# Takes in expression, provides sorted set of atoms
def extract_atoms(expression:Expression) -> List[dict]:
    atoms = set()

    def _check_node(expression:Expression) -> None:
        if isinstance(expression, Atom):
            atoms.add(expression.name)
        elif isinstance(expression, BinaryOperator):
            _check_node(expression.left)
            _check_node(expression.right)
        elif isinstance(expression, Not):
            _check_node(expression.right)
        else:
            raise TypeError("Expression type not recognized")
        
    _check_node(expression)
    return atoms
