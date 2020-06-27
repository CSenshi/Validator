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


def test_rule_func_06():
    def fun_ages(x):
        return x >= 18

    # Dummy Checker
    def fun_mail(x):
        return "@" in x

    req = {"name": "", "ages": 10, "mail": "not mail"}

    rules = {"name": lambda x: len(x) > 0, "ages": fun_ages, "mail": fun_mail}

    result, errors = validate(req, rules, True)

    # Result Should be False
    assert not result

    # Check for all rules' errors
    assert len(errors) == 3

    # Check if all of them are containing string
    assert len(errors["ages"]) == 1
    assert len(errors["mail"]) == 1
    assert len(errors["name"]) == 1

    # check for correct namings in errors
    assert "fun_ages" in errors["ages"]
    assert "fun_mail" in errors["mail"]
    assert "<lambda>" in errors["name"]

    # check for correct namings in errors
    assert errors["ages"]["fun_ages"] == "Error: Custom Rule Failed"
    assert errors["mail"]["fun_mail"] == "Error: Custom Rule Failed"
    assert errors["name"]["<lambda>"] == "Error: Custom Rule Failed"
