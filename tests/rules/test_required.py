from validator.rules import Required


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
