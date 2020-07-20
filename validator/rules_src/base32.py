from validator.rules_src import Rule
import base64


class Base32(Rule):
    """
    The field under validation must be a valid Base32 encoded


    Examples:
    >>> from validator import validate

    >>> reqs = {"data" : "KZAUYSKEIFKE6URAIZKFOII="}
    >>> rule = {"data" : "base32"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"data" : "Not Encoded"}
    >>> rule = {"data" : "base32"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        try:
            base64.b32decode(arg)
            return True
        except Exception as e:
            self.set_error(e)
        return False

    def __from_str__(self):
        pass
