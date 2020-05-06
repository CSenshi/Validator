import importlib
import os
import pkgutil
from pathlib import Path

"""
Import all modules from Rules folder dynamicly
"""

# Iterate each module in the given package
for (_, file, _) in pkgutil.iter_modules([Path(__file__).parent]):
    # Get Absolute Path
    module_abs_path = f"Validator.Rules.{file}"

    pkg = importlib.import_module(module_abs_path)

    # Import all classes from given modules
    names = [x for x in pkg.__dict__ if not x.startswith("_")]
    globals().update({k: getattr(pkg, k) for k in names})
