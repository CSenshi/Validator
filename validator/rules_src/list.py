from validator.rules_src import Rule


class List(Rule):
    """
    The field under validation must be a list (Python array)

    Examples:
    >>> List().check([1, 2, 3])
    True

    >>> List().check(123)
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        if isinstance(arg, list):
            return True

        self.set_errror_message(f"Expected type list, Got:{type(arg)}")
        return False

    def __from_str__(self):
        pass
