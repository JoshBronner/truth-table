from truth_table import TruthTable

# Test "A"
def test_A():
    assert TruthTable("A").get_table() == [{'A': True}, {'A': False}]

# Test OR
def test_A_or_B():
    assert TruthTable("AvB").get_table() == [{'A': True, 'B': True, 'AvB':True}, {'A': True, 'B': False, 'AvB':True}, 
                                            {'A': False, 'B': True, 'AvB':True}, {'A': False, 'B': False, 'AvB':False}]
    
# Test AND
def test_A_and_B():
    assert TruthTable("A^B").get_table() == [{'A': True, 'B': True, 'A^B':True}, {'A': True, 'B': False, 'A^B':False}, 
                                            {'A': False, 'B': True, 'A^B':False}, {'A': False, 'B': False, 'A^B':False}]

# Test NOT 
def test_not_A():
    assert TruthTable("¬A").get_table() == [{'A': True, '¬A': False}, {'A': False, '¬A': True}]

# Test IMPLIES
def test_A_implies_B():
    assert TruthTable("A⇒B").get_table() == [{'A': True, 'B': True, 'A⇒B':True}, {'A': True, 'B': False, 'A⇒B':False}, 
                                            {'A': False, 'B': True, 'A⇒B':True}, {'A': False, 'B': False, 'A⇒B':True}]
    
# Test BICONDITIONAL
def test_A_biconditional_B():
    assert TruthTable("A⇔B").get_table() == [{'A': True, 'B': True, 'A⇔B':True}, {'A': True, 'B': False, 'A⇔B':False}, 
                                            {'A': False, 'B': True, 'A⇔B':False}, {'A': False, 'B': False, 'A⇔B':True}]