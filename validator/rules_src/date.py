from validator.rules_src import Rule
from dateutil.parser import parse


class Date(Rule):
    """
    The field under validation must be an Integer

    Examples:
    >>> from validator import validate

    >>> reqs = {"date" : "25-08-1900"}
    >>> rule = {"date" : "date"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"date" : "32-12-2020"}
    >>> rule = {"date" : "date"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        try:
            resp = parse(arg)
            return True
        except ValueError as err:
            self.set_error(f"Invalid: {err}")
        return False

    def __from_str__(self):
        pass
