from validator.rules_src import Rule


class Size(Rule):
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
        Rule.__init__(self)
        self.size = size

    def check(self, arg):
        #  ToDo: Check with rpv

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
        pass
