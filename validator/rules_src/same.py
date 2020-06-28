from validator.rules_src import Rule


class Same(Rule):
    """
    The given field must match the field under validation

    Examples:
    >>> Same("123").check("123")
    True

    >>> Same("456").check("123")
    False
    """

    def __init__(self, value):
        Rule.__init__(self)
        self.value = str(value)

    def check(self, arg):
        if str(arg) == self.value:
            return True

        self.set_errror_message(f"Expected exact value {self.value}, Got: {arg}")
        return False

    def __from_str__(self):
        pass
