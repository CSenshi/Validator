import importlib
import pkgutil
from pathlib import Path
from abc import ABCMeta


class Rule(metaclass=ABCMeta):
    def __init__(self):
        self.error_message = "error"
        self.rpv = []

    def __call__(self, arg):
        return self.check(arg)

    def check(self, arg):
        pass

    def __from_str__(self, arg):
        pass

    def get_class_name(self):
        return type(self).__name__

    def set_errror_message(self, message):
        self.error_message = message

    def get_error_message(self):
        return self.error_message

    def set_rpv(self, rpv):
        self.rpv = rpv


# Iterate each module in the given package and fill __all__ dictionary
__all__ = {}
for (_, file, _) in pkgutil.iter_modules([Path(__file__).parent]):
    # Get Absolute Path
    module_abs_path = f"validator.rules_src.{file}"

    # Import given module
    pkg = importlib.import_module(module_abs_path)

    # Import all classes from given modules
    names = [x for x in pkg.__dict__ if not x.startswith("_")]

    # add class from module to globals() adn all (e.g. add 'min.Min')
    __all__.update({k.lower(): getattr(pkg, k) for k in names})
