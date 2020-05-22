# validate args count exception
class ArgsCountError(Exception):
    pass


# No such a rule in rulles list exception
class NoRuleError(Exception):
    pass


# Invalid arguments for translating exception
class UnknownTranslatorArgError(Exception):
    pass


# Incorrect format for rules dictionary
class RulesFormatError(Exception):
    pass
