import re
from validator.rules_src import Rule


class Mail(Rule):
    """
    The field under validation must be formatted as an e-mail address 

    Examples:
    >>> Mail().check('abcd@ef.gh')
    True

    >>> Mail().check('aaa.com')
    False
    """

    def __init__(self):
        Rule.__init__(self)
        self.regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    def check(self, arg):
        if re.search(self.regex, arg) is not None:
            return True

        self.set_errror_message(f"Expected a Mail, Got: {arg}")
        return False

    def __from_str__(self):
        pass
