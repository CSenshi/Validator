from validator import rules as R
import re

# Some needed Variables
target_char, target_regex = ':', '|'

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
        # First step. Split whole string to array.
        mid_arr = re.split(r'[' + target_regex + ']', self.value)

        print(mid_arr)

        # Second step: Loop throught array and initialize class objects.
        for class_str in mid_arr:
            class_str = class_str.capitalize()

            if target_char in class_str:
                # Split by target character
                target_arr = class_str.split(target_char)
                class_name, class_arg = target_arr

                # Initialize class
                my_class = R.__all__[class_name](class_arg)
                my_class.__from_str__()

                print(my_class(25))  # Just for checking
            else:
                R.__all__[class_str]

        return 0
