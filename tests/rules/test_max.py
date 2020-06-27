from validator.rules import Max
from validator.rules import Integer
from validator.rules import List
from validator.rule_pipe_validator import RulePipeValidator as RPV
import pytest


def test_max_01():
    assert not Max(2).check("max")

    assert Max(4).check("max")


def test_max_02():
    assert not Max(-18).check("123456789")

    assert not Max(0).check("123456789")

    assert Max(20).check("123456789")

    assert Max(9).check("123456789")


def test_max_03():
    assert Max(10).check([1, 2, 3, 4])

    assert Max(10).check("qweasdzxc")

    assert Max(10).check({1, 2, 3, 4, 5})


def test_max_04_rpv():
    rpv = RPV(18, [Integer(), Max(18)])
    assert rpv.execute()

    rpv = RPV(0, [Integer(), Max(0)])
    assert rpv.execute()

    rpv = RPV(0, [Integer(), Max(10)])
    assert rpv.execute()

    rpv = RPV([1, 2, 3], [List(), Max(3)])
    assert rpv.execute()

    rpv = RPV([], [List(), Max(0)])
    assert rpv.execute()

    rpv = RPV([], [List(), Max(10)])
    assert rpv.execute()


def test_max_05_rpv():
    rpv = RPV(1000, [Integer(), Max(10)])
    assert not rpv.execute()

    rpv = RPV(0, [Integer(), Max(-10)])
    assert not rpv.execute()

    rpv = RPV([1, 2, 3], [List(), Max(2)])
    assert not rpv.execute()

    rpv = RPV([], [List(), Max(-1)])
    assert not rpv.execute()


def test_max_06_bad():
    # zero arg
    with pytest.raises(TypeError):
        assert not Max().check(0)

    # many arg
    with pytest.raises(TypeError):
        assert not Max(5, 5, 5).check(0)

    # wrong type
    with pytest.raises(TypeError):
        assert not Max("5", "5").check(0)
