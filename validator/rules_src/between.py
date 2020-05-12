from validator.rules_src.max import Max
from validator.rules_src.min import Min


class Between(Max, Min):
    """
    >>> TrueBetween = Between(2, 15)
    >>> TrueBetween(23)
    False

    >>> TrueBetween = Between(2, 15)
    >>> TrueBetween(12)
    True
    """

    def __init__(self, min_value, max_value):
        Min.__init__(self, min_value)
        Max.__init__(self, max_value)

    def __call__(self, arg):
        return Min.__call__(self, arg) and Max.__call__(self, arg)

    def __from_str__(self):
        Min.__from_str__(self)
        Max.__from_str__(self)
