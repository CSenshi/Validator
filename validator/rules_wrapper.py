from .rule_pipe_validator import RulePipeValidator as RPV


class RulesWrapper:
    def __init__(self, request, rules):
        self.request = request
        self.rules = rules
        self.errors = {}
        self.validated_data = {}
        self.result = False

    def run(self):
        # prepare variables
        result = True

        # at this point all rules are being correctly passed
        for key in self.rules:
            rules = self.rules[key]

            if key not in self.request:
                data = None
            else:
                data = self.request[key]

            # Interface for rules
            rpv = RPV(data, rules, self)
            rpv_result = rpv.execute()
            errors_on_key = rpv.get_errors()

            # if current validation fails change final result
            if rpv_result:
                self.validated_data[key] = data
            else:
                result = rpv_result
                self.errors[key] = errors_on_key

        self.result = result

    def get_errors(self):
        return self.errors

    def get_result(self):
        return self.result

    def req_contains_field(self, field_name):
        return field_name in self.request

    def get_field_data(self, field_name):
        return self.request[field_name]

    def get_validated_data(self):
        return self.validated_data
