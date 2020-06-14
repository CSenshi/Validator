import re
from validator.rules_src import Rule


class IPv4(Rule):
    """
    >>> TrueIPv4 = IPv4()
    >>> TrueIPv4('127.0.0.1')
    True

    >>> TrueIPv4 = IPv4()
    >>> TrueIPv4('0.299.2.1')
    False

    >>> TrueIPv4 = IPv4()
    >>> TrueIPv4('01.14.0.1')
    True
    """

    def __init__(self):
        Rule.__init__(self)

    def __call__(self, arg):
        octets = arg.split('.')

        # check number of octets
        if len(octets) != 4:
            f"Expected four octets, Got: {len(octets)}"
            return False

        # check if all octets are digits
        for octet in octets:
            if not octet.isdigit():
                f"Expected digits, Got: {octet}"
                return False
            if len(octet) > 3:
                f"Expected less than length of three octet, Got: {len(octet)}"
                return False
            if not 0 <= int(octet) < 256:
                f"Expected digit less than 256, Got: {octet}"
                return False

        return True

    def __from_str__(self):
        pass