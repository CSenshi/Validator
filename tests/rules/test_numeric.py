from validator.rules import Numeric


def test_numeric_01():
    assert Numeric().check("123")

    assert Numeric().check(123)


def test_numeric_02():
    assert not Numeric().check("abc")

    assert not Numeric().check("1abc23")
