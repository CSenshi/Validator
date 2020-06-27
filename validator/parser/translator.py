from validator import rules as R
import re
import inspect
from validator import exceptions as exc


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
            rule = None
            if isinstance(elem, str):
                rule = self._translate_str(elem)
            elif isinstance(elem, R.Rule):
                rule = elem
            elif inspect.isclass(elem) and issubclass(elem, R.Rule):
                rule = self._translate_class(elem)
            elif callable(elem):
                rule = self._translate_func(elem)
            else:
                raise exc.UnknownTranslatorArgError
            if rule:
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

    def _translate_str(self, elem):
        """
        Translates strings to Rule instances
        "required" -> R.Required()
        "between:10,20" -> R.Between(10, 20)
        """
        if not elem:
            return []

        # split example: required_if
        class_str = "".join(elem.lower().split("_"))
        args = []
        if target_char in class_str:
            # extract rule_name and arguments from string
            class_str, args_str = class_str.split(target_char)
            # Split arguments into array
            args = args_str.split(target_args)

        # Initialize class
        if not class_str in R.__all__:
            raise exc.NoRuleError

        init_rule = R.__all__[class_str]

        # Check for arguments count
        if not self._validate_args_count(init_rule, args):
            raise exc.ArgsCountError

        rule_instance = init_rule(*args)
        rule_instance.__from_str__()

        return rule_instance

    def _translate_class(self, elem):
        """
        Translates Rule classes to Rule Instances
        R.Required -> R.Required()
        """
        # Chechk for arguments count
        if not self._validate_args_count(elem, []):
            raise exc.ArgsCountError

        return elem()

    def _translate_func(self, elem):
        """
        Translates Function to Rule Instances
        
        def test_func(x):
            ...
            return True

        For this example new rule will be created, for which
        check() method will evaluate to test_func
        """
        func_rule = R.Rule()
        func_rule.override_check(elem)
        return func_rule

    def _validate_args_count(self, init_rule, args):
        a = inspect.getfullargspec(init_rule)
        # ToDo: check for positional arguments
        return len(args) + 1 == len(a.args)
