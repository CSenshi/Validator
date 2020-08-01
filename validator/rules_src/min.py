from validator.rules_src import Rule
from validator.rules_src.size import Size
from validator import utils


class Min(Rule):
    """
    The field under validation must be greater than or equal to a minimum value.
    Given value is evaluated according to `Size` rule

    Examples:
    >>> from validator import validate

    >>> reqs = {"age" : 23}
    >>> rule = {"age" : "min:18"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"age" : 13}
    >>> rule = {"age" : "min:18"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self, min_value):
        Rule.__init__(self)
        self.min = min_value

    def check(self, arg):
        # Evaluate to Size rule
        size = Size.size_value(arg, self.rpv)
        if size is None:
            self.set_error(f"Could not get size from data. type = {type(arg)}")
            return False
        if size < self.min:
            self.set_error(f"Expected Maximum: {self.min}, Got: {size}")
            return False

        return True

    def __from_str__(self):
        if utils.RepresentsInt(self.min):
            self.min = int(self.min)
        else:
            # ToDo: Handle Error
            pass
