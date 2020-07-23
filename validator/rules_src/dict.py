from validator.rules_src import Rule


class Dict(Rule):
    """
    The field under validation must be a dictionary (Python map)


    Examples:
    >>> from validator import validate

    >>> reqs = {"data" : {"key1" : "val1", "key2" : "val2"} }
    >>> rule = {"data" : "dict"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"data" : ["val1", "val2", "val3", "val4"]}
    >>> rule = {"data" : "dict"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        if isinstance(arg, dict):
            return True

        self.set_error(f"Expected type dict, Got:{type(arg)}")
        return False

    def __from_str__(self):
        pass
