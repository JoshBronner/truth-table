from itertools import product

class TruthTable():
    
    def __init__(self, input_statement:str):
        self._SYMBOLS = {'v': self._eval_or,
                         '^': self._eval_and,
                         '¬': self._eval_not,
                         '⇒': self._eval_implies,
                         '⇔': self._eval_biconditional}
        
        self._input_statement = input_statement
        self._atoms = []
        self._statements = []
        self._atomic_truths = []
        self._table = []
        self._parse_input()
        
    def _parse_input(self):   
        self._extract_atoms()
        self._extract_conditions()
        self._generate_atomic_combinations()
        self._generate_statements()

    def _generate_statements(self):
        for char in self._statements:
            if char[0] in self._SYMBOLS:
                if char[1] in self._table[0] and char[2] in self._table[0]:
                    self._evaluate_statement(char[0], char[1], char[2])

    def _extract_atoms(self):
            for char in self._input_statement:
                if char.isupper() and not char in self._atoms:
                    self._atoms.append(char)
    
    def _extract_conditions(self):
        for i, char in enumerate(self._input_statement):
            if char in self._SYMBOLS:
                self._statements.append([char, self._input_statement[i-1], self._input_statement[i+1]])

    def _generate_atomic_combinations(self):
        combinations = list(product([True, False], repeat=len(self._atoms)))
        self._atomic_truths = [dict(zip(self._atoms, combination)) for combination in combinations]
        self._table = self._atomic_truths
    
    def get_table(self):
        return self._table
    
    def _evaluate_statement(self, operator:str, left:str, right:str):
        for combination in self._table:
            if self._SYMBOLS[operator] == self._eval_not:
                combination[f'{operator}{right}'] = True if combination[right] == False else False
            elif self._SYMBOLS[operator](combination[left], combination[right]):
                combination[f'{left}{operator}{right}'] = True
            else:
                combination[f'{left}{operator}{right}'] = False

    def _eval_or(self, left:str, right:str):
        if left == True or right == True:
            return True
        return False
    
    def _eval_and(self, left:str, right:str):
        if left == True and right == True:
            return True
        return False

    def _eval_not(self, left:str, right:str):
        return not right

    def _eval_implies(self, left:str, right:str):
        if left == False or right == True:
            return True
        return False
    
    def _eval_biconditional(self, left:str, right:str):
        if left == right:
            return True
        return False