import re
from validator.rules_src import Rule


class Mail(Rule):
    """
    >>> TrueMail = Mail()
    >>> TrueMail('abcd@ef.gh')
    True

    >>> TrueMail = Mail()
    >>> TrueMail('aaa.com')
    False
    """

    def __init__(self):
        self.regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    def __call__(self, arg):
        return re.search(self.regex, arg) is not None

    def __from_str__(self):
        pass
