


# validate args count exception
class ArgsCountError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ArgsCountError, {} '.format(self.message)
        else:
            return 'ArgsCountError has been raised'


