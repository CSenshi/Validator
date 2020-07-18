from validator.rules_src import Rule
from uuid import UUID


class UUID1(Rule):
    """
    The field under validation must be formatted as an uuid1

    Examples:
    >>> from validator import validate

    >>> reqs = {'data' : 'eb241bb4-c087-11ea-b3de-0242ac130004'}
    >>> rule = {'data' : 'uuid1'}
    >>> validate(reqs, rule)
    True
    >>> reqs = {'data' : 'bba617b4-364b-4a0d-9e96-cb8a24ef1bec'}
    >>> rule = {'data' : 'uuid1'}
    >>> validate(reqs, rule) # False, it's uuidv4
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        try:
            uuid = UUID(arg, version=1)
            return str(uuid) == arg
        except Exception as e:
            self.set_errror_message(f"Expected a UUID1, Got: {e}")
            return False

        return True

    def __from_str__(self):
        pass
