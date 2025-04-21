from itertools import product

# cool

# Working towards:
# (¬(A^B)) -> ¬A^¬B

class TruthTable():
    def __init__(self, input_statement:str):
        self.atoms = []
        statements = []
        
        for i, char in enumerate(input_statement):
            if char.isupper() and not char in self.atoms:
                self.atoms.append(char)
            
            if char == 'v':
                statements.append(['v', input_statement[i-1], input_statement[i+1]])

        combinations = list(product('TF', repeat=len(self.atoms)))
        atomic_truths = [dict(zip(self.atoms, combination)) for combination in combinations]

        self.table = atomic_truths

    def getTable(self):
        return self.table