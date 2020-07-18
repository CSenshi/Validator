from validator.rules import IP
from validator import validate


def test_IP_01():
    assert IP().check("2001:0db8:85a3:0:0:8a2e:0370:7334")

    assert IP().check("ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff")

    assert IP().check("::1")

    assert IP().check("::2:3:4:5:6:7:8")

    assert IP().check("127.0.0.1")

    assert IP().check("01.9.9.255")


def test_IP_02():
    assert not IP().check(":1:2:3:4:5:6:7")

    assert not IP().check("1:2:3:4:5::6:7:8")

    assert not IP().check("2001:0db8:85a3:9876:1234:8a2e")

    assert not IP().check("234::123::23")

    assert not IP().check("0001.253.254.255")

    assert not IP().check("01.9.9.256")


def test_IP_03_string():
    assert validate({"val": "2001:0db8:85a3:0:0:8a2e:0370:7334"}, {"val": "ip"})

    assert validate({"val": "127.0.0.1"}, {"val": "ip"})

    assert not validate({"val": "234::123::23"}, {"val": "ip"})

    assert not validate({"val": "01.9.9.256"}, {"val": "ip"})
