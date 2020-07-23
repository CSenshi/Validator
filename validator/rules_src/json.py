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
            _ = JSON.convert(arg)
        except Exception as e:
            self.set_error(f"Incorrect JSON: {e}")
            return False

        return True

    @staticmethod
    def convert(val):
        return json.loads(val)

    def __from_str__(self):
        pass
