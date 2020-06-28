from validator.rules import Regex


def test_regex_01():
    assert Regex("c").check("abcdef")

    assert Regex("^foo$").check("foo")

    assert Regex("abc*").check("abccc")

    assert Regex("abc*").check("ab")


def test_regex_02():
    assert not Regex("^c").check("abcdef")

    assert not Regex("^foo$").check("foobar")

    assert not Regex("abc*").check("a")
