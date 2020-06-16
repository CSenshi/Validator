import re
from validator.rules_src import Rule
from validator.rules_src.IPv4 import IPv4
from validator.rules_src.IPv6 import IPv6


class IP(IPv4, IPv6):
    """
    The field under validation must be an IP address.

    Examples:
    >>> IP().check('127.0.0.1')
    True
    
    >>> IP().check('0.299.2.1')
    False
    """

    def __init__(self):
        IPv4.__init__(self)
        IPv6.__init__(self)

    def check(self, arg):
        return IPv4.check(self, arg) or IPv6.check(self, arg)

    def __from_str__(self):
        pass
