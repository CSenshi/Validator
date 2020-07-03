from validator.rules import Same
from validator.rules_wrapper import RulesWrapper as RW


def test_same_01():
    req = {"old_pass": "password", "new_pass": "password"}
    rule = {"new_pass": [Same("old_pass")]}
    rw = RW(req, rule)
    rw.run()
    assert rw.get_result()

    req = {"old_val": 5, "new_val": 5}
    rule = {"new_val": [Same("old_val")]}
    rw = RW(req, rule)
    rw.run()
    assert rw.get_result()

    req = {"old_arr": [1, 2, 3], "new_arr": [1, 2, 3]}
    rule = {"new_arr": [Same("old_arr")]}
    rw = RW(req, rule)
    rw.run()
    assert rw.get_result()


def test_same_02():
    req = {"old_pass": "old_password", "new_pass": "new_password"}
    rule = {"new_pass": [Same("old_pass")]}
    rw = RW(req, rule)
    rw.run()
    assert not rw.get_result()

    req = {"old_val": 5, "new_val": 6}
    rule = {"new_val": [Same("old_val")]}
    rw = RW(req, rule)
    rw.run()
    assert not rw.get_result()

    req = {"old_arr": [1, 2, 3], "new_arr": [1, 2, 3, 4, 5]}
    rule = {"new_arr": [Same("old_arr")]}
    rw = RW(req, rule)
    rw.run()
    assert not rw.get_result()
