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
        return arg.isalpha()

    def __from_str__(self):
        pass
