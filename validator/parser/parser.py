from validator.parser.translator import Translator

"""
Parser class implements parsing from generic type of rules to specified

Example:
>>> rules = {"firstName": "required",
...          "lastName": "required",
...          "age": "required|min:18",
...          "mail": "required|mail"}

>>> rules = {"firstName": [Rules.Required()],
...          "lastName": [Rules.Required()],
...          "age": [Rules.Required(), Rules.Min(18)],
...          "mail": [Rules.Required(), Rules.Mail()]}

"""


class Parser:
    def __init__(self, rules):
        self.rules = rules
        self.result_rules = {}

    def parse(self):
        self.parsed_rules = {
            key: Translator(self.rules[key]).translate() for key in self.rules
        }
        return self.parsed_rules
