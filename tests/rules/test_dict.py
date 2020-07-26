from validator.rules import Dict


def test_dict_01():
    assert Dict().check({"key_1": "val_1"})

    assert Dict().check({})

    assert Dict().check({1: 1, 2: 4, 3: 9})

    assert Dict().check({"a": 1, "b": 2})

    assert Dict().check({"": 0, "ab": 2})


def test_dict_02():
    assert not Dict().check(None)

    assert not Dict().check([1, 2, 3])

    assert not Dict().check({1, 2, 3})

    assert not Dict().check("ASD")

    assert not Dict().check("{a,s,d}")
