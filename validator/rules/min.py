from validator.rules import Rule


class Min(Rule):
    """
    >>> TrueMin = Min(18)
    >>> TrueMin(23)
    True

    >>> TrueMin = Min(18)
    >>> TrueMin(15)
    False
    """

    def __init__(self, min_value):
        self.min_value = min_value

    def __call__(self, arg):
        return self.min_value <= arg
