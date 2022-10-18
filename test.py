from sum_nuemros import sum_number

def test_sum_numbers_default():
    """Test that the default value is a list"""
    assert sum_number() == 5050
    assert sum_number(numbers=None) == 5050
    

def test_sum_numbers_with_list():
    assert sum_number([1, 2, 3]) == 6
