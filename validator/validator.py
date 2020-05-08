from validator.__parser__.parser import Parser

"""
Validator class takes 2 inputs:
1. request to be validated
2. rules to be validated with

Following class is responsible for validating request with given rules
"""


class Validator:
    def __init__(self, request, rules):
        self.request = request
        self.rules = Parser(rules).parse()

    def validate(self):
        # check for internal error (incorrect rules)
        self.check_rules()

        # at this point all rules are being correctly passed
        for key in self.rules:
            rules_array = self.rules[key]
            req_value = self.request[key]
            for rule in rules_array:
                if not rule(req_value):
                    return False
        return True

    def check_rules(self):
        pass
