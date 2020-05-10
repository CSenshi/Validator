from validator.rules_src import Rule


class Max(Rule):
    """
    >>> TrueMax = Max(18)
    >>> TrueMax(23)
    False

    >>> TrueMax = Max(18)
    >>> TrueMax(15)
    True
    """

    def __init__(self, max_value):
        self.max_value = max_value

    def __call__(self, arg):
        return self.max_value >= arg

    def __from_str__(self):
        self.max_value = int(self.max_value)
