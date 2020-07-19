from validator.rules_src import Rule


class Accepted(Rule):
    """
    The field under validation must be 'yes', 'on', '1', or 'true' as String or True as boolena. This is useful for validating "Terms of Service" acceptance.


    Examples:
    >>> from validator import validate

    >>> reqs = {'value' : '1'}
    >>> rule = {'value' : 'accepted'}
    >>> validate(reqs, rule)
    True

    >>> reqs = {'value' : '0'}
    >>> rule = {'value' : 'accepted'}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        if isinstance(arg, bool):
            if arg == False:
                self.set_errror_message(f"Expected True, Got: {arg} ({type(arg)})")
                return False
            return True
        elif isinstance(arg, str):
            valids = ["true", "1", "on", "yes"]
            for valid_str in valids:
                if valid_str.lower() == arg.lower():
                    return True

            self.set_errror_message(f"Expected to be any of valid strings, Got: {arg}")
            return False
        else:
            self.set_errror_message(f"Expected type [Str/Bool], Got: {type(arg)}")
            return False

    def __from_str__(self):
        pass
