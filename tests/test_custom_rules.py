from validator import validate, rules as R
from validator.rules import Rule

CUSTOM_ERROR_MSG = "Error: Custom Rule Failed"


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
    assert errors["ages"]["fun_ages"] == CUSTOM_ERROR_MSG
    assert errors["mail"]["fun_mail"] == CUSTOM_ERROR_MSG
    assert errors["name"]["<lambda>"] == CUSTOM_ERROR_MSG


def test_rule_func_07():
    class AgesChecker:
        def __call__(self, arg):
            return 18 <= arg

    class NameChecker:
        def __call__(self, arg):
            return len(arg) > 0

    class MailChecker:
        def __call__(self, arg):
            return "@" in arg

    rule = {"name": NameChecker(), "ages": AgesChecker(), "mail": MailChecker()}
    req = {"name": "Jon Doe", "ages": 33, "mail": "Jon.Doe@gmail.com"}
    assert validate(req, rule)

    req = {"name": "", "ages": 10, "mail": "Jon.Doe"}
    result, errors = validate(req, rule, True)
    # Result Should be False
    assert not result

    # Check for all rules' errors
    assert len(errors) == 3

    # Check if all of them are containing string
    assert len(errors["ages"]) == 1
    assert len(errors["mail"]) == 1
    assert len(errors["name"]) == 1

    # check for correct namings in errors
    assert "AgesChecker" in errors["ages"]
    assert "MailChecker" in errors["mail"]
    assert "NameChecker" in errors["name"]

    # check for correct namings in errors
    assert errors["ages"]["AgesChecker"] == CUSTOM_ERROR_MSG
    assert errors["mail"]["MailChecker"] == CUSTOM_ERROR_MSG
    assert errors["name"]["NameChecker"] == CUSTOM_ERROR_MSG


def test_rule_func_08():
    class AgesRule(Rule):
        def __init__(self, min):
            Rule.__init__(self)
            self.min = min

        def __call__(self, arg):
            return self.min <= arg

    class NameRule(Rule):
        def __init__(self, name):
            Rule.__init__(self)
            self.name = name

        def __call__(self, arg):
            return arg == self.name

    class MailRule(Rule):
        def __init__(self):
            Rule.__init__(self)

        def __call__(self, arg):
            if "@" in arg:
                return True
            self.set_errror_message("Mail Rule Failed")

    rule = {"name": NameRule("Jon Doe"), "ages": AgesRule(18), "mail": MailRule()}
    req = {"name": "Jon Doe", "ages": 33, "mail": "Jon.Doe@gmail.com"}
    assert validate(req, rule)

    req = {"name": "", "ages": 10, "mail": "Jon.Doe"}
    result, errors = validate(req, rule, True)
    # Result Should be False
    assert not result

    # Check for all rules' errors
    assert len(errors) == 3

    # Check if all of them are containing string
    assert len(errors["ages"]) == 1
    assert len(errors["mail"]) == 1
    assert len(errors["name"]) == 1

    # check for correct namings in errors
    assert "AgesRule" in errors["ages"]
    assert "MailRule" in errors["mail"]
    assert "NameRule" in errors["name"]

    # check for correct namings in errors
    assert errors["ages"]["AgesRule"] == "error"
    assert errors["mail"]["MailRule"] == "Mail Rule Failed"
    assert errors["name"]["NameRule"] == "error"
