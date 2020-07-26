from validator.rules import Base64


def test_base64_01():
    assert Base64().check("c2hPd1MgaSBMSWtFOg==")

    assert Base64().check("U09VVEggUEFSSw==")

    assert Base64().check("QkxBQ0sgTUlSUk9S")

    assert Base64().check("RkFSR08=")

    assert Base64().check("QnJlYUtJTkcgQmFkIA==")


def test_base64_02():
    assert not Base64().check("hbsdf")

    assert not Base64().check("!@#")

    assert not Base64().check("bfjhsdf HGHG &^&&")

    assert not Base64().check("29i03r09j....")

    assert not Base64().check("olgak9999")
