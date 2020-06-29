from validator.rules_src import Rule
from validator.rules_src.size import Size
from validator import utils


class Min(Rule):
    """
    The field under validation must be greater than or equal to a minimum value.
    Given value is evaluated according to `Size` rule

    Examples:
    >>> Min(2).check('Min')
    True

    >>> Min(4).check('Min')
    False
    """

    def __init__(self, min_value):
        Rule.__init__(self)
        self.min = min_value

    def check(self, arg):
        # Evaluate to Size rule
        size = Size.size_value(arg, self.rpv)
        if size == None:
            self.set_errror_message(f"Could not get size from data. type = {type(arg)}")
            return False
        if size < self.min:
            self.set_errror_message(f"Expected Maximum: {self.min}, Got: {size}")
            return False

        return True

    def __from_str__(self):
        if utils.RepresentsInt(self.min):
            self.min = int(self.min)
        else:
            # ToDo: Handle Error
            pass
