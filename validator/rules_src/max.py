from validator.rules_src import Rule


class Max(Rule):
    """
    >>> TrueMax = Max(18)
    >>> TrueMax(23)
    False

    >>> TrueMax = Max(18)
    >>> TrueMax(15)
    True
    """

    def __init__(self, max_value):
        self.max_value = max_value

    def __call__(self, arg):
        if self.max_value >= arg:
            return True

        err_msg = "Expected Maximum: {}, Got: {}".format(self.max_value, arg)
        self.set_errror_message(err_msg)
        return False

    def __from_str__(self):
        self.max_value = int(self.max_value)
