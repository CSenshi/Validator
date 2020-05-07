from validator.__parser__.parser import Parser


class Validator:
    def __init__(self, request, rules):
        self.request = request
        self.rules = Parser(rules).parse()

    def validate(self):
        # ToDo: Implement Validation
        return True
