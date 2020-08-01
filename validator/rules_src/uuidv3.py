from validator.rules_src import Rule
from uuid import UUID


class UUIDv3(Rule):
    """
    The field under validation must be formatted as an uuidv3

    Examples:
    >>> from validator import validate

    >>> reqs = {'data' : 'a3bb189e-8bf9-3888-9912-ace4e6543002'}
    >>> rule = {'data' : 'uuidv3'}
    >>> validate(reqs, rule)
    True

    >>> reqs = {'data' : 'bba617b4-364b-4a0d-9e96-cb8a24ef1bec'}
    >>> rule = {'data' : 'uuidv3'}
    >>> validate(reqs, rule) # It fails because data is uuidv4
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        try:
            uuid = UUID(arg)

            if uuid.version is None:
                self.set_error(f"Expected: UUIDv3, but no version was found")
                return False

            if uuid.version != 3:
                self.set_error(f"Expected: UUIDv3, Got: UUIDv{uuid.version}")
                return False

            return True
        except Exception as e:
            self.set_error(f"Expected: UUIDv3, Got: {e}")
            return False

    def __from_str__(self):
        pass
