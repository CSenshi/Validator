from validator.rules import Min
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
