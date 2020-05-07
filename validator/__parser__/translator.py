from validator.rules import Rule


"""
Translator class is used by Parser class and implements translation
of one given generic rule to specified and final version

Example

>>> before_value     = "required|min:18"
>>> translated_value = [Rules.Required(), Rules.Min(18)]

"""


class Translator:
    def __init__(self, value):
        self.value = value

    def translate(self):
        # ToDo: Implement translation
        return self.value
