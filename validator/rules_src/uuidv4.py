from validator.rules_src import Rule
from uuid import UUID


class UUIDv4(Rule):
    """
    The field under validation must be formatted as an uuidv4

    Examples:
    >>> from validator import validate

    >>> reqs = {'data' : '81368b76-31e9-41db-b28c-8c029cb435f0'}
    >>> rule = {'data' : 'uuidv4'}
    >>> validate(reqs, rule)
    True

    >>> reqs = {'data' : 'a3bb189e-8bf9-3888-9912-ace4e6543002'}
    >>> rule = {'data' : 'uuidv4'}
    >>> validate(reqs, rule) # It fails because data is uuidv3
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        try:
            uuid = UUID(arg)

            if uuid.version is None:
                self.set_error(f"Expected: UUIDv4, but no version was found")
                return False

            if uuid.version != 4:
                self.set_error(f"Expected: UUIDv4, Got: UUIDv{uuid.version}")
                return False

            return True
        except Exception as e:
            self.set_error(f"Expected: UUIDv4, Got: {e}")
            return False

    def __from_str__(self):
        pass
