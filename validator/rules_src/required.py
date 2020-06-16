from validator.rules_src import Rule


class Required(Rule):
    """
    The field under validation must be present in the input data and not empty 

    Examples:
    >>> Required().check('Not Empty')
    True

    >>> Required().check('')
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        if arg is None or (hasattr(arg, "__len__") and len(arg) == 0):
            self.set_errror_message("Field was empty")
            return False
        return True

    def __from_str__(self):
        pass
