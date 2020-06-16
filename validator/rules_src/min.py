from validator.rules_src import Rule


class Min(Rule):
    """
    The field under validation must be greater than or equal to a minimum value 

    Examples:
    >>> Min(18).check(23)
    True

    >>> Min(18).check(15)
    False
    """

    def __init__(self, min_value):
        Rule.__init__(self)
        self.min_value = min_value

    def check(self, arg):
        if self.min_value <= arg:
            return True

        self.set_errror_message(f"Expected Minumum: {self.min_value}, Got: {arg}")
        return False

    def __from_str__(self):
        self.min_value = int(self.min_value)
