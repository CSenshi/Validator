from validator.rules_src import Rule


class Alpha(Rule):
    """
    The field under validation must be entirely alphabetic characters

    Examples:
    >>> from validator import validate

    >>> reqs = {'value' : 'KillerBunny'}
    >>> rule = {'value' : 'alpha'}
    >>> validate(reqs, rule)
    True

    >>> reqs = {'value' : '326forever'}
    >>> rule = {'value' : 'alpha'}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        if not isinstance(arg, str):
            self.set_error(f"Expected: Type str, Got: {type(arg)}")
            return False

        if not arg.isalpha():
            self.set_error(f"Expected all characters to be alphabetic [a-zA-z]")
            return False

        return True

    def __from_str__(self):
        pass
