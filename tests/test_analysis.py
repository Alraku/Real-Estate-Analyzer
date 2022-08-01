from source.analysis import average

def test_average():
    values = [10, 8, 12]
    given = average(values)
    assert given == 10, f"Average value is not valid, given {given}, but should be 10!"