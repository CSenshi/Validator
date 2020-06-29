from validator.rules_src import Rule
from validator.rules_src.size import Size
from validator import utils


class Max(Rule):
    """
    The field under validation must be less than or equal to a maximum value 
    Given value is evaluated according to `Size` rule

    Examples:
    >>> Max(23).check('max_rule')
    True

    >>> Max(2).check('max_rule')
    False
    """

    def __init__(self, max_value):
        Rule.__init__(self)
        self.max = max_value

    def check(self, arg):
        # Evaluate to Size rule
        size = Size.size_value(arg, self.rpv)
        if size == None:
            self.set_errror_message(f"Could not get size from data. type = {type(arg)}")
            return False

        if size > self.max:
            self.set_errror_message(f"Expected Maximum: {self.max}, Got: {size}")
            return False

        return True

    def __from_str__(self):
        if utils.RepresentsInt(self.max):
            self.max = int(self.max)
        else:
            # ToDo: Handle Error
            pass
