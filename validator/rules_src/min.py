from validator.rules_src import Rule


class Min(Rule):
    """
    >>> TrueMin = Min(18)
    >>> TrueMin(23)
    True

    >>> TrueMin = Min(18)
    >>> TrueMin(15)
    False
    """

    def __init__(self, min_value):
        Rule.__init__(self)
        self.min_value = min_value

    def __call__(self, arg):
        if self.min_value <= arg:
            return True

        err_msg = f"Expected Minumum: {self.min_value}, Got: {arg}"
        self.set_errror_message(err_msg)
        return False

    def __from_str__(self):
        self.min_value = int(self.min_value)
