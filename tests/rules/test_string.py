from validator.rules import String
from validator import validate


def test_string_01():
    assert String().check("this is string")

    assert String().check("this is also string")

    assert String().check(f"this is interpolated string { 17 }")

    assert String().check("")

    assert String().check(f"{ 17 + 23 }")


def test_string_02():
    assert not String().check(17)

    assert not String().check([1, 2, 3])

    assert not String().check({"isThisAString": "No, this is dictionary"})

    assert not String().check(3.14)

    assert not String().check(int("17"))

    assert not String().check(None)


def test_string_03():
    assert validate({"val": "some string value"}, {"val": "string"})

    assert validate({"val": ""}, {"val": "string"})

    assert validate({"val": f"{17 + 23}"}, {"val": "string"})

    assert not validate({"val": 17}, {"val": "string"})

    assert not validate({"val": 3.1415}, {"val": "string"})

    assert not validate({"val": [12, 3, 5]}, {"val": "string"})

    assert not validate({"val": None}, {"val": "string"})
