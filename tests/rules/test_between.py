from validator.rules import Between
from validator.rules import Integer
from validator.rules import List
from validator.rule_pipe_validator import RulePipeValidator as RPV
import pytest


def test_between_01():
    assert Between(2, 18).check("Between")

    assert not Between(10, 18).check("Between")

    assert not Between(2, 4).check("Between")


def test_between_02():
    assert Between(-15, 30).check("")

    assert Between(-15, 30).check([])

    assert Between(-15, 30).check(123456789)


def test_between_03():
    assert Between(7, 7).check("Between")

    assert not Between(5, 5).check("asd")


def test_between_04():
    rpv = RPV(5, [Integer(), Between(2, 18)])
    assert rpv.execute()

    rpv = RPV(1, [Integer(), Between(2, 18)])
    assert not rpv.execute()

    rpv = RPV(19, [Integer(), Between(2, 18)])
    assert not rpv.execute()


def test_between_05():
    rpv = RPV(-15, [Integer(), Between(-15, 30)])
    assert rpv.execute()

    rpv = RPV(30, [Integer(), Between(-15, 30)])
    assert rpv.execute()

    rpv = RPV(0, [Integer(), Between(-15, 30)])
    assert rpv.execute()


def test_between_06():
    rpv = RPV(5, [Integer(), Between(5, 5)])
    assert rpv.execute()

    rpv = RPV(0, [Integer(), Between(5, 5)])
    assert not rpv.execute()


# implement bad tests for between class
def test_between_07_bad():
    # zero arg
    with pytest.raises(TypeError):
        assert not Between().check(0)

    # 1 arg
    with pytest.raises(TypeError):
        assert Between(5).check(0)

    with pytest.raises(TypeError):
        assert Between(5, 5, 5).check(0)

    # wrong type
    with pytest.raises(TypeError):
        assert Between("5", "5").check(0)
