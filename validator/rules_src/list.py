from validator.rules_src import Rule


class List(Rule):
    """
    The field under validation must be a list (Python array)

    Examples:
    >>> from validator import validate

    >>> reqs = {"arr" : [1, 2, 3]}
    >>> rule = {"arr" : "list"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"arr" : 123}
    >>> rule = {"arr" : "list"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        if isinstance(arg, list):
            return True

        self.set_error(f"Expected type list, Got:{type(arg)}")
        return False

    def __from_str__(self):
        pass
