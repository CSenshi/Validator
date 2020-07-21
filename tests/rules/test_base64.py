from validator.rules import Base32
from validator import validate


def test_base32_01():
    assert Base32().check("c2hPd1MgaSBMSWtFOg==")

    assert Base32().check("U09VVEggUEFSSw==")

    assert Base32().check("QkxBQ0sgTUlSUk9S")

    assert Base32().check("RkFSR08=")

    assert Base32().check("QnJlYUtJTkcgQmFkIA==")


def test_base32_02():
    assert not Base32().check("hbsdf")

    assert not Base32().check("!@#")

    assert not Base32().check("bfjhsdf HGHG &^&&")

    assert not Base32().check("29i03r09j....")

    assert not Base32().check("olgak9999")
