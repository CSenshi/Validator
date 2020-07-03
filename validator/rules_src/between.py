from validator.rules_src.max import Max
from validator.rules_src.min import Min


class Between(Max, Min):
    """
    The field under validation must have a size between the given min and max 

    Examples:
    >>> from validator import validate

    >>> reqs = {"age" : 10}
    >>> rule = {"age" : "between:6,18"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"age" : 23}
    >>> rule = {"age" : "between:6,18"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self, min_value, max_value):
        Min.__init__(self, min_value)
        Max.__init__(self, max_value)

    def check(self, arg):
        if Min.check(self, arg) and Max.check(self, arg):
            return True
        return False

    def __from_str__(self):
        Min.__from_str__(self)
        Max.__from_str__(self)
