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
    assert rule.check(value_to_check)

    value_to_check = False
    assert rule.check(value_to_check)

    value_to_check = "Not empty"
    assert rule.check(value_to_check)

    value_to_check = "სხვა ენა ვცადოთ?"
    assert rule.check(value_to_check)

    value_to_check = ["Something here"]
    assert rule.check(value_to_check)

    value_to_check = {"Still not empty"}
    assert rule.check(value_to_check)
