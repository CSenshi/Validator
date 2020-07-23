from validator.rules_src import Rule
from re import compile


class Regex(Rule):
    """
    The field under validation must match the given regular expression.

    Examples:
    >>> from validator import validate

    >>> reqs = {"value" : "PythonValidator"}
    >>> rule = {"value" : "regex:^[0-9a-zA-Z]*$"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"value" : "Python_Validator"}
    >>> rule = {"value" : "regex:^[0-9a-zA-Z]*$"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self, pattern):
        Rule.__init__(self)
        self.pattern = compile(pattern)

    def check(self, arg):
        if self.pattern.search(arg):
            return True

        self.set_error(f"Expected to follow regex {self.pattern.pattern}, Got: {arg}")
        return False

    def __from_str__(self):
        pass
