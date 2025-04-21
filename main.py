from truth_table import TruthTable

# Working towards:
# (¬(A^B)) -> ¬A^¬B



if __name__ == "__main__":
    print('check')
    print(TruthTable("¬(AvB) ^ ¬B").getTable())