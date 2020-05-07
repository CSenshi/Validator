from validator.__parser__.translator import Translator


class Parser:
    def __init__(self, rules):
        self.rules = rules
        self.result_rules = {}

    def parse(self):
        self.parsed_rules = {
            key: Translator(self.rules[key]).translate() for key in self.rules
        }
        return self.parsed_rules
