from validator.rules import Regex
from validator import validate


def test_regex_01():
    assert Regex("c").check("abcdef")

    assert Regex("^foo$").check("foo")

    assert Regex("abc*").check("abccc")

    assert Regex("abc*").check("ab")

    assert Regex("gray|grey").check("gray")

    assert Regex("z{3,6}").check("zzzz")

    assert Regex("xyz$").check("abcxyz")


def test_regex_02():
    assert not Regex("^c").check("abcdef")

    assert not Regex("^foo$").check("foobar")

    assert not Regex("abc*").check("a")

    assert not Regex("gr[ae]y").check("groy")

    assert not Regex("z{3,6}").check("xyzzxy")

    assert not Regex("xyz$").check("xyzabc")


def test_regex_03_string():
    assert validate({"val": "abcdef"}, {"val": "regex:a"})

    assert validate({"val": "dcdcdc"}, {"val": "regex:(dc)*"})

    assert not validate({"val": "groy"}, {"val": "regex:gr[ae]y"})

    assert not validate({"val": "xyzabc"}, {"val": "regex:xyz$"})
