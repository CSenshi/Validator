from validator import rules as R
import re
import inspect

# Some needed Variables
target_char, target_regex, target_args = ":", "|", ","

user_level, mid_level, class_level = "user level", "mid level", "class level"

"""
Translator class is used by Parser class and implements translation
of one given generic rule to specified and final version

Example

>>> before_value     = "required|min:18|between:10,25"
>>> translated_value = [Rules.Required(), Rules.Min(18), Rules.between(10, 25)]

"""


class Translator:
    def __init__(self, value):
        self.value = value

    def check_class(self):
        if isinstance(self.value, str):  # Checking for first level
            mid_arr = re.split(r"[" + target_regex + "]", self.value)
            return False, mid_arr

        elif isinstance(self.value, list):
            return False, self.value

        # Otherwise its broken object so lets return True and none
        return True, None

    def translate(self):
        # First step. Check for types and get array ready for looping.
        level_flag, mid_arr = self.check_class()

        if level_flag:
            return mid_arr  # Which will be None

        # Second step: Loop throught array and initialize class objects.
        new_rules = []
        for elem in mid_arr:
            if isinstance(elem, str):
                rule = self._translate_str(elem)
            elif isinstance(elem, R.Rule):
                rule = elem
            else:
                continue
            new_rules.append(rule)
        return new_rules


    def _translate_str(self, class_str):
        class_str = "".join(class_str.lower().split("_"))

        args = []
        if target_char in class_str:
            # extract rule_name and arguments from string
            class_str, args_str = class_str.split(target_char)
            # Split arguments into array
            args = args_str.split(target_args)

        # Initialize class
        if not class_str in R.__all__:
            # ToDo: change to throwing exception
            return None

        my_class = R.__all__[class_str](*args)
        my_class.__from_str__()

        return my_class
