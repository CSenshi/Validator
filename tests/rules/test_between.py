from validator.rules import Between
from validator.rules import Integer
from validator.rule_pipe_validator import RulePipeValidator as RPV
from validator import validate
import pytest


def test_between_01():
    assert Between(2, 18).check("Between")

    assert not Between(10, 18).check("Between")

    assert not Between(2, 4).check("Between")


def test_between_02():
    assert Between(-15, 30).check("")

    assert Between(-15, 30).check([])

    assert not Between(-15, 30).check(123456789)


def test_between_03():
    assert Between(7, 7).check("Between")

    assert not Between(5, 5).check("asd")


def test_between_04():
    rpv = RPV(data=5, rules=[Integer(), Between(2, 18)])
    assert rpv.execute()

    rpv = RPV(data=1, rules=[Integer(), Between(2, 18)])
    assert not rpv.execute()

    rpv = RPV(data=19, rules=[Integer(), Between(2, 18)])
    assert not rpv.execute()


def test_between_05():
    rpv = RPV(data=-15, rules=[Integer(), Between(-15, 30)])
    assert rpv.execute()

    rpv = RPV(data=30, rules=[Integer(), Between(-15, 30)])
    assert rpv.execute()

    rpv = RPV(data=0, rules=[Integer(), Between(-15, 30)])
    assert rpv.execute()


def test_between_06():
    rpv = RPV(data=5, rules=[Integer(), Between(5, 5)])
    assert rpv.execute()

    rpv = RPV(data=0, rules=[Integer(), Between(5, 5)])
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


def test_between_08_string():
    assert validate({"val": "15"}, {"val": "between:1,20"})

    assert validate({"val": -173}, {"val": "between:-400,0"})

    assert validate({"val": [15, "3", {}]}, {"val": "between:2,4"})

    assert not validate({"val": "MACS"}, {"val": "between:12,300"})

    assert not validate({"val": []}, {"val": "between:14,31"})


def test_between_09_string():
    assert validate({"val": "9"}, {"val": "integer|between:2,17"})

    assert validate({"val": [1, 2, 3]}, {"val": "list|between:2,17"})

    assert not validate({"val": "9"}, {"val": "integer|between:2,7"})

    assert not validate({"val": [5, 2]}, {"val": "list|between:1,1"})
