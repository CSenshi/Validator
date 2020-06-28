from validator.rules_src import Rule
from re import compile


class Regex(Rule):
    """
    The field under validation must match the given regular expression.

    Examples:
    >>> Regex("c").check("abcdef")
    True

    >>> Regex("^c").check("abcdef")
    False
    """

    def __init__(self, pattern):
        Rule.__init__(self)
        self.pattern = compile(pattern)

    def check(self, arg):
        if self.pattern.search(arg):
            return True

        self.set_errror_message(
            f"Expected to follow regex {self.pattern.pattern}, Got: {arg}"
        )
        return False

    def __from_str__(self):
        pass
