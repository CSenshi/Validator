from validator.rules import Same
from validator.rules_wrapper import RulesWrapper as RW


def test_same_01():
    req = {"old_pass": "password", "new_pass": "password"}
    rule = {"new_pass": [Same("old_pass")]}

    rw = RW(req, rule)
    rw.run()
    assert rw.get_result()


def test_same_02():
    req = {"old_pass": "old_password", "new_pass": "new_password"}
    rule = {"new_pass": [Same("old_pass")]}

    rw = RW(req, rule)
    rw.run()
    assert not rw.get_result()
