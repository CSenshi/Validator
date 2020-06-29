from validator.rules_src import Rule


class Numeric(Rule):
    """
    The field under validation must be numeric

    Examples:
    >>> Numeric().check("123")
    True

    >>> Numeric().check("abc")
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        if str(arg).isnumeric():
            return True

        self.set_errror_message(f"Expected numeric value, Got: {arg}")
        return False

    def __from_str__(self):
        pass
