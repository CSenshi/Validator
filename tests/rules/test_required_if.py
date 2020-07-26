from validator.rules import RequiredIf
from validator.rules_wrapper import RulesWrapper as RW


def test_required_if_01():
    req = {"under_age": "no"}
    rule = {"parrent": [RequiredIf("uner_age", "yes")]}
    rw = RW(req, rule)
    rw.run()
    assert rw.get_result()

    req = {"under_age": "yes", "parrent": "John Doe"}
    rule = {"parrent": [RequiredIf("uner_age", "yes")]}
    rw = RW(req, rule)
    rw.run()
    assert rw.get_result()

    req = {"age": 18}
    rule = {"parrent": [RequiredIf("age", 23)]}
    rw = RW(req, rule)
    rw.run()
    assert rw.get_result()

    req = {"age": 23, "rand": "non empty"}
    rule = {"rand": [RequiredIf("age", 23)]}
    rw = RW(req, rule)
    rw.run()
    assert rw.get_result()


def test_required_if_02():
    req = {"age": 18}
    rule = {"parrent": [RequiredIf("age", 18)]}
    rw = RW(req, rule)
    rw.run()
    assert not rw.get_result()

    req = {"age": 23, "rand": ""}
    rule = {"rand": [RequiredIf("age", 23)]}
    rw = RW(req, rule)
    rw.run()
    assert not rw.get_result()
