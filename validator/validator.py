from validator.__parser__.parser import Parser


class Validator:
    def __init__(self, request, rules):
        self.request = request
        self.rules = Parser(rules)

    def validate(self):
        return True
