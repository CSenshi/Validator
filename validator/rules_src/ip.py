import re
from validator.rules_src import Rule
from validator.rules_src.ipv4 import IPv4
from validator.rules_src.ipv6 import IPv6


class IP(IPv4, IPv6):
    """
    The field under validation must be an IP address.

    Examples:
    >>> from validator import validate

    >>> reqs = {"ip_addr" : "192.168.0.1" }
    >>> rule = {"ip_addr" : "ip"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"ip_addr" : "0.123:2:1" }
    >>> rule = {"ip_addr" : "ip"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        IPv4.__init__(self)
        IPv6.__init__(self)

    def check(self, arg):
        return IPv4.check(self, arg) or IPv6.check(self, arg)

    def __from_str__(self):
        pass
