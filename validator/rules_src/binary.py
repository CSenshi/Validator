from validator.rules_src import Rule


class Binary(Rule):
    """
    The field under validation must be a binary number

    Examples:
    >>> from validator import validate

    >>> reqs = {"date" : "010101010010"}
    >>> rule = {"date" : "binary"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"date" : "0b010101010010"}
    >>> rule = {"date" : "binary"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"date" : "0123012"}
    >>> rule = {"date" : "binary"}
    >>> validate(reqs, rule)
    False
    """

    aliases = ["bin", "binary"]

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        # Try to convert it to the binary.
        try:
            _ = Binary.convert(arg)
            return True
        except:
            # if transfered to exception we know its not binary.
            self.set_error(f"Expected String to be in Binary format, Got: {arg}")
            return False

    @staticmethod
    def convert(val):
        if isinstance(val, int):
            return val
        return int(val, 2)

    def __from_str__(self):
        pass
