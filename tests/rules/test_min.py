from validator.rules import Min
import pytest


def test_min_01():
    rule = Min(18)
    value_to_check = 23
    assert rule.check(value_to_check)

    rule = Min(18)
    value_to_check = 13
    assert not rule.check(value_to_check)


def test_min_02():
    rule = Min(-18)
    value_to_check = 0
    assert rule.check(value_to_check)

    rule = Min(0)
    value_to_check = 100
    assert rule.check(value_to_check)

    rule = Min(0)
    value_to_check = 100
    assert rule.check(value_to_check)

    rule = Min(999)
    value_to_check = -999
    assert not rule.check(value_to_check)


def test_min_03():
    rule = Min(10)
    value_to_check = 10
    assert rule.check(value_to_check)

    rule = Min(0)
    value_to_check = 0
    assert rule.check(value_to_check)

    rule = Min(-23)
    value_to_check = -23
    assert rule.check(value_to_check)


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
