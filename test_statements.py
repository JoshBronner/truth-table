from truth_table import truth_table

# Test "A"
def test_A():
    assert truth_table("A") == [{'A': 'T'}, {'A': 'F'}]

# Test "AvB"
# def test_AvB():
#     assert truth_table("A") == []