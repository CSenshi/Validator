from validator.rules import Hex
from validator import validate


def test_hex_01():
    assert Hex().check("A1B2c3")

    assert Hex().check("0xA1b2C3")

    assert Hex().check("884F43")

    assert Hex().check("EBB3A8")

    assert Hex().check("452F2B")

    assert Hex().check("DC4C31")

    assert Hex().check("0")

    assert Hex().check("1111111111111111")


def test_hex_02():
    assert not Hex().check("abcdefgh")

    assert not Hex().check("A1B2c3./")

    assert not Hex().check("A2Bc30ki")

    assert not Hex().check("1231drezga")

    assert not Hex().check("123ა")

    assert not Hex().check("0,A23C")

    assert not Hex().check("324sadaw")

    assert not Hex().check("1231dfgdfg")


def test_hex_03():
    assert validate({"val": "Abc123Abc"}, {"val": "hex"})

    assert validate({"val": "123123123123"}, {"val": "hex"})

    assert not validate({"val": "A123BP"}, {"val": "hex"})

    assert not validate({"val": "0bk123123"}, {"val": "hex"})
