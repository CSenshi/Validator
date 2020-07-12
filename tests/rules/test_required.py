from validator.rules import Required
from validator import validate


def test_required_01():
    assert not Required()([])

    assert not Required()("")

    assert not Required()(None)

    assert not Required()({})


def test_required_02():
    assert Required().check(0)

    assert Required().check(False)

    assert Required().check("Not empty")

    assert Required().check("სხვა ენა ვცადოთ?")

    assert Required().check(["Something here"])

    assert Required().check({"Still not empty"})


def test_required_03_string():
    assert validate({"val": "abcdef"}, {"val": "required"})

    assert validate({"val": 0}, {"val": "required"})

    assert validate({"val": "15"}, {"val": "integer|required"})

    assert not validate({"val": {}}, {"val": "required"})

    assert not validate({"val": ""}, {"val": "required"})

    assert not validate({"val": None}, {"val": "required"})
