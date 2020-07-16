import re
from validator.rules_src import Rule
from validator.rules_src.IP import IP
from urllib.parse import urlparse
from urllib.parse import unquote


class URL(Rule):
    """
    The field under validation must be formatted as an url

    Examples:
    >>> from validator import validate

    >>> reqs = {"url_" : "abcdef.gh"}
    >>> rule = {"url_" : "url"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"url_" : "nourl"}
    >>> rule = {"url_" : "url"}
    >>> validate(reqs, rule)
    False
    """

    # checkScheme checks if scheme is valid
    def checkScheme(self, arg):
        return True

    # checkPort checks if port is valid
    def checkPort(self, arg):
        try:
            oc = int(arg)
            return oc >= 0 and oc <= 65535
        except Exception:
            return False

    # checkNetloc checks if netloc is valid
    def checkNetloc(self, arg):
        if arg == "":
            return False
        if arg.count(":") > 1:
            return False
        if arg.count(":") == 1:
            withPort = arg.split(":")
            arg = withPort[0]
            port = withPort[1]
            if not self.checkPort(port):
                return False

        if IP.check(self, arg):
            return True

        if arg == "localhost":
            return True

        return arg.count(".") > 0

    # checkPath checks if path is valid
    def checkPath(self, arg):
        return True

    # checkParams checks if params are valid
    def checkParams(self, arg):
        return True

    # checkQuery checks if query is valid
    def checkQuery(self, arg):
        if arg == "":
            return True
        params = arg.split("&")
        for param in params:
            if param == "":
                return False
            if param[0] == "=":
                return False
            if param[-1] == "=":
                return False
            if param.count("=") != 1:
                return False
        return True

    # checkFragment checks if fragment is valid
    def checkFragment(self, arg):
        return True

    def __init__(self):
        Rule.__init__(self)
        IP.__init__(self)

    def check(self, arg):
        try:
            url = unquote(arg)
            result = urlparse(url)
        except Exception as identifier:
            self.set_errror_message(f"Expected a Mail, Got: {str(identifier)}")
            return False

        if not self.checkScheme(result.scheme):
            self.set_errror_message("incorrect scheme")
            return False
        if result.scheme == "":
            return self.check("https://" + arg)

        if not self.checkNetloc(result.netloc):
            self.set_errror_message("incorrect netloc")
            return False
        if not self.checkPath(result.path):
            self.set_errror_message("incorrect path")
            return False
        if not self.checkParams(result.params):
            self.set_errror_message("incorrect params")
            return False
        if not self.checkQuery(result.query):
            self.set_errror_message("incorrect query")
            return False
        if not self.checkFragment(result.fragment):
            self.set_errror_message("incorrect fragment")
            return False
        return True

    def __from_str__(self):
        IP.__from_str__(self)
