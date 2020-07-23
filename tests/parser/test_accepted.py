from validator.rules import Accepted
from validator import validate


def test_accepted_01():
    assert Accepted().check(True)

    assert Accepted().check("1")

    assert Accepted().check("true")

    assert Accepted().check("TRUE")

    assert Accepted().check("TrUe")

    assert Accepted().check("ON")

    assert Accepted().check("on")

    assert Accepted().check("Yes")

    assert Accepted().check("YeS")

    assert Accepted().check("yes")


def test_accepted_02():
    assert not Accepted().check(False)

    assert not Accepted().check("0")

    assert not Accepted().check("false")

    assert not Accepted().check("FalSE")

    assert not Accepted().check("off")

    assert not Accepted().check("OFF")

    assert not Accepted().check("NO")

    assert not Accepted().check("no")

    assert not Accepted().check("some random")

    assert not Accepted().check("1234567890")


def test_accepted_03():
    assert validate({"val": True}, {"val": "accepted"})

    assert validate({"val": "1"}, {"val": "accepted"})

    assert validate({"val": "on"}, {"val": "accepted"})

    assert validate({"val": "yes"}, {"val": "accepted"})

    assert not validate({"val": False}, {"val": "accepted"})

    assert not validate({"val": "false"}, {"val": "accepted"})

    assert not validate({"val": "0"}, {"val": "accepted"})

    assert not validate({"val": "off"}, {"val": "accepted"})

    assert not validate({"val": "no"}, {"val": "accepted"})
