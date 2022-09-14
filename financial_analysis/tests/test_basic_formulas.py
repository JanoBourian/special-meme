from basics.basic_formula import present_to_future

def test_present_to_future():
    assert present_to_future(100, 1, 0.1) == 110.00

def test_present_to_future_two():
    assert present_to_future(100, 10, 0.05) == 162.89