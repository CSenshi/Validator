from validator.rules_src import Rule
from validator.rules_src.size import Size
from validator import utils


class Max(Rule):
    """
    The field under validation must be less than or equal to a maximum value
    Given value is evaluated according to `Size` rule

    Examples:
    >>> from validator import validate

    >>> reqs = {"age" : 15}
    >>> rule = {"age" : "max:18"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"age" : 23}
    >>> rule = {"age" : "max:18"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self, max_value):
        Rule.__init__(self)
        self.max = max_value

    def check(self, arg):
        # Evaluate to Size rule
        size = Size.size_value(arg, self.rpv)
        if size is None:
            self.set_error(f"Could not get size from data. type = {type(arg)}")
            return False

        if size > self.max:
            self.set_error(f"Expected Maximum: {self.max}, Got: {size}")
            return False

        return True

    def __from_str__(self):
        if utils.RepresentsInt(self.max):
            self.max = int(self.max)
        else:
            # ToDo: Handle Error
            pass
