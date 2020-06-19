class RulePipeValidator:
    def __init__(self, data, rules):
        self.data = data
        self.rules = rules
        self.errors_on_key = {}

    def execute(self):
        result = True
        for rule in self.rules:
            if not rule(self.data):
                result = False
                self.errors_on_key[rule.get_class_name()] = rule.get_error_message()
        return result

    def get_error_messages(self):
        return self.errors_on_key
