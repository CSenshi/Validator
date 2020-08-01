from validator.rules_src import Rule
from uuid import UUID


class UUIDv1(Rule):
    """
    The field under validation must be formatted as an uuidv1

    Examples:
    >>> from validator import validate

    >>> reqs = {'data' : 'eb241bb4-c087-11ea-b3de-0242ac130004'}
    >>> rule = {'data' : 'uuidv1'}
    >>> validate(reqs, rule)
    True

    >>> reqs = {'data' : 'bba617b4-364b-4a0d-9e96-cb8a24ef1bec'}
    >>> rule = {'data' : 'uuidv1'}
    >>> validate(reqs, rule) # It fails because data is uuidv4
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        try:
            uuid = UUID(arg)

            if uuid.version is None:
                self.set_error(f"Expected: UUIDv1, but no version was found")
                return False

            if uuid.version != 1:
                self.set_error(f"Expected: UUIDv1, Got: UUIDv{uuid.version}")
                return False

            return True
        except Exception as e:
            self.set_error(f"Expected: UUIDv1, Got: {e}")
            return False

    def __from_str__(self):
        pass
