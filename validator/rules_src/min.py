from validator.rules_src import Rule
from validator.rules_src.size import Size


class Min(Rule):
    """
    The field under validation must be greater than or equal to a minimum value 

    Examples:
    >>> Min(2).check('Min')
    True

    >>> Min(4).check('Min')
    False
    """

    def __init__(self, min_value):
        Rule.__init__(self)
        self.min_value = min_value

    def check(self, arg):
        converted_size = Size.size_value(arg, self.rpv)
        if converted_size == None:
            self.set_errror_message(f"Could not get size from data. type = {type(arg)}")
            return False
        if converted_size < self.min_value:
            self.set_errror_message(
                f"Expected Maximum: {self.min_value}, Got: {converted_size}"
            )
            return False

        return True

    def __from_str__(self):
        self.min_value = int(self.min_value)
