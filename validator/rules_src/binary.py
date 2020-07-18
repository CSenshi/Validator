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

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        # Try to convert it to the binary.
        try:
            result = int(arg, 2)
            # if not error then given string is really binary.
            return True
        except:
            # if transfered to exception we know its not binary.
            self.set_errror_message("Specified String is not binary format!")
            return False

    def __from_str__(self):
        pass
