from validator import Validator, rules as R


def test_validator_001_simple():
    request = {"age": 23}
    rule = {"age": [R.Min(18)]}
    result = Validator(request, rule).validate()
    assert result

    request = {"age": 13}
    rule = {"age": [R.Min(18)]}
    result = Validator(request, rule).validate()
    assert not result

    request = {"age": 13}
    rule = {"age": [R.Max(18)]}
    result = Validator(request, rule).validate()
    assert result

    request = {"name": "Jon"}
    rule = {"name": [R.Required()]}
    result = Validator(request, rule).validate()
    assert result

    request = {"name": ""}
    rule = {"name": [R.Required()]}
    result = Validator(request, rule).validate()
    assert not result


def test_validator_002_simple():
    request = {"age": 23}
    rule = {"age": [R.Min(18), R.Max(30)]}
    result = Validator(request, rule).validate()
    assert result

    request = {"age": 33}
    rule = {"age": [R.Min(18), R.Max(30)]}
    result = Validator(request, rule).validate()
    assert not result

    request = {"age": 23, "name": "Jon"}
    rule = {"age": [R.Min(18)], "name": [R.Required()]}
    result = Validator(request, rule).validate()
    assert result

    request = {"age": 23, "name": ""}
    rule = {"age": [R.Min(18), R.Max(30)], "name": [R.Required()]}
    result = Validator(request, rule).validate()
    assert not result
