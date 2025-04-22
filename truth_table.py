from itertools import product

class TruthTable():
    
    def __init__(self, input_statement:str):
        self._SYMBOLS = {'v': self._eval_or,
                         '^': self._eval_and,
                         '¬': self._eval_not,
                         '⇒': self._eval_implies,
                         '⇔': self._eval_biconditional}
        
        self._atoms = []
        self._input_statement = self._tokenize_statement(input_statement)
        self._statements = []
        self._table = self._generate_atomic_combinations()
        self._parse_input()
        
    # Unclear
    def _parse_input(self):  
        self._extract_conditions()
        self._generate_statements()

    # Takes original user statement, creates list of tokens as dicts
    def _tokenize_statement(self, original_statement): 
        new_statement = []
        for i, char in enumerate(original_statement):
            if char in self._SYMBOLS:
                new_statement.append({'type':'SYMBOL','value':char, 'position':i})
            elif char.isalpha():
                new_statement.append({'type':'ATOM', 'value':char, 'position':i})
                if char not in self._atoms:
                    self._atoms.append(char)
            elif char == '(':
                new_statement.append({'type':'LEFT_PAREN', 'value':char, 'position':i})
            elif char == ')':
                new_statement.append({'type':'RIGHT_PAREN', 'value':char, 'position':i})
        return new_statement

    # Populates self._statements
    def _extract_conditions(self):
        for i, char in enumerate(self._input_statement):
            if char['type'] == 'SYMBOL':
                self._statements.append([char['value'], self._input_statement[i-1]['value'], self._input_statement[i+1]['value']])

    # Creates True/False table for atoms
    def _generate_atomic_combinations(self):
        combinations = list(product([True, False], repeat=len(self._atoms)))
        _atomic_truths = [dict(zip(self._atoms, combination)) for combination in combinations]
        return _atomic_truths
    
    # Evaluates each statement in self._statements
    def _generate_statements(self):
        for char in self._statements:
            self._evaluate_statement(char[0], char[1], char[2])
    
    # Returns unformatted table. Primarily for testing.
    def get_table(self):
        return self._table
    
    # Evaluates statements
    def _evaluate_statement(self, operator:str, left:str, right:str):
        for combination in self._table:
            if self._SYMBOLS[operator] == self._eval_not:
                combination[f'{operator}{right}'] = True if combination[right] == False else False
            elif self._SYMBOLS[operator](combination[left], combination[right]):
                combination[f'{left}{operator}{right}'] = True
            else:
                combination[f'{left}{operator}{right}'] = False

    def _eval_or(self, left:str, right:str):
        return left or right
    
    def _eval_and(self, left:str, right:str):
        return left and right

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
    
print(TruthTable("QvU").get_table())