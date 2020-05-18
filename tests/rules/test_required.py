from validator.rules import Required


def test_required_01():
    rule = Required()
    assert not rule([])
    assert not rule("")
    assert not rule(None)
    assert not rule({})


def test_required_02():
    rule = Required()
    value_to_check = 0
    assert rule(value_to_check)

    value_to_check = False
    assert rule(value_to_check)

    value_to_check = "Not empty"
    assert rule(value_to_check)

    value_to_check = "სხვა ენა ვცადოთ?"
    assert rule(value_to_check)

    value_to_check = ["Something here"]
    assert rule(value_to_check)

    value_to_check = {"Still not empty"}
    assert rule(value_to_check)
