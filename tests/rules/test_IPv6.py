from validator.rules import IPv6


def test_IPv6_01():
    rule = IPv6()
    assert rule.check("2001:0db8:85a3:0:0:8a2e:0370:7334")

    rule = IPv6()
    assert rule.check("ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff")

    rule = IPv6()
    assert rule.check("::1")

    rule = IPv6()
    assert rule.check("::2:3:4:5:6:7:8")


def test_IPv6_02():
    rule = IPv6()
    assert not rule.check(":1:2:3:4:5:6:7")

    rule = IPv6()
    assert not rule.check("1:2:3:4:5::6:7:8")

    rule = IPv6()
    assert not rule.check("2001:0db8:85a3:9876:1234:8a2e")

    rule = IPv6()
    assert not rule.check("234::123::23")

    rule = IPv6()
    assert not rule.check("0001.253.254.255")
