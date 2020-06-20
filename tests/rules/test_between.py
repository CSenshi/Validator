from validator.rules import Between
from validator.rules import Integer
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


# implement bad tests for between class
def test_between_bad():
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
