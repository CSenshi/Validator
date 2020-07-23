from validator.rules_src import Rule
from validator.rules_src.binary import Binary
from validator.rules_src.octal import Octal
from validator.rules_src.decimal import Decimal
from validator.rules_src.hex import Hex


class Integer(Rule):
    """
    The field under validation must be an Integer

    Examples:
    >>> from validator import validate

    >>> reqs = {"num" : "23"}
    >>> rule = {"num" : "integer"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"num" : "value"}
    >>> rule = {"num" : "integer"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        if isinstance(arg, int):
            return True

        if not isinstance(arg, str):
            self.set_error(f"Expected Type of Int or Str, Got: {type(arg)}")
            return False

        try:
            _ = Integer.convert(arg)
            return True
        except:
            self.set_error(f"Expected String to be in Binary format, Got: {arg}")
            return False

    @staticmethod
    def convert(val):
        convert_funcs = [Decimal.convert, Binary.convert, Octal.convert, Hex.convert]
        for func in convert_funcs:
            try:
                return func(val)
            except:
                pass

        raise Exception("Couldn't convert number to any of numeric system", val)

    def __from_str__(self):
        pass
