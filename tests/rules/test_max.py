from validator.rules import Max
import pytest


def test_max_01():
    rule = Max(18)
    value_to_check = 23
    assert not rule.check(value_to_check)

    rule = Max(18)
    value_to_check = 13
    assert rule.check(value_to_check)


def test_max_02():
    rule = Max(-18)
    value_to_check = 0
    assert not rule.check(value_to_check)

    rule = Max(0)
    value_to_check = 100
    assert not rule.check(value_to_check)

    rule = Max(0)
    value_to_check = 100
    assert not rule.check(value_to_check)

    rule = Max(999)
    value_to_check = -999
    assert rule.check(value_to_check)


def test_max_03():
    rule = Max(10)
    value_to_check = 10
    assert rule.check(value_to_check)

    rule = Max(0)
    value_to_check = 0
    assert rule.check(value_to_check)

    rule = Max(-23)
    value_to_check = -23
    assert rule.check(value_to_check)


def test_max_bad():
    # zero arg
    with pytest.raises(TypeError):
        rule = Max()
        value_to_check = 0
        assert not rule.check(value_to_check)

    # many arg
    with pytest.raises(TypeError):
        rule = Max(5, 5, 5)
        value_to_check = 0
        assert not rule.check(value_to_check)

    # wrong type
    with pytest.raises(TypeError):
        rule = Max("5", "5")
        value_to_check = 0
        assert not rule.check(value_to_check)
