from validator import validate, rules as R


def test_rule_func_01():
    # True Rule
    def func_true(x):
        return True

    assert validate({"name": "Jon"}, {"name": func_true})

    # False Rule
    def func_false(x):
        return False

    assert not validate({"name": "Jon"}, {"name": func_false})


def test_rule_func_02():
    def func(x):
        return x > 5

    rule = {"age": func}
    assert validate({"age": 10}, rule)
    assert not validate({"age": 0}, rule)
    assert not validate({"age": 5}, rule)


def test_rule_func_03():
    rule = {"age": lambda x: True}
    assert validate({"age": "Jon"}, rule)
    assert validate({"age": "Doe"}, rule)

    rule = {"age": lambda x: False}
    assert not validate({"age": "Fail"}, rule)


def test_rule_func_04():
    rule = {"age": lambda x: x == "PASS"}
    assert validate({"age": "PASS"}, rule)
    assert not validate({"age": "FAIL"}, rule)
    assert not validate({"age": "SMTH"}, rule)


def test_rule_func_05():
    def func_prime(x):
        if x <= 1:
            return False

        return not any([(x % i) == 0 for i in range(2, x)])

    rule = {"prime_num": func_prime}
    assert validate({"prime_num": 13}, rule)
    assert validate({"prime_num": 23}, rule)
    assert not validate({"prime_num": 26}, rule)
    assert not validate({"prime_num": 1}, rule)
