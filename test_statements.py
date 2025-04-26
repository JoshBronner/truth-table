# Purpose of file: Testing. Currently broken due to dict order inconsistency.

from truth_table import TruthTable

# Test "A"
def test_A():
    assert TruthTable("A").generate_truth_table() == [{'A': True}, {'A': False}]

# Test OR
def test_A_or_B():
    assert ((TruthTable("AvB").generate_truth_table())) == [{'A': True, 'B': True, 'A∨B':True}, {'A': True, 'B': False, 'A∨B':True}, 
                                            {'A': False, 'B': True, 'A∨B':True}, {'A': False, 'B': False, 'A∨B':False}]
    
# Test AND
def test_A_and_B():
    assert TruthTable("A^B").generate_truth_table() == [{'A': True, 'B': True, 'A∧B':True}, {'A': True, 'B': False, 'A∧B':False}, 
                                            {'A': False, 'B': True, 'A∧B':False}, {'A': False, 'B': False, 'A∧B':False}]

# Test NOT 
def test_not_A():
    assert TruthTable("¬A").generate_truth_table() == [{'A': True, '¬A': False}, {'A': False, '¬A': True}]
# Test IMPLIES
def test_A_implies_B():
    assert TruthTable("A⇒B").generate_truth_table() == [{'A': True, 'B': True, 'A⇒B':True}, {'A': True, 'B': False, 'A⇒B':False}, 
                                            {'A': False, 'B': True, 'A⇒B':True}, {'A': False, 'B': False, 'A⇒B':True}]
    
# Test BICONDITIONAL
def test_A_biconditional_B():
    assert TruthTable("A⇔B").generate_truth_table() == [{'A': True, 'B': True, 'A⇔B':True}, {'A': True, 'B': False, 'A⇔B':False}, 
                                            {'A': False, 'B': True, 'A⇔B':False}, {'A': False, 'B': False, 'A⇔B':True}]

# Test Combinations

def test_not_A_and_B_or_A_implies_not_B():
    assert TruthTable("(¬A^B)v(A⇒¬B)").generate_truth_table() == [{'A': True, 'B': True, '¬A∧B∨A⇒¬B':False}, {'A': True, 'B': False, '¬A∧B∨A⇒¬B':True}, 
                                                                  {'A': False, 'B': True, '¬A∧B∨A⇒¬B':True}, {'A': False, 'B': False, '¬A∧B∨A⇒¬B':True}]


def test_A_implies_B_implies_C():
    assert TruthTable("A⇒B⇒C").generate_truth_table() ==  [{'C': True, 'B': True, 'A': True, 'A⇒B⇒C': True},
                                                          {'C': True, 'B': True, 'A': False, 'A⇒B⇒C': True},
                                                          {'C': True, 'B': False, 'A': True, 'A⇒B⇒C': True},
                                                          {'C': True, 'B': False, 'A': False, 'A⇒B⇒C': True},
                                                          {'C': False, 'B': True, 'A': True, 'A⇒B⇒C': False},
                                                          {'C': False, 'B': True, 'A': False, 'A⇒B⇒C': True},
                                                          {'C': False, 'B': False, 'A': True, 'A⇒B⇒C': True},
                                                          {'C': False, 'B': False, 'A': False, 'A⇒B⇒C': True}]