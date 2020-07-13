from validator.rules_src import Rule


class String(Rule):
    """
    The field under validation must be a String

    Examples:
    >>> from validator import validate

    >>> reqs = {"value" : "some string"}
    >>> rule = {"value" : "string"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"value" : 17}
    >>> rule = {"value" : "string"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        return isinstance(arg, str)

    def __from_str__(self):
        pass
