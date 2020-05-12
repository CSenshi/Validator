from validator.rules import Min


def test_min_01():
    rule = Min(18)
    value_to_check = 23
    assert rule(value_to_check)

    rule = Min(18)
    value_to_check = 13
    assert rule(value_to_check) == False


def test_min_02():
    rule = Min(-18)
    value_to_check = 0
    assert rule(value_to_check)

    rule = Min(0)
    value_to_check = 100
    assert rule(value_to_check)

    rule = Min(0)
    value_to_check = 100
    assert rule(value_to_check)

    rule = Min(999)
    value_to_check = -999
    assert rule(value_to_check) == False


def test_min_03():
    rule = Min(10)
    value_to_check = 10
    assert rule(value_to_check)

    rule = Min(0)
    value_to_check = 0
    assert rule(value_to_check)

    rule = Min(-23)
    value_to_check = -23
    assert rule(value_to_check)
