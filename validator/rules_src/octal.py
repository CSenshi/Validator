from validator.rules_src import Rule


class Octal(Rule):
    """
    The field under validation must be an octal number

    Examples:
    >>> from validator import validate

    >>> reqs = {"date" : "73021"}
    >>> rule = {"date" : "octal"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"date" : "0o73021"}
    >>> rule = {"date" : "octal"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"date" : "23489"}
    >>> rule = {"date" : "octal"}
    >>> validate(reqs, rule)
    False
    """

    aliases = ["oct", "octal"]

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        # Try to convert it to the octal.
        try:
            _ = Octal.convert(arg)
            return True
        except:
            # if transfered to exception we know its not octal.
            self.set_error(f"Expected String to be in Octal format, Got: {arg}")
            return False

    @staticmethod
    def convert(val):
        if isinstance(val, int):
            return val
        return int(val, 8)

    def __from_str__(self):
        pass
