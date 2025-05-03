# Purpose of file: Project main file.

from truth_table import TruthTable

if __name__ == "__main__":
    table = TruthTable("(¬(A^B)) ⇒ ¬A^¬B").generate_truth_table()
    for row in table: print(row)