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
        Rule.__init__(self)
        self.regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    def __call__(self, arg):
        if re.search(self.regex, arg) is not None:
            return True

        err_msg = f"Expected a Mail, Got: {arg}"
        self.set_errror_message(err_msg)
        return False

    def __from_str__(self):
        pass
