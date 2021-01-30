from validator.rules_src import Rule
from validator.rules_src.integer import Integer
from validator.rules_src.binary import Binary
from validator.rules_src.octal import Octal
from validator.rules_src.decimal import Decimal
from validator.rules_src.hex import Hex
from validator.rules_src.string import String
from validator.rules_src.list import List
from validator.rules_src.dict import Dict
from validator.rules_src.json import JSON
from validator import utils


class Size(Integer, List):
    """
    The field under validation must have a size matching the given value.


    * For string data, value corresponds to the number of characters.

    * For numeric data, value corresponds to a given integer value. The attribute must also have any of the number rules: decimal, binary, octal, hex.
      If Integer rule is given it checks for all four systems with given order

    * For collectons, size corresponds to the len() of the given argument. It works for: String, List, Dict, JSON

    Examples:
    >>> from validator import validate

    # Checks for given number system
    >>> reqs = {"value" : "42"}
    >>> rule = {"value" : "decimal|size:42"}
    >>> validate(reqs, rule) # Checks for Decimal Integer value
    True

    >>> reqs = {"value" : "0b101010"}
    >>> rule = {"value" : "binary|size:42"}
    >>> validate(reqs, rule) # Checks for Binary Integer value
    True

    >>> reqs = {"value" : "0o52"}
    >>> rule = {"value" : "octal|size:42"}
    >>> validate(reqs, rule) # Checks for Octal Integer value
    True

    >>> reqs = {"value" : "0x2a"}
    >>> rule = {"value" : "hex|size:42"}
    >>> validate(reqs, rule) # Checks for Hex Integer value
    True

    # Checks len() for given collections
    >>> reqs = {"value" : "something"}
    >>> rule = {"value" : "string|size:9"}
    >>> validate(reqs, rule) # Checks for string length
    True

    >>> reqs = {"value" : ["a", "b", "c"]}
    >>> rule = {"value" : "list|size:3"}
    >>> validate(reqs, rule) # Checks for List length
    True

    >>> reqs = {"value" : {"k1":"v1", "k2":"v2", "k3":"v3", "k4":"v4"}}
    >>> rule = {"value" : "dict|size:4"}
    >>> validate(reqs, rule) # Checks for Dictionary length
    True

    >>> reqs = {"value" : '{"name":"John", "age":31, "city":"New York"}'}
    >>> rule = {"value" : "json|size:3"}
    >>> validate(reqs, rule) # Checks for JSON length
    True
    """

    def __init__(self, size):
        Rule.__init__(self)
        self.size = size

    def check(self, arg):
        converted_size = Size.size_value(arg, self.rpv)
        if converted_size is None:
            self.set_error(f"Could not get size from data. type = {type(arg)}")
            return False

        if converted_size != self.size:
            self.set_error(f"Expected Size:{self.size}, Got:{converted_size}")
            return False

        return True

    @staticmethod
    def size_value(arg, rpv):
        try:
            # Check With RPV for other rules
            if Integer in rpv:
                return Integer.convert(arg)
            elif Binary in rpv:
                return Binary.convert(arg)
            elif Octal in rpv:
                return Octal.convert(arg)
            elif Decimal in rpv:
                return Decimal.convert(arg)
            elif Hex in rpv:
                return Hex.convert(arg)
            elif String in rpv:
                return len(arg)
            elif List in rpv:
                return len(arg)
            elif Dict in rpv:
                return len(arg)
            elif JSON in rpv:
                return len(JSON.convert(arg))

            # Check for compatible comparision
            if utils.CanBeComparedToInt(arg):
                return arg

            # Check for length, else convert to string and then check for len()
            if hasattr(arg, "__len__"):
                check_size = len(arg)
            else:
                converted = str(arg)
                check_size = len(converted)
            return check_size
        except:
            return None

    def __from_str__(self):
        if utils.RepresentsInt(self.size):
            self.size = int(self.size)
        else:
            # ToDo: Handle Error
            pass
