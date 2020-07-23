from validator.rules_src import Rule
import base64


class Base64(Rule):
    """
    The field under validation must be a valid Base64 encoded


    Examples:
    >>> from validator import validate

    >>> reqs = {"data" : "VmFsaWRhdG9yIEZUVyE="}
    >>> rule = {"data" : "base64"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"data" : "Not Encoded"}
    >>> rule = {"data" : "base64"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        try:
            base64.b64decode(arg)
            for i in arg:
                if (not i.isalnum()) and i not in ["+", "/", "="]:
                    self.set_error("Invalid literal in input")
                    return False
            return True
        except Exception as e:
            self.set_error(e)
        return False

    def __from_str__(self):
        pass
