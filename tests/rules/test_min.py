from validator.rules import Min
from validator.rules import Integer
from validator.rules import List
from validator.rule_pipe_validator import RulePipeValidator as RPV
import pytest


def test_min_01():
    assert Min(1).check("min")

    assert not Min(5).check("min")


def test_min_02():
    assert Min(1).check(100)

    assert Min(2).check(100)

    assert Min(3).check(100)

    assert not Min(4).check(100)


def test_min_03():
    assert Min(1).check([1, 2, 3])

    assert Min(0).check([])

    assert not Min(1).check([])


def test_min_04_rpv():
    rpv = RPV(1000, [Integer(), Min(10)])
    assert rpv.execute()

    rpv = RPV(0, [Integer(), Min(-10)])
    assert rpv.execute()

    rpv = RPV(18, [Integer(), Min(18)])
    assert rpv.execute()

    rpv = RPV(0, [Integer(), Min(0)])
    assert rpv.execute()

    rpv = RPV([1, 2, 3], [List(), Min(2)])
    assert rpv.execute()

    rpv = RPV([], [List(), Min(-1)])
    assert rpv.execute()


def test_min_05_rpv():
    rpv = RPV(0, [Integer(), Min(10)])
    assert not rpv.execute()

    rpv = RPV([1, 2, 3], [List(), Min(4)])
    assert not rpv.execute()

    rpv = RPV([], [List(), Min(1)])
    assert not rpv.execute()

    rpv = RPV([], [List(), Min(10)])
    assert not rpv.execute()


# implement bad tests for min class.
def test_min_bad():
    # zero arg
    with pytest.raises(TypeError):
        assert not min().check(0)

    # many arg
    with pytest.raises(AttributeError):
        assert not min(5, 5, 5).check(0)

    # wrong type
    with pytest.raises(AttributeError):
        assert not min("5", "5").check(0)
