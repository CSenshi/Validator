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
        # ToDo: Implement Validation
        return True
