import re
from validator.rules_src import Rule


class IPv6(Rule):
    """
    The field under validation must be an IPv6 address.

    Examples:
    >>> IPv6().check('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
    True

    >>> IPv6().check('2001:0db8:85a3:9876:1234:8a2e')
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):

        if arg.count("::") > 1:
            self.set_errror_message(
                f"Expected less than 2 consecutive colons, Got: {arg.count('::')}"
            )
            return False

        if arg[0] == ":" and arg[1] != ":":
            self.set_errror_message(f"Starts with colon")
            return False

        if arg[-1] == ":" and arg[-2] != ":":
            self.set_errror_message(f"Endss with colon")
            return False

        hextets = arg.split(":")
        if len(hextets) < 3:
            self.set_errror_message(f"Less than 3 sectors")
            return False

        case = len(hextets) == 9 and (
            arg[0] == arg[1] == ":" or arg[-1] == arg[-2] == ":"
        )

        if len(hextets) > 8 and not case:
            self.set_errror_message(
                f"More than 8 hextets with now trailing consecutive colons"
            )
            return False

        if len(hextets) != 8 and arg.count("::") == 0:
            self.set_errror_message(f"No apropriate number of hextets")
            return False

        for hextet in hextets:
            if len(hextet) == 0:
                continue

            if len(hextet) > 4:
                self.set_errror_message(
                    f"Maximum length of hextet is 4, Got: {len(hextet)}"
                )
                return False

            for num in hextet:
                if not ("0" <= num <= "9" or "a" <= num <= "f"):
                    self.set_errror_message(f"Invalid number {num}")
                    return False
        return True

    def __from_str__(self):
        pass
