from truth_table import TruthTable

# Test "A"
def test_A():
    assert TruthTable("A").get_table() == [{'A': 'T'}, {'A': 'F'}]

# Test OR
def test_A_or_B():
    assert TruthTable("AvB").get_table() == [{'A': 'T', 'B': 'T', 'AvB':'T'}, {'A': 'T', 'B': 'F', 'AvB':'T'}, 
                                            {'A': 'F', 'B': 'T', 'AvB':'T'}, {'A': 'F', 'B': 'F', 'AvB':'F'}]
    
# Test AND
def test_A_and_B():
    assert TruthTable("A^B").get_table() == [{'A': 'T', 'B': 'T', 'A^B':'T'}, {'A': 'T', 'B': 'F', 'A^B':'F'}, 
                                            {'A': 'F', 'B': 'T', 'A^B':'F'}, {'A': 'F', 'B': 'F', 'A^B':'F'}]

# Test NOT 
def test_not_A():
    assert TruthTable("¬A").get_table() == [{'A': 'T', '¬A': 'F'}, {'A': 'F', '¬A': 'T'}]

# Test IMPLIES
def test_A_implies_B():
    assert TruthTable("A⇒B").get_table() == [{'A': 'T', 'B': 'T', 'A⇒B':'T'}, {'A': 'T', 'B': 'F', 'A⇒B':'F'}, 
                                            {'A': 'F', 'B': 'T', 'A⇒B':'T'}, {'A': 'F', 'B': 'F', 'A⇒B':'T'}]
    
# Test BICONDITIONAL
def test_A_biconditional_B():
    assert TruthTable("A⇔B").get_table() == [{'A': 'T', 'B': 'T', 'A⇔B':'T'}, {'A': 'T', 'B': 'F', 'A⇔B':'F'}, 
                                            {'A': 'F', 'B': 'T', 'A⇔B':'F'}, {'A': 'F', 'B': 'F', 'A⇔B':'T'}]