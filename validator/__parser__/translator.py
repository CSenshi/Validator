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

    def create_class(self, class_str):
        class_str = ''.join(class_str.lower().split('_'))
        # Devided between many args and zero args
        if target_char in class_str:
            # Split by target character
            target_arr = class_str.split(target_char)
            class_name, class_arg = target_arr

            class_arg = class_arg.split(target_args)
            # Initialize class
            my_class = R.__all__[class_name](*class_arg)
            my_class.__from_str__()
        else:
            my_class = R.__all__[class_str]()
        return my_class

    def translate(self):
        # First step. Check for types and get array ready for looping.
        level_flag, mid_arr = self.check_class()
        new_rules = []

        if level_flag:
            return mid_arr  # Which will be None

        # Second step: Loop throught array and initialize class objects.
        for class_str in mid_arr:
            # if string
            if isinstance(class_str, str):
                my_class = self.create_class(class_str)
                new_rules.append(my_class)
            else:  # To Do: checking class types or bad info types!!
                new_rules.append(class_str)
        return new_rules
