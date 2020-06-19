from validator.rules import List


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
