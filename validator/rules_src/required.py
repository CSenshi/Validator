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
        pass

    def __call__(self, arg):
        if arg is None or (hasattr(arg, "__len__") and len(arg) == 0):
            err_msg = "Field was empty"
            self.set_errror_message(err_msg)
            return False
        return True

    def __from_str__(self):
        pass
