from validator.rules import Max
import pytest


def test_max_01():
    rule = Max(2)
    value_to_check = "max"
    assert not rule.check(value_to_check)

    rule = Max(4)
    value_to_check = "max"
    assert rule.check(value_to_check)


def test_max_02():
    rule = Max(-18)
    value_to_check = "123456789"
    assert not rule.check(value_to_check)

    rule = Max(0)
    value_to_check = "123456789"
    assert not rule.check(value_to_check)

    rule = Max(20)
    value_to_check = "123456789"
    assert rule.check(value_to_check)

    rule = Max(9)
    value_to_check = "123456789"
    assert rule.check(value_to_check)


def test_max_03():
    rule = Max(10)
    value_to_check = [1, 2, 3, 4]
    assert rule.check(value_to_check)

    rule = Max(10)
    value_to_check = "qweasdzxc"
    assert rule.check(value_to_check)

    rule = Max(10)
    value_to_check = {1, 2, 3, 4, 5}
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
