#!/usr/bin/env python3
import os
import pkgutil

rules_src = f"validator/rules.py"
rules_file = open(rules_src, "w")

# import parrent rule class
rules_pkg_path = "validator.rules_src"
line = f"from {rules_pkg_path} import Rule \n\n"
rules_file.writelines(line)

# import all rules from rules_src module
for (_, file, _) in pkgutil.iter_modules(["validator/rules_src"]):
    class_name = file.capitalize()
    line = f"from {rules_pkg_path}.{file} import {class_name}\n"
    rules_file.write(line)
