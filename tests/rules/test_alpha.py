from validator.rules import Alpha


def test_apha_01():
    assert Alpha().check("yolo")
    assert Alpha().check("KillerBunny")
    assert Alpha().check("AAA")


def test_apha_02():
    assert not Alpha().check("16:20")
    assert not Alpha().check("")
    assert not Alpha().check(" ")
    assert not Alpha().check(",.,.,")
