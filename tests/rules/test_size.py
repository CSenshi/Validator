from validator.rules import Size


def test_size_01():
    assert Size(3).check("abc")

    assert Size(3).check(123)

    assert Size(3).check(0.00)

    assert Size(3).check(1.2)

    assert Size(3).check([1, 2, 3])

    assert Size(3).check({1, 2, 3})

    assert Size(3).check({"a": 1, "b": 2, "c": 3})

    assert Size(4).check(None)


def test_size_02():
    assert not Size(10).check("abc")

    assert not Size(123).check(123)

    assert not Size(0).check(0.00)

    assert not Size(1.23).check(1.23)
