from validator.rules import Min
import pytest


def test_min_01():
    rule = Min(1)
    value_to_check = "min"
    assert rule.check(value_to_check)

    rule = Min(5)
    value_to_check = "min"
    assert not rule.check(value_to_check)


def test_min_02():
    rule = Min(1)
    value_to_check = 100
    assert rule.check(value_to_check)

    rule = Min(2)
    value_to_check = 100
    assert rule.check(value_to_check)

    rule = Min(3)
    value_to_check = 100
    assert rule.check(value_to_check)

    rule = Min(4)
    value_to_check = 100
    assert not rule.check(value_to_check)


def test_min_03():
    rule = Min(1)
    value_to_check = [1, 2, 3]
    assert rule.check(value_to_check)

    rule = Min(0)
    value_to_check = []
    assert rule.check(value_to_check)

    rule = Min(1)
    value_to_check = []
    assert not rule.check(value_to_check)


# implement bad tests for min class.
def test_min_bad():
    # zero arg
    with pytest.raises(TypeError):
        rule = min()
        value_to_check = 0
        assert not rule.check(value_to_check)

    # many arg
    with pytest.raises(AttributeError):
        rule = min(5, 5, 5)
        value_to_check = 0
        assert not rule.check(value_to_check)

    # wrong type
    with pytest.raises(AttributeError):
        rule = min("5", "5")
        value_to_check = 0
        assert not rule.check(value_to_check)
