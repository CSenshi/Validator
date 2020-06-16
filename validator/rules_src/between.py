from validator.rules_src.max import Max
from validator.rules_src.min import Min


class Between(Max, Min):
    """
    The field under validation must have a size between the given min and max 

    Examples:
    >>> Between(2, 15).check(23)
    False

    >>> Between(2, 15).check(12)
    True
    """

    def __init__(self, min_value, max_value):
        Min.__init__(self, min_value)
        Max.__init__(self, max_value)

    def check(self, arg):
        if Min.check(self, arg) and Max.check(self, arg):
            return True

        self.set_errror_message(
            f"Expected Between: {self.min_value} and {self.max_value}, Got: {arg}"
        )
        return False

    def __from_str__(self):
        Min.__from_str__(self)
        Max.__from_str__(self)
