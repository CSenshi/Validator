from validator.rules import Octal
from validator import validate


def test_octal_01():
    assert Octal().check("73021")

    assert Octal().check("0o73021")

    assert Octal().check("152717")

    assert Octal().check("0")

    assert Octal().check("111110000")

    assert Octal().check("355312")


def test_octal_02():
    assert not Octal().check("0bk123123")

    assert not Octal().check("35kd35")

    assert not Octal().check("35ა53")

    assert not Octal().check("A123BP")

    assert not Octal().check("Abc123Abc")

    assert not Octal().check("123456789")


def test_octal_03():
    assert validate({"val": "122333444555"}, {"val": "octal"})

    assert validate({"val": "1234"}, {"val": "octal"})

    assert not validate({"val": "PD010DP"}, {"val": "octal"})

    assert not validate({"val": "ll000ll"}, {"val": "octal"})


def test_octal_04():
    assert validate({"val": "-122333444555"}, {"val": "octal"})

    assert validate({"val": "-1234"}, {"val": "octal"})

    assert validate({"val": "-1"}, {"val": "octal"})
