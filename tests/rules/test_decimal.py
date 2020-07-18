from validator.rules import Decimal
from validator import validate


def test_decimal_01():
    assert Decimal().check("73021")

    assert Decimal().check("152717")

    assert Decimal().check("0")

    assert Decimal().check("111110000")

    assert Decimal().check("355312")


def test_decimal_02():
    assert not Decimal().check("0bk123123")

    assert not Decimal().check("0x35afd35")

    assert not Decimal().check("0b3553")

    assert not Decimal().check("0oA123BP")

    assert not Decimal().check("Abc123Abc")

    assert not Decimal().check("A1F23456789")


def test_decimal_03():
    assert validate({"val": "122333444555"}, {"val": "decimal"})

    assert validate({"val": "1234"}, {"val": "decimal"})

    assert validate({"val": "-1234"}, {"val": "decimal"})

    assert not validate({"val": "PD010DP"}, {"val": "decimal"})

    assert not validate({"val": "ll000ll"}, {"val": "decimal"})


def test_decimal_04():
    assert Decimal().check("-0")

    assert Decimal().check("-111110000")

    assert Decimal().check("-355312")

    assert not Decimal().check("-0bk123123")

    assert not Decimal().check("-0x35afd35")

    assert not Decimal().check("-0b3553")
