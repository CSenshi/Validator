from validator.rules import Between
import pytest


def test_between_01():
    rule = Between(2, 18)
    value_to_check = 5
    assert rule.check(value_to_check)

    rule = Between(2, 18)
    value_to_check = 1
    assert not rule.check(value_to_check)

    rule = Between(2, 18)
    value_to_check = 19
    assert not rule.check(value_to_check)


def test_between_02():

    rule = Between(-15, 30)
    value_to_check = -15
    assert rule.check(value_to_check)

    rule = Between(-15, 30)
    value_to_check = 30
    assert rule.check(value_to_check)

    rule = Between(-15, 30)
    value_to_check = 0
    assert rule.check(value_to_check)


def test_between_03():
    rule = Between(5, 5)
    value_to_check = 5
    assert rule.check(value_to_check)

    rule = Between(5, 5)
    value_to_check = 0
    assert not rule.check(value_to_check)


# implement bad tests for between class
def test_between_bad():
    # zero arg
    with pytest.raises(TypeError):
        rule = Between()
        value_to_check = 0
        assert not rule.check(value_to_check)

    # 1 arg
    with pytest.raises(TypeError):
        rule = Between(5)
        value_to_check = 0
        assert not rule.check(value_to_check)

    with pytest.raises(TypeError):
        rule = Between(5, 5, 5)
        value_to_check = 0
        assert not rule.check(value_to_check)

    # wrong type
    with pytest.raises(TypeError):
        rule = Between("5", "5")
        value_to_check = 0
        assert not rule.check(value_to_check)
