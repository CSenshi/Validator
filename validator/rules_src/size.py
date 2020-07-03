from validator.rules_src import Rule
from validator.rules_src.integer import Integer
from validator.rules_src.list import List
from validator import utils


class Size(Integer, List):
    """
    The field under validation must have a size matching the given value. 
    For string data, value corresponds to the number of characters.
    For numeric data, value corresponds to a given integer value (the attribute must also have the numeric or integer rule). 
    For an array, size corresponds to the count of the array. 

    Examples:
    >>> from validator import validate

    >>> reqs = {'value' : 'string'}
    >>> rule = {'value' : 'size:6'}
    >>> validate(reqs, rule)
    True

    >>> reqs = {'value' : 'string'}
    >>> rule = {'value' : 'size:12'}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self, size):
        Integer.__init__(self)
        List.__init__(self)

        self.size = size

    def check(self, arg):
        converted_size = Size.size_value(arg, self.rpv)
        if converted_size == None:
            self.set_errror_message(f"Could not get size from data. type = {type(arg)}")
            return False

        if converted_size != self.size:
            self.set_errror_message(f"Expected Size:{self.size}, Got:{converted_size}")
            return False

        return True

    @staticmethod
    def size_value(arg, rpv):
        try:
            # Check With RPV for other rules
            if Integer in rpv:
                return int(arg)
            elif List in rpv:
                return len(arg)

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
