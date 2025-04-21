from itertools import product

# cool

# Working towards:
# (¬(A^B)) -> ¬A^¬B



def truth_table(input_statement:str):
    atoms = []
    statement = []
    
    for i, char in enumerate(input_statement):
        if char.isupper() and not char in atoms:
            atoms.append(char)
        
        if char == 'v':
            statement.append(['v', input_statement[i-1], input_statement[i+1]])

    combinations = list(product('TF', repeat=len(atoms)))
    atomic_truths = [dict(zip(atoms, combination)) for combination in combinations]

    table = atomic_truths

    return table
