from validator.rules import IPv4


def test_IPv4_01():
    rule = IPv4()
    assert rule('001.255.255.255')

    rule = IPv4()
    assert rule('234.1.2.0')

    rule = IPv4()
    assert rule('0.0.0.0')

    rule = IPv4()
    assert rule('252.253.254.255')


def test_IPv4_02():
    rule = IPv4()
    assert not rule('001.300.1.2')

    rule = IPv4()
    assert not rule('234.bla.2.0')

    rule = IPv4()
    assert not rule('0.A1.0.0')

    rule = IPv4()
    assert not rule('252.253.254.255.1')

    rule = IPv4()
    assert not rule('0001.253.254.255')