from itertools import product

# cool

# Working towards:
# (¬(A^B)) -> ¬A^¬B

class TruthTable():
    
    def __init__(self, input_statement:str):
        self._SYMBOLS = {'v': self._eval_or,
                         '^': self._eval_and,
                         '¬': self._eval_nor,
                         '⇒': self._eval_implies,
                         '⇔': self._eval_biconditional}
        
        self._input_statement = input_statement
        self._atoms = []
        self._statements = []
        self._atomic_truths = []
        self._table = []
        self._parse_input()
        
    def _parse_input(self):
        for i, char in enumerate(self._input_statement):
            if char.isupper() and not char in self._atoms:
                self._atoms.append(char)
            
            if char in self._SYMBOLS:
                self._statements.append([char, self._input_statement[i-1], self._input_statement[i+1]])

        combinations = list(product('TF', repeat=len(self._atoms)))
        self._atomic_truths = [dict(zip(self._atoms, combination)) for combination in combinations]

        self._table = self._atomic_truths

        for char in self._statements:
            if char[0] in self._SYMBOLS:
                if char[1] in self._table[0] and char[2] in self._table[0]:
                    self._SYMBOLS[char[0]](char[1], char[2])

    def get_table(self):
        return self._table
    
    def _eval_or(self, left:str, right:str):
        for combination in self._table:
            if combination[left] == 'T' or combination[right] == 'T':
                combination[f'{left}v{right}'] = 'T'
            else:
                combination[f'{left}v{right}'] = 'F'
    
    def _eval_and(self, left:str, right:str):
        for combination in self._table:
            if combination[left] == 'T' and combination[right] == 'T':
                combination[f'{left}^{right}'] = 'T'
            else:
                combination[f'{left}^{right}'] = 'F'

    def _eval_nor(self, left:str, right:str):
        for combination in self._table:
            if combination[right] == 'T':
                combination[f'¬{right}'] = 'F'
            else:
                combination[f'¬{right}'] = 'T'

    def _eval_implies(self, left:str, right:str):
        for combination in self._table:
            if combination[left] == 'F':
                combination[f'{left}⇒{right}'] = 'T'
            elif combination[left] == 'T' and combination[right] =='T':
                combination[f'{left}⇒{right}'] = 'T'
            else:
                combination[f'{left}⇒{right}'] = 'F'
    
    def _eval_biconditional(self, left:str, right:str):
        for combination in self._table:
            if combination[left] == combination[right]:
                combination[f'{left}⇔{right}'] = 'T'
            else:
                combination[f'{left}⇔{right}'] = 'F'