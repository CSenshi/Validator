from validator.rules_src import Rule
from validator.rules_src.size import Size


class Max(Rule):
    """
    The field under validation must be less than or equal to a maximum value 

    Examples:
    >>> Max(23).check('max_rule')
    True

    >>> Max(2).check('max_rule')
    False
    """

    def __init__(self, max_value):
        Rule.__init__(self)
        self.max_value = max_value

    def check(self, arg):
        converted_size = Size.size_value(arg, self.rpv)
        if converted_size == None:
            self.set_errror_message(f"Could not get size from data. type = {type(arg)}")
            return False

        if converted_size > self.max_value:
            self.set_errror_message(
                f"Expected Maximum: {self.max_value}, Got: {converted_size}"
            )
            return False

        return True

    def __from_str__(self):
        self.max_value = int(self.max_value)
