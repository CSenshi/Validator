from validator.rules_src import Rule


class Integer(Rule):
    """
    The field under validation must be an Integer

    Examples:
    >>> Integer().check('123')
    True

    >>> Integer().check('string')
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        if isinstance(arg, int):
            return True

        if isinstance(arg, str):
            if arg.startswith("-"):
                arg = arg[1:]
            return arg.isdigit()

        return False

    def __from_str__(self):
        pass
