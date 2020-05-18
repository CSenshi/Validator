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
        if arg is None:
            return False
        if hasattr(arg, "__len__"):
            return len(arg) != 0
        return True

    def __from_str__(self):
        pass
