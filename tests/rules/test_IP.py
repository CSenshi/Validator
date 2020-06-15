from validator.rules import IP


def test_IP_01():
    rule = IP()
    assert rule.check("2001:0db8:85a3:0:0:8a2e:0370:7334")

    rule = IP()
    assert rule.check("ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff")

    rule = IP()
    assert rule.check("::1")

    rule = IP()
    assert rule.check("::2:3:4:5:6:7:8")

    rule = IP()
    assert rule.check("127.0.0.1")

    rule = IP()
    assert rule.check("01.9.9.255")


def test_IP_02():
    rule = IP()
    assert not rule.check(":1:2:3:4:5:6:7")

    rule = IP()
    assert not rule.check("1:2:3:4:5::6:7:8")

    rule = IP()
    assert not rule.check("2001:0db8:85a3:9876:1234:8a2e")

    rule = IP()
    assert not rule.check("234::123::23")

    rule = IP()
    assert not rule.check("0001.253.254.255")

    rule = IP()
    assert not rule.check("01.9.9.256")
