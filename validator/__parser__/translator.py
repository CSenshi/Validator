from validator import rules as R
import re

# Some needed Variables
target_char, target_regex, target_args = ":", "|", ","

user_level, mid_level, class_level = "user level", "mid level", "class level"

"""
Translator class is used by Parser class and implements translation
of one given generic rule to specified and final version

Example

>>> before_value     = "required|min:18|max:30|between:10,25"
>>> translated_value = [Rules.Required(), Rules.Min(18), Rules.max(30), Rules.between(10, 25)]

"""


class Translator:
    def __init__(self, value):
        self.value = value

    def __check__(self):
        level_flag = False
        print(self.value)
        if isinstance(self.value, str):  # Checking for first level
            mid_arr = re.split(r"[" + target_regex + "]", self.value)
            return level_flag, mid_arr

        elif isinstance(self.value, list):
            # Checking for mid level.
            if len(self.value) != 0 and isinstance(self.value[0], str):
                return level_flag, self.value

            return not level_flag, self.value  # Checking for class level

    def translate(self):
        # First step. Check for types and get array ready for looping.
        level_flag, mid_arr = self.__check__()
        new_rules = []

        # Check for code level
        if level_flag:
            return self.value  # It means we have already final format. Class level

        # Second step: Loop throught array and initialize class objects.
        for class_str in mid_arr:
            class_str = class_str.capitalize()
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

            new_rules.append(my_class)
        return new_rules
