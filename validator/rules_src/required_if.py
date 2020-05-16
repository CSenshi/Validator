from validator.rules_src.required import Required

class RequiredIf(Required):
    """
    >>> TrueRequiredIf = RequiredIf('a')
    >>> TrueRequiredIf('abc')
    True

    >>> FalseRequiredIf = RequiredIf('z')
    >>> FalseRequiredIf('abc')
    False
    """

    def __init__(self, requirement):
        Required.__init__(self)
        self.requirement = requirement
        

    def __call__(self, arg):
        if not Required.__call__(self, arg):
            return False
        return self.requirement in arg

    def __from_str__(self):
        pass
