from validator.rules_src import Rule


class Decimal(Rule):
    """
    The field under validation must be a decimal number

    Examples:
    >>> from validator import validate

    >>> reqs = {'value' : '23'}
    >>> rule = {'value' : 'decimal'}
    >>> validate(reqs, rule)
    True

    >>> reqs = {'value' : '2F'}
    >>> rule = {'value' : 'decimal'}
    >>> validate(reqs, rule)
    False
    """

    aliases = ["dec", "decimal"]

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        # Try to convert it to the octal.
        try:
            _ = Decimal.convert(arg)
            return True
        except:
            # if transfered to exception we know its not octal.
            self.set_error(f"Expected String to be in Octal format, Got: {arg}")
            return False

    @staticmethod
    def convert(val):
        if isinstance(val, int):
            return val
        return int(val, 10)

    def __from_str__(self):
        pass
