from truth_table import TruthTable

# Test "A"
def test_A():
    assert TruthTable("A").getTable() == [{'A': 'T'}, {'A': 'F'}]

# Test "AvB"
# def test_AvB():
#     assert truth_table("A") == []