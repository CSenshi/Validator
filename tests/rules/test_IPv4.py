from validator.rules import IPv4


def test_IPv4_01():
    assert IPv4().check("001.255.255.255")

    assert IPv4().check("234.1.2.0")

    assert IPv4().check("0.0.0.0")

    assert IPv4().check("252.253.254.255")


def test_IPv4_02():
    assert not IPv4().check("001.300.1.2")

    assert not IPv4().check("234.bla.2.0")

    assert not IPv4().check("0.A1.0.0")

    assert not IPv4().check("252.253.254.255.1")

    assert not IPv4().check("0001.253.254.255")
