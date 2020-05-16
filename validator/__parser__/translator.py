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

    def translate(self):
        # First step. Check for types and get array ready for looping.
        arr = self._value_to_array()

        # Second step: Loop throught array and initialize class objects.
        rules_arr = []
        for elem in arr:
            if isinstance(elem, str):
                rule = self._translate_str(elem)
            elif isinstance(elem, R.Rule):
                rule = elem
            else:
                # ToDo: throw error
                continue
            rules_arr.append(rule)
        return rules_arr

    def _value_to_array(self):
        # if value is string transform to string
        if isinstance(self.value, str):
            return re.split("[" + target_regex + "]", self.value)

        # if value is array return
        if isinstance(self.value, list):
            return self.value

        # at this point we should return given value tranformed into array
        return [self.value]

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
            # ToDo: Throw Exception
            return None

        init_rule = R.__all__[class_str]

        # Chechk for arguments count
        if not self._validate_args_count(init_rule, args):
            # ToDo: Throw Exception
            return None

        rule_instance = init_rule(*args)
        rule_instance.__from_str__()

        return rule_instance

    def _validate_args_count(self, init_rule, args):
        a = inspect.getfullargspec(init_rule)
        # ToDo: check for positional arguments
        return len(args) + 1 == len(a.args)
