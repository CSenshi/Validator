from validator.rules_src import Rule
from validator.rules_src.integer import Integer
from validator.rules_src.list import List


class Size(Integer, List):
    """
    The field under validation must have a size matching the given value. 
    For string data, value corresponds to the number of characters.
    For numeric data, value corresponds to a given integer value (the attribute must also have the numeric or integer rule). 
    For an array, size corresponds to the count of the array. 

    Examples:
    >>> Size(6).check('string')
    True

    >>> Size(12).check('string')
    False
    """

    def __init__(self, size):
        Integer.__init__(self)
        List.__init__(self)

        self.size = size

    def check(self, arg):
        if Integer in self.rpv:
            # RPV 1: with 'integer'
            if not Integer.check(self, arg):
                return False
            if int(arg) != self.size:
                self.set_errror_message(f"Expected Size:{self.size}, Got:{arg}")
                return False
            return True
        elif List in self.rpv:
            # RPV 2: with 'list'
            if not List.check(self, arg):
                return False
            if len(arg) != self.size:
                self.set_errror_message(f"Expected Size:{self.size}, Got:{len(arg)}")
                return False
            return True

        if hasattr(arg, "__len__"):
            check_size = len(arg)
        else:
            # convert to string and check size
            try:
                converted = str(arg)
                check_size = len(converted)
            except ValueError:
                # could not be converted to string
                self.set_errror_message(
                    f"Could not get size from data. type = {type(arg)}"
                )
                return False

        if check_size == self.size:
            return True

        self.set_errror_message(f"Expected Size:{self.size}, Got:{check_size}")
        return False

    def __from_str__(self):
        self.size = int(self.size)
