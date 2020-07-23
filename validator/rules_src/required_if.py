from validator.rules_src.required import Required


class RequiredIf(Required):
    """
    The field under validation must be present and not empty if the anotherfield field is equal to any value.

    Examples:
    >>> from validator import validate

    >>> reqs = {'under_age' : 'no'}
    >>> rule = {'parent' : 'required_if:under_age,yes'}
    >>> validate(reqs, rule)
    True

    >>> reqs = {'under_age' : 'yes',
    ...         'parent': 'John Doe'}
    >>> rule = {'parent' : 'required_if:under_age,yes'}
    >>> validate(reqs, rule)
    True

    >>> reqs = {'under_age' : 'yes'}
    >>> rule = {'parent' : 'required_if:under_age,yes'}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self, field_name, field_val):
        Required.__init__(self)
        self.field_name = field_name
        self.field_val = field_val

    def check(self, arg):
        if not self.rw.req_contains_field(self.field_name):
            return True

        field_value = self.rw.get_field_data(self.field_name)

        if field_value != self.field_val:
            return True

        return Required.check(self, arg)

    def __from_str__(self):
        pass
