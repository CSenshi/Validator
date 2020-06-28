from validator.rules import Same


def test_same_01():
    assert Same("123").check("123")

    assert Same("123").check(123)

    assert Same(123).check("123")

    assert Same([1, 2, 3]).check([1, 2, 3])


def test_same_02():
    assert not Same("456").check("123")

    assert not Same("456").check(123)
