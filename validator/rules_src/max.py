from validator.rules_src import Rule


class Max(Rule):
    """
    The field under validation must be less than or equal to a maximum value 

    Examples:
    >>> Max(18).check(23)
    False

    >>> Max(18).check(15)
    True
    """

    def __init__(self, max_value):
        Rule.__init__(self)
        self.max_value = max_value

    def check(self, arg):
        if self.max_value >= arg:
            return True

        self.set_errror_message(f"Expected Maximum: {self.max_value}, Got: {arg}")
        return False

    def __from_str__(self):
        self.max_value = int(self.max_value)
