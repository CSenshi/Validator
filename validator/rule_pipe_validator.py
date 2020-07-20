class RulePipeValidator:
    def __init__(self, data, rules, rw=[]):
        # data to validate
        self.data = data

        # assign rules and set 'self' o each of them
        self.rules = rules
        [rule.set_rpv(self) for rule in rules]
        [rule.set_rw(rw) for rule in rules]

        # if validation fails we will fill errors dictionary
        self.errors_on_key = {}

    def execute(self):
        result = True
        for rule in self.rules:
            if not rule(self.data):
                result = False
                self.errors_on_key[rule.get_class_name()] = rule.get_error()
        return result

    def get_errors(self):
        return self.errors_on_key

    def __contains__(self, item):
        return any([type(rule) == item for rule in self.rules])
