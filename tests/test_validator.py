from validator import Validator


def test_validator():
    assert Validator({}, {}).validate() == True
