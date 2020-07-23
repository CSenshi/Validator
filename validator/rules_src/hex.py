from validator.rules_src import Rule


class Hex(Rule):
    """
    The field under validation must be a hexadecimal number

    Examples:
    >>> from validator import validate

    >>> reqs = {"date" : "A1B2c3"}
    >>> rule = {"date" : "hex"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"date" : "0xA1b2C3"}
    >>> rule = {"date" : "hex"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"date" : "abcdefgh"}
    >>> rule = {"date" : "hex"}
    >>> validate(reqs, rule)
    False
    """

    aliases = ["hex", "hexadecimal"]

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        # Try to convert it to the hex.
        try:
            _ = Hex.convert(arg)
            return True
        except:
            # if transfered to exception we know its not hex.
            self.set_error(f"Expected String to be in Hexadecimal format, Got: {arg}")
            return False

    @staticmethod
    def convert(val):
        if isinstance(val, int):
            return val
        return int(val, 16)

    def __from_str__(self):
        pass
