from validator.rules_src import Rule


class Required(Rule):
    """
    >>> TrueRequired = Required()
    >>> TrueRequired('Not Empty')
    True

    >>> FalseRequired = Required()
    >>> FalseRequired('')
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def __call__(self, arg):
        if arg is None or (hasattr(arg, "__len__") and len(arg) == 0):
            self.set_errror_message("Field was empty")
            return False
        return True

    def __from_str__(self):
        pass
