from validator.rules import IPv6


def test_IPv6_01():
    assert IPv6().check("2001:0db8:85a3:0:0:8a2e:0370:7334")

    assert IPv6().check("ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff")

    assert IPv6().check("::1")

    assert IPv6().check("::2:3:4:5:6:7:8")


def test_IPv6_02():
    assert not IPv6().check(":1:2:3:4:5:6:7")

    assert not IPv6().check("1:2:3:4:5::6:7:8")

    assert not IPv6().check("2001:0db8:85a3:9876:1234:8a2e")

    assert not IPv6().check("234::123::23")

    assert not IPv6().check("0001.253.254.255")
