from validator.rules import List
from validator import validate


def test_list_01():
    assert List().check([1, 2, 3])

    assert List().check(["a", "b", "c"])

    assert List().check([{}])

    assert List().check([{1, 2, 3}])

    assert List().check([(1, 2)])

    assert List().check([(1, 2), [3, 4], {5, 6}, {7: 8}, "9"])


def test_list_02():
    assert not List().check(None)

    assert not List().check({})

    assert not List().check("abc")

    assert not List().check({1, 2})

    assert not List().check(123)


def test_list_03_string():
    assert validate({"val": []}, {"val": "list"})

    assert validate({"val": [5, "213", "blah"]}, {"val": "list"})

    assert validate({"val": [{2: 3}, {"key", "value"}]}, {"val": "list"})

    assert not validate({"val": 15}, {"val": "list"})

    assert not validate({"val": "string here"}, {"val": "list"})

    assert not validate({"val": {}}, {"val": "list"})

    assert not validate({"val": None}, {"val": "list"})

    assert not validate({"val": True}, {"val": "list"})
