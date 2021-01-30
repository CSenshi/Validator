from validator.rules_src import Rule


class Same(Rule):
    """
    The given field must match the field under validation

    Examples:
    >>> from validator import validate

    >>> reqs = {"old_pass": "password",
    ...         "new_pass": "password"}
    >>> rule = {"new_pass": "same:old_pass"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"old_pass": "password",
    ...         "new_pass": "changed_password"}
    >>> rule = {"new_pass": "same:old_pass"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self, field_name):
        Rule.__init__(self)
        self.field_name = field_name

    def check(self, arg):
        if not self.rw.req_contains_field(self.field_name):
            self.set_error(f"Field {self.field_name} is not in the list")
            return False

        field_value = self.rw.get_field_data(self.field_name)

        # 1. check for type
        if type(field_value) != type(arg):
            self.set_error(
                f"Expected: {arg}({type(arg)}), Got: {field_value}({type(field_value)})"
            )
            return False

        # 2. check for value
        if field_value != arg:
            self.set_error(f"Expected: {arg}, Got: {field_value}")
            return False

        return True

    def __from_str__(self):
        pass
