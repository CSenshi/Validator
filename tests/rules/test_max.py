from validator.rules import Max
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


def test_max_bad():
    # zero arg
    with pytest.raises(TypeError):
        assert not Max().check(0)

    # many arg
    with pytest.raises(TypeError):
        assert not Max(5, 5, 5).check(0)

    # wrong type
    with pytest.raises(TypeError):
        assert not Max("5", "5").check(0)
