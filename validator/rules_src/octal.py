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

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        # Try to convert it to the octal.
        try:
            result = int(arg, 8)
            # if not error then given string is really octal.
            return True
        except:
            # if transfered to exception we know its not octal.
            self.set_errror_message("Specified String is not Octal format!")
            return False

    def __from_str__(self):
        pass
