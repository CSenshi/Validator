from validator.rules import Size
from validator.rules import Integer
from validator.rules import List
from validator.rule_pipe_validator import RulePipeValidator as RPV
from validator import validate


def test_size_01():
    assert Size(3).check("abc")

    assert Size(3).check(3)

    assert Size(123).check(123)

    assert Size(3).check([1, 2, 3])

    assert Size(3).check({1, 2, 3})

    assert Size(1.23).check(1.23)

    assert Size(3).check({"a": 1, "b": 2, "c": 3})

    assert Size(4).check(None)


def test_size_02():
    assert not Size(10).check("abc")

    assert not Size(0).check("0.00")

    assert not Size(3).check(0)


def test_size_03_rpv():
    rpv = RPV(data=18, rules=[Integer(), Size(18)])
    assert rpv.execute()

    rpv = RPV(data=0, rules=[Integer(), Size(0)])
    assert rpv.execute()

    rpv = RPV(data=[1, 2, 3], rules=[List(), Size(3)])
    assert rpv.execute()

    rpv = RPV(data=[], rules=[List(), Size(0)])
    assert rpv.execute()


def test_size_04_rpv():
    rpv = RPV(data=100, rules=[Integer(), Size(10)])
    assert not rpv.execute()

    rpv = RPV(data=100, rules=[Integer(), Size(0)])
    assert not rpv.execute()

    rpv = RPV(data=[1, 2, 3], rules=[List(), Size(6)])
    assert not rpv.execute()

    rpv = RPV([], rules=[List(), Size(-1)])
    assert not rpv.execute()


def test_size_05_string():
    assert validate({"val": "fghij"}, {"val": "size:5"})

    assert validate({"val": 10}, {"val": "size:10"})

    assert validate({"val": "15"}, {"val": "integer|size:15"})

    assert validate({"val": [-124, True]}, {"val": "size:2"})

    assert not validate({"val": [-124, True]}, {"val": "list|size:3"})

    assert not validate({"val": ["Name", "Surname"]}, {"val": "size:0"})

    assert not validate({"val": 8}, {"val": "size:7"})
