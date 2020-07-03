from validator.rules_src import Rule


class Integer(Rule):
    """
    The field under validation must be an Integer

    Examples:
    >>> from validator import validate

    >>> reqs = {"num" : "23"}
    >>> rule = {"num" : "integer"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"num" : "value"}
    >>> rule = {"num" : "integer"}
    >>> validate(reqs, rule)
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
