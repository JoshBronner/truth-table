# Purpose of file: Contains classes for each expression type.


# Abstract base class
class Expression:
    def evaluate(self, assignment) -> bool:
        raise NotImplementedError("Abstract class used")

# Abstract binary class   
class BinaryOperator(Expression):
    def __init__(self, left:Expression, right:Expression):
        self.left:Expression = left
        self.right:Expression = right
        self.symbol = ''
    def __str__(self):
        if isinstance(self.left, (Atom, Not)) and isinstance(self.right, (Atom, Not)):
            return f"{self.left}{self.symbol}{self.right}"
        elif isinstance(self.left, (Atom, Not)):
            return f"{self.left}{self.symbol}({self.right})"
        elif isinstance(self.right, (Atom, Not)):
            return f"({self.left}){self.symbol}{self.right}"
        else:
            return f"({self.left}){self.symbol}({self.right})"
    def evaluate(self, assignment):
        raise NotImplementedError("Abstract class used")

class Atom(Expression):
    def __init__(self, name:str):
        self.name = name
        self.left = self.name
        self.right = self.name
    def __str__(self):
        return self.name
    def evaluate(self, assignment) -> bool:
        return assignment[self.name]
    
class Not(Expression):
    def __init__(self, right:Expression):
        self.right = right
    def __str__(self):
        if isinstance(self.right, Atom):
            return f'¬{self.right}'
        return f'¬{self.right}'
    def evaluate(self, assignment) -> bool:
        return not self.right.evaluate(assignment)
    
class Conjunction(BinaryOperator):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.symbol = '∧'
    def evaluate(self, assignment):
        return self.left.evaluate(assignment) and self.right.evaluate(assignment)
    
class Disjunction(BinaryOperator):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.symbol = '∨'
    def evaluate(self, assignment):
        return self.left.evaluate(assignment) or self.right.evaluate(assignment)

class Implies(BinaryOperator):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.symbol = '⇒'
    def evaluate(self, assignment):
        return not self.left.evaluate(assignment) or self.right.evaluate(assignment)

class Biconditional(BinaryOperator):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.symbol = '⇔'
    def evaluate(self, assignment):
        return self.left.evaluate(assignment) == self.right.evaluate(assignment)