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
    rpv = RPV(data="0b01011001", rules=[Integer(), Size(89)])
    assert rpv.execute()

    rpv = RPV(data="0o113356", rules=[Integer(), Size(38638)])
    assert rpv.execute()

    rpv = RPV(data="12313", rules=[Integer(), Size(12313)])
    assert rpv.execute()

    rpv = RPV(data="0x1f", rules=[Integer(), Size(31)])
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


def test_size_06_integer():
    assert validate({"val": "23"}, {"val": "integer|size:23"})

    assert validate({"val": 11}, {"val": "integer|size:11"})

    assert validate({"val": 0}, {"val": "integer|size:0"})

    assert not validate({"val": "23"}, {"val": "integer|size:35"})

    assert not validate({"val": 11}, {"val": "integer|size:12"})

    assert not validate({"val": 0}, {"val": "integer|size:1"})


def test_size_07_decimal():
    assert validate({"val": "23"}, {"val": "decimal|size:23"})

    assert validate({"val": "305"}, {"val": "decimal|size:305"})

    assert validate({"val": "10"}, {"val": "decimal|size:10"})

    assert not validate({"val": "23"}, {"val": "decimal|size:35"})

    assert not validate({"val": "306"}, {"val": "decimal|size:305"})

    assert not validate({"val": "10"}, {"val": "decimal|size:111"})


def test_size_08_binary():
    assert validate({"val": "0b10111"}, {"val": "binary|size:23"})

    assert validate({"val": "0"}, {"val": "binary|size:0"})

    assert validate({"val": "1"}, {"val": "binary|size:1"})

    assert validate({"val": "1000"}, {"val": "binary|size:8"})

    assert not validate({"val": "0b10111"}, {"val": "binary|size:35"})

    assert not validate({"val": "0"}, {"val": "binary|size:213"})

    assert not validate({"val": "1"}, {"val": "binary|size:3331"})

    assert not validate({"val": "1000"}, {"val": "binary|size:28"})


def test_size_09_octal():
    assert validate({"val": "0o27"}, {"val": "octal|size:23"})

    assert validate({"val": "157"}, {"val": "octal|size:111"})

    assert validate({"val": "26"}, {"val": "octal|size:22"})

    assert not validate({"val": "0o27"}, {"val": "octal|size:35"})

    assert not validate({"val": "157"}, {"val": "octal|size:112"})

    assert not validate({"val": "26"}, {"val": "octal|size:26"})


def test_size_10_hex():
    assert validate({"val": "0x17"}, {"val": "hex|size:23"})

    assert validate({"val": "6F"}, {"val": "hex|size:111"})

    assert validate({"val": "29A"}, {"val": "hex|size:666"})

    assert not validate({"val": "0x17"}, {"val": "hex|size:35"})

    assert not validate({"val": "6F"}, {"val": "hex|size:1166"})

    assert not validate({"val": "29A"}, {"val": "hex|size:777"})


def test_size_11_list():
    assert validate({"val": [1, 2, 3, 4, 5]}, {"val": "list|size:5"})

    assert validate({"val": [1]}, {"val": "list|size:1"})

    assert validate({"val": []}, {"val": "list|size:0"})

    assert validate({"val": [1, 1, 1]}, {"val": "list|size:3"})

    assert not validate({"val": [1, 2, 3, 4, 5]}, {"val": "list|size:25"})

    assert not validate({"val": [1]}, {"val": "list|size:12"})

    assert not validate({"val": []}, {"val": "list|size:-1"})

    assert not validate({"val": [1, 1, 1]}, {"val": "list|size:33"})


def test_size_12_dict():
    assert validate(
        {"val": {"k1": "v1", "k2": "v2", "k3": "v3"}}, {"val": "dict|size:3"},
    )

    assert validate({"val": {}}, {"val": "dict|size:0"},)

    assert validate({"val": {"k1": "v1"}}, {"val": "dict|size:1"},)

    assert not validate(
        {"val": {"k1": "v1", "k2": "v2", "k3": "v3"}}, {"val": "dict|size:25"},
    )

    assert not validate({"val": {}}, {"val": "dict|size:12"},)

    assert not validate({"val": {"k1": "v1"}}, {"val": "dict|size:11"},)


def test_size_13_json():
    assert validate(
        {"val": '{"name":"John", "age":31, "city":"New York"}'}, {"val": "json|size:3"}
    )

    assert validate({"val": "{}"}, {"val": "json|size:0"},)

    assert validate({"val": '{"k1": "v1"}'}, {"val": "json|size:1"},)

    assert not validate(
        {"val": '{"name":"John", "age":31, "city":"New York"}'}, {"val": "json|size:25"}
    )

    assert not validate({"val": "{}"}, {"val": "dict|size:12"},)

    assert not validate({"val": '{"k1": "v1"}'}, {"val": "dict|size:11"},)


def test_size_14_string():
    assert validate({"val": "string"}, {"val": "string|size:6"})

    assert validate({"val": "string2"}, {"val": "string|size:7"})

    assert validate({"val": ""}, {"val": "string|size:0"})

    assert not validate({"val": "string"}, {"val": "string|size:66"})

    assert not validate({"val": "string2"}, {"val": "string|size:77"})

    assert not validate({"val": ""}, {"val": "string|size:10"})
