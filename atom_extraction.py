
from typing import List
from expressions import *

# Takes in expression, provides sorted set of atoms
def extract_atoms(expression:Expression) -> List[dict]:
    atoms = set()

    def _check_node(expression:Expression) -> None:
        if isinstance(expression, Atom):
            atoms.add(expression)
        elif isinstance(BinaryOperator):
            _check_node(expression.left)
            _check_node(expression.right)
        elif isinstance(Not):
            _check_node(expression.right)
        else:
            raise TypeError("Expression type not recognized")
        
    _check_node(expression)
    return sorted(atoms)
