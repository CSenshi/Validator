from validator.rules_src import Rule
from uuid import UUID


class UUIDv4(Rule):
    """
    The field under validation must be formatted as an uuidv4
    Examples:
    >>> from validator import validate
    >>> reqs = {'val' : '81368b76-31e9-41db-b28c-8c029cb435f0'}
    >>> rule = {'val' : 'uuidv4'}
    >>> validate(reqs, rule) 
    True

    >>> reqs = {'val' : 'a3bb189e-8bf9-3888-9912-ace4e6543002'}
    >>> rule = {'val' : 'uuidv4'}
    >>> validate(reqs, rule) #It fails because data is uuidv3
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        try:
            uuid = UUID(arg)
            if uuid.version == 4:
                return True
            else:
                self.set_errror_message(f"Expected a uuid of version 4, Got uuid of version {uuid.version}")
            return False
        except Exception as e:
            self.set_errror_message(f"Expected a UUIDv4, Got: {e}")
            return False

        return True

    def __from_str__(self):
        pass
