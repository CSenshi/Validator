from validator.__parser__.parser import Parser
from validator import rules as R
from validator import exceptions as exc

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
        # check for internal error (incorrect rules)
        if not self.check_rules():
            raise exc.RulesFormatError

    def validate(self):
        # prepare variables
        result = True
        errors = {}

        # at this point all rules are being correctly passed
        for key in self.rules:
            rules_array = self.rules[key]
            req_value = self.request[key]
            errors_on_key = {}

            for rule in rules_array:
                if not rule(req_value):
                    result = False
                    errors_on_key[rule.get_class_name()] = rule.get_error_message()

            if errors_on_key:
                errors[key] = errors_on_key

        return result, errors

    def check_rules(self):
        # check for rules' type (should be dictionary)
        if not type(self.rules) is dict:
            False

        for _, value in self.rules.items():
            # check for dictionary's value's type (should be list)
            if not type(value) is list:
                False
            for rule in value:
                # check for each value being R.Rule class instance
                if not isinstance(rule, R.Rule):
                    False

        return True
