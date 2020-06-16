import re
from validator.rules_src import Rule


class IPv4(Rule):
    """
    The field under validation must be an IPv4 address.

    Examples:
    >>> IPv4().check('127.0.0.1')
    True

    >>> IPv4().check('0.299.2.1')
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        octets = arg.split(".")

        # check number of octets
        if len(octets) != 4:
            self.set_errror_message(f"Expected four octets, Got: {len(octets)}")
            return False

        # check if all octets are digits
        for octet in octets:
            if not octet.isdigit():
                self.set_errror_message(f"Expected digits, Got: {octet}")
                return False
            if len(octet) > 3:
                self.set_errror_message(
                    f"Expected less than length of three octet, Got: {len(octet)}"
                )
                return False
            if not 0 <= int(octet) < 256:
                self.set_errror_message(f"Expected digit less than 256, Got: {octet}")
                return False

        return True

    def __from_str__(self):
        pass
