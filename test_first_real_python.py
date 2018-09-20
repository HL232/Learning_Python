def test_add_three():
    from first_real_python import add_three
    s = add_three(1, 2, 3)
    assert s == 6

def test_divide_three():
    from first_real_python import divide_three
    s = divide_three(9)
    assert s == 3.0