#!/usr/bin/env python3
import pkgutil

rules_src = f"validator/rules.py"
rules_file = open(rules_src, "w")

# import parrent rule class
rules_pkg_path = "validator.rules_src"
line = f"from {rules_pkg_path} import Rule\n"
rules_file.writelines(line)

# import __all__ object
line = f"from {rules_pkg_path} import __all__\n"
rules_file.writelines(line)

# import all rules from rules_src module
for (_, file, _) in pkgutil.iter_modules(["validator/rules_src"]):
    line = f"from {rules_pkg_path}.{file} import *\n"
    rules_file.write(line)
