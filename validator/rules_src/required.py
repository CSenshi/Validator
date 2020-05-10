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
        if not arg:
            return False
        return True

    def __from_str__(self):
        pass
