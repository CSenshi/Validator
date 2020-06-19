from validator.rule_pipe_validator import RulePipeValidator as RPV
from validator import rules as R
from validator import Validator, validate, validate_many, rules as R


def test_rpv_001_simple():
    data = "10"

    # with integer
    rules = [R.Integer(), R.Size(10)]
    rpv = RPV(data, rules)
    assert rpv.execute()

    # without integer
    rules = [R.Size(10)]
    rpv = RPV(data, rules)
    assert not rpv.execute()


def test_rpv_002_simple():
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # with list
    rules = [R.List(), R.Size(10)]
    rpv = RPV(data, rules)
    assert rpv.execute()

    # without list
    rules = [R.Integer(), R.Size(10)]
    rpv = RPV(data, rules)
    assert not rpv.execute()


def test_rpv_003_simple():
    request = {"age": 23}
    rule = {"age": "integer|size:23"}
    result = Validator(request, rule).validate()
    assert result

    request = {"age": 23}
    rule = {"age": "size:23"}
    result = Validator(request, rule).validate()
    assert not result

    request = {"age": 23}
    rule = {"age": "size:2"}
    result = Validator(request, rule).validate()
    assert result

    request = {"age": 123456789}
    rule = {"age": "size:9"}
    result = Validator(request, rule).validate()
    assert result

    request = {"age": 123456789}
    rule = {"age": "integer|size:123456789"}
    result = Validator(request, rule).validate()
    assert result


def test_rpv_004_simple():
    request = {"age": "23"}
    rule = {"age": "integer|size:23"}
    result = Validator(request, rule).validate()
    assert result

    request = {"age": "23"}
    rule = {"age": "size:23"}
    result = Validator(request, rule).validate()
    assert not result

    request = {"age": "23"}
    rule = {"age": "size:2"}
    result = Validator(request, rule).validate()
    assert result

    request = {"age": "123456789"}
    rule = {"age": "size:9"}
    result = Validator(request, rule).validate()
    assert result

    request = {"age": "123456789"}
    rule = {"age": "integer|size:123456789"}
    result = Validator(request, rule).validate()
    assert result


def test_rpv_005_simple():
    request = {"args": [1, 2, 3]}
    rule = {"args": "size:3"}
    result = Validator(request, rule).validate()
    assert result

    request = {"args": [1, 2, 3]}
    rule = {"args": "list|size:3"}
    result = Validator(request, rule).validate()
    assert result

    request = {"args": [1, 2, 3]}
    rule = {"args": "integer|size:23"}
    result = Validator(request, rule).validate()
    assert not result
