from validator.rules import Size
from validator.rules import Integer
from validator.rules import List
from validator.rule_pipe_validator import RulePipeValidator as RPV


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


def test_size_03_rpv():
    rpv = RPV(18, [Integer(), Size(18)])
    assert rpv.execute()

    rpv = RPV(0, [Integer(), Size(0)])
    assert rpv.execute()

    rpv = RPV([1, 2, 3], [List(), Size(3)])
    assert rpv.execute()

    rpv = RPV([], [List(), Size(0)])
    assert rpv.execute()


def test_size_04_rpv():
    rpv = RPV(100, [Integer(), Size(10)])
    assert not rpv.execute()

    rpv = RPV(100, [Integer(), Size(0)])
    assert not rpv.execute()

    rpv = RPV([1, 2, 3], [List(), Size(6)])
    assert not rpv.execute()

    rpv = RPV([], [List(), Size(-1)])
    assert not rpv.execute()
