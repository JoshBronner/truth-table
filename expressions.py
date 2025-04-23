# Abstract base class
class Expression:
    def evaluate(self, assignment) -> bool:
        raise NotImplementedError("Abstract class used")

# Abstract binary class   
class BinaryOperator(Expression):
    def __init__(self, left:Expression, right:Expression):
        self.left:Expression = left
        self.right:Expression = right
    def evaluate(self, assignment):
        raise NotImplementedError("Abstract class used")

class Atom(Expression):
    def __init__(self, name:str):
        self.name = name
    def evaluate(self, assignment) -> bool:
        return assignment[self.name]
    
class Not(Expression):
    def __init__(self, right:Expression):
        self.right = right
    def evaluate(self, assignment) -> bool:
        return not self.right.evaluate(assignment)
    
class Conjunction(BinaryOperator):
    def __init__(self, left, right):
        super().__init__(left, right)
    def evaluate(self, assignment):
        return self.left.evaluate(assignment) and self.right.evaluate(assignment)
    
class Disjunction(BinaryOperator):
    def __init__(self, left, right):
        super().__init__(left, right)
    def evaluate(self, assignment):
        return self.left.evaluate(assignment) or self.right.evaluate(assignment)

class Implies(BinaryOperator):
    def __init__(self, left, right):
        super().__init__(left, right)
    def evaluate(self, assignment):
        if self.left.evaluate(assignment) == False:
            return True
        elif self.right.evaluate(assignment) == True:
            return True
        return False

class Biconditional(BinaryOperator):
    def __init__(self, left, right):
        super().__init__(left, right)
    def evaluate(self, assignment):
        return self.left.evaluate(assignment) == self.right.evaluate(assignment)