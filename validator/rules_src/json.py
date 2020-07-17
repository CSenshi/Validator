from validator.rules_src import Rule
import json


class JSON(Rule):
    """
    The field under validation must be formatted as an JSON

    Examples:
    >>> from validator import validate

    >>> reqs = {"value" : '{ "age":100}'}
    >>> rule = {"value" : "json"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"value" : "aaa.com"}
    >>> rule = {"value" : "json"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        try:
            _ = json.loads(arg)
        except Exception as e:
            self.set_errror_message(f"Incorrect JSON: {e}")
            return False

        return True

    def __from_str__(self):
        pass
