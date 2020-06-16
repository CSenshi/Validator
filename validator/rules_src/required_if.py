from validator.rules_src.required import Required


class RequiredIf(Required):
    """
    Some Description...
    
    Examples:
    >>> RequiredIf('a').check('abc')
    True

    >>> RequiredIf('z').check('abc')
    False
    """

    def __init__(self, requirement):
        Required.__init__(self)
        self.requirement = requirement

    def check(self, arg):
        if Required.check(self, arg) and self.requirement in arg:
            return True

        self.set_errror_message(f"Required: {self.requirement} not in {arg}")
        return False

    def __from_str__(self):
        pass
