import pytest
from truth_table import TruthTable

# Test "A"
def test_A():
    assert TruthTable("A").get_table() == [{'A': 'T'}, {'A': 'F'}]

# Test "AvB"
def test_AvB():
    assert TruthTable("AvB").get_table() == [{'A': 'T', 'B': 'T', 'AvB':'T'}, {'A': 'T', 'B': 'F', 'AvB':'T'}, 
                                            {'A': 'F', 'B': 'T', 'AvB':'T'}, {'A': 'F', 'B': 'F', 'AvB':'F'}]