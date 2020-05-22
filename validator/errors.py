


# validate args count exception
class ArgsCountError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ArgsCountError, {} '.format(self.message)
        else:
            return 'ArgsCountError has been raised'


# No such a rule in rulles list exception 
class NoRuleError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'NoRuleError, {} '.format(self.message)
        else:
            return 'NoRuleError has been raised'

# Invalid arguments for translating exception
class UnknownTranslatorArgError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'UnknownTranslatorArgError, {} '.format(self.message)
        else:
            return 'UnknownTranslatorArgError has been raised'
